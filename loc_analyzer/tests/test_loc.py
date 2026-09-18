import contextlib
import importlib.machinery
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
loader = importlib.machinery.SourceFileLoader("loc_analyzer", str(ROOT / "bin/loc"))
spec = importlib.util.spec_from_loader(loader.name, loader)
loc = importlib.util.module_from_spec(spec)
loader.exec_module(loc)


class Lines(unittest.TestCase):
    def test_physical_lines_include_blanks_and_final_unterminated_line(self):
        for data, expected in [(b"", 0), (b"\n", 1), (b"a\n\nb", 3),
                               (b"a\r\nb\r\n", 2), (b"# comment\n", 1),
                               (b"a\x0bb", 1)]:
            self.assertEqual(loc.text_lines(data), expected)

    def test_binary_and_non_utf8_are_not_text(self):
        self.assertIsNone(loc.text_lines(b"text\0binary\n"))
        self.assertIsNone(loc.text_lines(b"\xff\n"))


class Analysis(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.here = self.root / "analyzer"
        (self.here / "subjects").mkdir(parents=True)
        self.subject = {"subject": "sample", "sources": [
            {"id": "sample", "origin": "https://example.org/sample", "ref": "main"}]}
        self.config = self.here / "subjects/sample.json"
        self.config.write_text(json.dumps(self.subject))
        self.checkouts = self.root / "checkouts"
        self.repo = self.checkouts / "sample"
        self.repo.mkdir(parents=True)
        self.git("init", "-b", "main")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.invalid")
        self.git("commit", "--allow-empty", "-m", "root")
        root_sha = self.git("rev-parse", "HEAD")
        for path, data in {"code.py": b"# comment\n\nprint(1)", "README.MD": b"# Title\n\nDocs\n",
                           "empty.md": b"", "config.json": b"{}\n", "nul.md": b"x\0\n",
                           "non-utf8": b"\xff\n", "odd\nname.txt": b"one\ntwo\n",
                           "vendor/data.txt": b"data\n", "vendor2/data.txt": b"keep\n"}.items():
            p = self.repo / path
            p.parent.mkdir(exist_ok=True)
            p.write_bytes(data)
        (self.repo / "link.md").symlink_to("README.MD")
        self.git("add", ".")
        self.git("update-index", "--add", "--cacheinfo", f"160000,{root_sha},submodule")
        self.git("commit", "-m", "counted tree")
        self.sha = self.git("rev-parse", "HEAD")
        self.patch = patch.object(loc, "HERE", self.here)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        self.rd = self.here / "runs/sample/2026-09-18"

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.repo), *args],
                                       stderr=subprocess.DEVNULL, text=True).strip()

    def run_analysis(self):
        with contextlib.redirect_stdout(io.StringIO()):
            loc.run_analysis("sample", self.checkouts, "2026-09-18")
        return loc.check_run(self.rd)

    def test_counts_main_tree_not_dirty_worktree_or_checked_out_topic(self):
        self.git("checkout", "-b", "topic")
        (self.repo / "topic.py").write_text("new\n")
        self.git("add", "topic.py")
        self.git("commit", "-m", "topic")
        (self.repo / "code.py").write_text("dirty\n" * 100)
        (self.repo / "untracked.md").write_text("untracked\n")
        corpus, counts = self.run_analysis()
        src = counts["sources"][0]
        self.assertEqual(src["commit"], self.sha)
        self.assertEqual(src["implementation"], {"files": 5, "lines": 8})
        self.assertEqual(src["documentation"], {"files": 2, "lines": 3})
        self.assertEqual(src["skipped"], dict(binary=2, symlink=1, submodule=1, excluded=0))
        self.assertEqual(src["tracked_entries"], 11)
        self.assertEqual(loc.check_run(self.rd, self.checkouts), (corpus, counts))

    def test_exclusions_are_path_boundaries_and_are_recorded(self):
        self.subject["exclude"] = ["vendor/"]
        self.config.write_text(json.dumps(self.subject))
        _, counts = self.run_analysis()
        self.assertEqual(counts["sources"][0]["implementation"]["lines"], 7)
        self.assertEqual(counts["sources"][0]["skipped"]["excluded"], 1)

    def test_missing_main_does_not_fall_back_to_head_or_a_tag(self):
        self.git("checkout", "-b", "topic")
        self.git("tag", "main")
        self.git("branch", "-D", "main")
        with self.assertRaises(ValueError):
            self.run_analysis()
        self.assertFalse(self.rd.exists())

    def test_missing_checkout_leaves_no_partial_run(self):
        self.subject["sources"].append({"id": "missing", "origin": "https://example.org/missing"})
        self.config.write_text(json.dumps(self.subject))
        with self.assertRaises(ValueError):
            self.run_analysis()
        self.assertFalse(self.rd.exists())

    def test_existing_run_is_not_overwritten(self):
        self.run_analysis()
        before = (self.rd / "corpus.json").read_bytes()
        with self.assertRaisesRegex(ValueError, "already exists"):
            self.run_analysis()
        self.assertEqual((self.rd / "corpus.json").read_bytes(), before)

    def test_changed_evidence_totals_and_prose_each_fail_validation(self):
        self.run_analysis()
        for name in ("files.jsonl", "loc.json", "report.md"):
            with self.subTest(name=name):
                path = self.rd / name
                original = path.read_bytes()
                if name == "files.jsonl":
                    path.write_bytes(original + b"\n")
                elif name == "loc.json":
                    data = json.loads(original)
                    data["totals"]["implementation"] += 1
                    path.write_text(json.dumps(data))
                else:
                    path.write_bytes(original + b"extra prose\n")
                with self.assertRaises(ValueError):
                    loc.check_run(self.rd)
                path.write_bytes(original)

    def test_run_name_cannot_escape_the_runs_directory(self):
        with self.assertRaises(ValueError):
            loc.run_analysis("sample", self.checkouts, "../escape")


class CommittedRuns(unittest.TestCase):
    def test_every_committed_run_matches_its_per_file_evidence(self):
        paths = list((ROOT / "runs").glob("*/*/corpus.json"))
        self.assertTrue(paths)
        for path in paths:
            with self.subTest(run=path.parent):
                corpus, _ = loc.check_run(path.parent)
                refs = {s["id"]: s["ref"] for s in corpus["sources"]}
                if corpus["subject"] == "eunoia-ecosystem":
                    self.assertEqual(refs["cvc5"], "main")
                    self.assertEqual(refs["ethos"], "main")


if __name__ == "__main__":
    unittest.main()
