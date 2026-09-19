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


class Languages(unittest.TestCase):
    def test_file_types_headers_case_and_extensionless_files(self):
        cases = {"src/code.py": "Python", "code.PY": "Python", "code.pyi": "Python",
                 "code.cpp": "C++", "code.C": "C++", "code.c": "C", "code.H": "C++",
                 "code.h": "C/C++ headers", "code.hpp": "C++", "Proof.lean": "Lean",
                 "README.MD": "Markdown", ".md": "Markdown", "CMakeLists.txt": "CMake",
                 "build/Makefile": "Make", "code.cpp.in": "C++", "input.smt2": "SMT-LIB",
                 "data.jsonl": "JSON / JSONL", "bin/loc": "Other text", "code.unknown": "Other text"}
        for path, expected in cases.items():
            with self.subTest(path=path):
                self.assertEqual(loc.language(path), expected)

    def test_denominators_weighting_skipped_files_and_empty_repositories(self):
        sources = [{"id": name, "commit": name * 40, "ref": "main", "origin": "https://example.org/" + name}
                   for name in ("a", "b", "empty")]
        corpus = {"subject": "sample", "run": "test", "files_digest": "digest", "sources": sources,
                  "rules": loc.RULES}
        rows = [{"source": source, "path": path, "category": category, "lines": lines, "object": "blob"}
                for source, path, category, lines in [
                    ("a", "code.py", "implementation", 30), ("a", "README.md", "documentation", 10),
                    ("b", "code.cpp", "implementation", 60), ("b", "empty.py", "implementation", 0)]]
        rows += [{"source": "a", "path": "binary.py", "category": "binary"},
                 {"source": "b", "path": "symlink.lean", "category": "symlink"}]
        data = loc.language_summary(corpus, rows)
        groups = {g["language"]: g for g in data["totals"]["languages"]}
        self.assertEqual(data["totals"]["total_lines"], 100)
        self.assertEqual(data["totals"]["implementation_lines"], 90)
        self.assertEqual(groups["Python"]["percent_total"], 30)
        self.assertAlmostEqual(groups["Python"]["percent_implementation"], 100 / 3, places=5)
        self.assertIsNone(groups["Markdown"]["percent_implementation"])
        self.assertEqual(groups["Python"]["files"], 2)
        self.assertEqual(data["sources"][0]["languages"][0]["percent_total"], 75)
        self.assertEqual(data["sources"][2]["languages"], [])
        self.assertEqual(data["sources"][2]["total_lines"], 0)
        self.assertEqual(groups["Python"]["largest_files"][0]["source"], "a")

    def test_zero_line_files_have_no_percentage_denominator(self):
        corpus = {"subject": "sample", "run": "test", "files_digest": "digest", "sources": [{"id": "a"}],
                  "rules": loc.RULES}
        rows = [{"source": "a", "path": "empty.md", "category": "documentation", "lines": 0, "object": "blob"}]
        group = loc.language_summary(corpus, rows)["totals"]["languages"][0]
        self.assertEqual(group["files"], 1)
        self.assertIsNone(group["percent_total"])
        self.assertIsNone(group["percent_implementation"])

    def test_language_share_uses_only_implementation_in_a_mixed_group(self):
        corpus = {"subject": "sample", "run": "test", "files_digest": "digest", "rules": loc.RULES,
                  "sources": [{"id": "a"}, {"id": "docs-only"}]}
        rows = [{"source": source, "path": path, "category": category, "lines": lines, "object": "blob"}
                for source, path, category, lines in [
                    ("a", "code.py", "implementation", 30),
                    ("a", "code.cpp", "implementation", 70),
                    ("a", "docs/example.py", "documentation", 300),
                    ("docs-only", "docs/example.py", "documentation", 10)]]
        rows.append({"source": "a", "path": "data.json", "category": "ignored", "reason": "json"})
        data = loc.language_summary(corpus, rows)
        groups = {g["language"]: g for g in data["totals"]["languages"]}
        self.assertEqual(data["totals"]["total_lines"], 410)
        self.assertEqual(groups["Python"]["lines"], 340)
        self.assertEqual(groups["Python"]["implementation_lines"], 30)
        self.assertEqual(groups["Python"]["documentation_lines"], 310)
        self.assertEqual(groups["Python"]["percent_implementation"], 30)
        self.assertEqual(sum(g["percent_implementation"] or 0 for g in groups.values()), 100)
        self.assertIsNone(data["sources"][1]["languages"][0]["percent_implementation"])
        self.assertNotIn("JSON / JSONL", groups)


class Classification(unittest.TestCase):
    def test_policy_precedence_and_source_formats(self):
        cases = {
            "docs/code.py": "documentation", "tools/widget/docs/demo.cpp": "documentation",
            "feature/docs/template.py.in": "documentation", "docs/page.html": "documentation",
            "prompts/review": "documentation", "README.MD": "documentation",
            "README.minisat": "documentation", "LICENSE": "documentation",
            "licenses/gpl-3.0.txt": "documentation",
            "src/prop/minisat/CVC4-README": "documentation", "THANKS": "documentation",
            "manual.rst": "documentation", "paper.tex": "documentation",
            "config.JSON": "ignored", "docs/results.jsonl": "ignored",
            "docs/config.json.in": "ignored", "tools/widget/docs/data.JSONL": "ignored",
            ".github/workflows/ci.yml": "ignored", ".github/scripts/check.py": "ignored",
            ".github/README.md": "ignored", "tools/widget/.gitignore": "ignored",
            "data.csv": "ignored", "data.txt": "ignored", "config.toml": "ignored",
            "something.unknown": "ignored", "tests/expected": "ignored",
            "source.py": "implementation", "tests/test.py": "implementation",
            "test.smt2": "implementation", "test.sy": "implementation",
            "proof.plf": "implementation", "test.eo": "implementation",
            "proof.lean": "implementation", "CMakeLists.txt": "implementation",
            "build/Makefile": "implementation", "Dockerfile": "implementation",
            "src/code.cpp.in": "implementation", "cmake/rules.cmake.template": "implementation",
            "src/theory/arith/rewrites": "implementation",
            "src/theory/bv/rewrites-simplification": "implementation",
            "other/rewrites": "ignored", "docs/src/theory/arith/rewrites": "documentation",
            "docs_extra/code.py": "implementation", "src/mydocs/code.py": "implementation",
        }
        for path, expected in cases.items():
            with self.subTest(path=path):
                self.assertEqual(loc.classify(path)[0], expected)
        self.assertEqual(loc.language("src/theory/arith/rewrites"), "Rewrite rules")

    def test_shebangs_require_a_known_interpreter_and_do_not_override_paths(self):
        cases = {b"#!/usr/bin/env python3\n": "Python", b"#!/usr/bin/python3.12 -u\n": "Python",
                 b"#!/bin/bash\n": "Shell", b"#!/usr/bin/env -S python3 -u\n": "Python",
                 b"#!/usr/bin/env FLAG=yes node\n": "JavaScript",
                 b"#!/usr/bin/env -u OLD ruby\n": "Ruby", b"#!/usr/bin/perl\n": "Perl",
                 b"# notes\n": None, b"#!unknown\n": None, b"#!\n": None,
                 b"#!/usr/bin/env\n": None, b"#!/usr/bin/env 'broken\n": None}
        for data, expected in cases.items():
            with self.subTest(data=data):
                self.assertEqual(loc.script_language(data), expected)
        self.assertEqual(loc.classify("bin/loc", "Python"), ("implementation", None))
        self.assertEqual(loc.language("bin/loc", "Python"), "Python")
        self.assertEqual(loc.classify("docs/loc", "Python"), ("documentation", None))
        self.assertEqual(loc.classify("data.json", "Python"), ("ignored", "json"))


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
                           "vendor/code.py": b"pass\n", "vendor2/code.py": b"pass\n"}.items():
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
        self.assertEqual(src["implementation"], {"files": 3, "lines": 5})
        self.assertEqual(src["documentation"], {"files": 2, "lines": 3})
        self.assertEqual(src["skipped"], dict(binary=2, symlink=1, submodule=1, excluded=0, ignored=2))
        self.assertEqual(src["tracked_entries"], 11)
        self.assertEqual(loc.check_run(self.rd, self.checkouts), (corpus, counts))

    def test_language_view_uses_the_validated_evidence(self):
        self.run_analysis()
        data = loc.languages_for_run(self.rd)
        groups = {g["language"]: g for g in data["totals"]["languages"]}
        self.assertEqual(groups["Python"]["lines"], 5)
        self.assertEqual(groups["Markdown"]["lines"], 3)
        self.assertEqual(data["sources"][0]["commit"], self.sha)
        path = self.rd / "files.jsonl"
        path.write_bytes(path.read_bytes() + b"\n")
        with self.assertRaisesRegex(ValueError, "digest"):
            loc.languages_for_run(self.rd)

    def test_exclusions_are_path_boundaries_and_are_recorded(self):
        self.subject["exclude"] = ["vendor/"]
        self.config.write_text(json.dumps(self.subject))
        _, counts = self.run_analysis()
        self.assertEqual(counts["sources"][0]["implementation"]["lines"], 4)
        self.assertEqual(counts["sources"][0]["skipped"]["excluded"], 1)

    def test_tree_classification_keeps_docs_out_of_implementation(self):
        files = {"docs/example.py": b"print(1)\n", "tools/child/docs/page.rst": b"Title\n",
                 "docs/results.json": b"{}\n", ".github/workflows/check.yml": b"name: check\n",
                 ".gitignore": b"scratch/\n", "bin/check": b"#!/usr/bin/env python3\nprint(1)\n",
                 "bin/not-code": b"ordinary prose\n", "prompts/task": b"Read the docs.\n"}
        for path, data in files.items():
            p = self.repo / path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)
        (self.repo / "bin/not-code").chmod(0o755)
        self.git("add", ".")
        self.git("commit", "-m", "policy fixtures")
        corpus, counts = self.run_analysis()
        rows = {r["path"]: r for r in map(json.loads, (self.rd / "files.jsonl").read_text().splitlines())}
        self.assertEqual(counts["sources"][0]["implementation"]["lines"], 7)
        self.assertEqual(counts["sources"][0]["documentation"]["lines"], 6)
        self.assertEqual(rows["docs/results.json"]["category"], "ignored")
        self.assertNotIn("lines", rows["docs/results.json"])
        self.assertEqual(rows["bin/check"]["interpreter"], "Python")
        self.assertEqual(rows["bin/not-code"]["category"], "ignored")
        self.assertEqual(loc.check_run(self.rd, self.checkouts), (corpus, counts))

    def test_documentation_repo_with_ci_and_metadata_has_zero_implementation(self):
        self.subject["exclude"] = ["code.py", "vendor", "vendor2"]
        self.config.write_text(json.dumps(self.subject))
        for path, text in {".github/workflows/anoieu.yml": "name: policy\n", ".gitignore": "scratch/\n"}.items():
            p = self.repo / path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text)
        self.git("add", ".")
        self.git("commit", "-m", "repository setup")
        _, counts = self.run_analysis()
        self.assertEqual(counts["sources"][0]["implementation"], {"files": 0, "lines": 0})

    def test_recount_preserves_pins_even_when_main_advances(self):
        corpus, counts = self.run_analysis()
        (self.repo / "new.py").write_text("print('new')\n")
        self.git("add", "new.py")
        self.git("commit", "-m", "advance main")
        with contextlib.redirect_stdout(io.StringIO()):
            loc.recount_analysis("sample", self.checkouts, "2026-09-18")
        revised, new_counts = loc.check_run(self.rd, self.checkouts)
        self.assertEqual(new_counts, counts)
        self.assertEqual(revised["sources"], corpus["sources"])
        self.assertEqual(revised["recorded_at"], corpus["recorded_at"])
        self.assertEqual(revised["previous_files_digest"], corpus["files_digest"])
        self.assertIn("recounted_at", revised)

    def test_failed_recount_leaves_snapshot_intact(self):
        self.run_analysis()
        before = {p.name: p.read_bytes() for p in self.rd.iterdir()}
        with self.assertRaises(ValueError):
            loc.recount_analysis("sample", self.root / "missing", "2026-09-18")
        self.assertEqual({p.name: p.read_bytes() for p in self.rd.iterdir()}, before)

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

    def test_documentation_repositories_and_ignored_paths_in_published_evidence(self):
        rd = ROOT / "runs/eunoia-ecosystem/2026-09-18"
        _, counts = loc.check_run(rd)
        by_id = {s["id"]: s for s in counts["sources"]}
        for name in ("aisthesis", "eschaton"):
            self.assertEqual(by_id[name]["implementation"], {"files": 0, "lines": 0})
        for row in map(json.loads, (rd / "files.jsonl").read_text().splitlines()):
            if row["category"] == "implementation":
                parts = Path(row["path"]).parts
                self.assertNotIn("docs", parts[:-1])
                self.assertNotIn(".github", parts[:-1])
                self.assertNotIn(Path(row["path"]).suffix.lower(), (".json", ".jsonl"))


if __name__ == "__main__":
    unittest.main()
