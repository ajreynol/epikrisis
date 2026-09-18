"""Commit tracking must survive checkout changes and fail on missing evidence."""
import argparse
import contextlib
import importlib.machinery
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
loader = importlib.machinery.SourceFileLoader("epikrisis", str(ROOT / "bin/epikrisis"))
spec = importlib.util.spec_from_loader(loader.name, loader)
epikrisis = importlib.util.module_from_spec(spec)
loader.exec_module(epikrisis)


class PinTracking(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.checkouts = self.root / "checkouts"
        self.checkouts.mkdir()
        self.here = self.root / "analyzer"
        (self.here / "subjects").mkdir(parents=True)
        (self.here / "questions.md").write_text("Questions registered before pin.\n")
        self.patch = patch.object(epikrisis, "HERE", str(self.here))
        self.patch.start()
        self.addCleanup(self.patch.stop)
        self.tips = {}
        for name in ("member", "cvc5", "ethos"):
            repo = self.checkouts / name
            repo.mkdir()
            self.git(repo, "init", "-b", "main")
            self.git(repo, "config", "user.name", "Test")
            self.git(repo, "config", "user.email", "test@example.invalid")
            self.git(repo, "commit", "--allow-empty", "-m", "main commit")
            self.tips[name] = self.git(repo, "rev-parse", "HEAD")
            self.git(repo, "checkout", "-b", "topic")
            self.git(repo, "commit", "--allow-empty", "-m", "unrelated branch")
        self.subject = {
            "subject": "fixture", "kind": "ecosystem",
            "sources": [{"id": "member", "origin": "https://example.org/member"}],
            "tracked_sources": [{"id": n, "origin": f"https://example.org/{n}",
                                 "ref": "main"} for n in ("cvc5", "ethos")],
        }
        (self.here / "subjects/fixture.json").write_text(json.dumps(self.subject))
        self.args = argparse.Namespace(subject="fixture", date="2026-09-18",
                                       frm=str(self.checkouts))
        self.manifest = self.here / "runs/fixture/2026-09-18/corpus.json"

    def git(self, repo, *args):
        env = dict(os.environ, GIT_AUTHOR_DATE="2026-08-01T00:00:00Z",
                   GIT_COMMITTER_DATE="2026-09-01T00:00:00Z")
        return subprocess.run(["git", "-C", str(repo), *args], check=True,
                              capture_output=True, text=True, env=env).stdout.strip()

    def pin(self):
        with contextlib.redirect_stdout(io.StringIO()):
            epikrisis.cmd_pin(self.args)
        return json.loads(self.manifest.read_text())

    def test_pin_counts_named_main_with_a_different_branch_checked_out(self):
        corpus = self.pin()
        self.assertEqual([s["id"] for s in corpus["sources"]], ["member"])
        self.assertEqual(corpus["sources"][0]["commits"], 2)
        for src in corpus["commit_tracking"]["sources"]:
            self.assertEqual(src["ref"], "main")
            self.assertEqual(src["commit"], self.tips[src["id"]])
            self.assertEqual(src["commits"], 1)
            self.assertEqual(src["first_commit"], "2026-09-01")
            self.assertEqual(src["last_commit"], "2026-09-01")

    def test_missing_checkout_preserves_existing_manifest(self):
        self.pin()
        before = self.manifest.read_bytes()
        (self.checkouts / "ethos").rename(self.root / "elsewhere")
        with self.assertRaisesRegex(SystemExit, "not a git checkout"):
            self.pin()
        self.assertEqual(self.manifest.read_bytes(), before)

    def test_missing_main_fails_without_using_head(self):
        self.git(self.checkouts / "ethos", "tag", "main")
        self.git(self.checkouts / "ethos", "branch", "-D", "main")
        with self.assertRaises(SystemExit):
            self.pin()
        self.assertFalse(self.manifest.exists())

    def test_shallow_history_fails_without_partial_manifest(self):
        source = self.root / "ethos-source"
        (self.checkouts / "ethos").rename(source)
        self.git(self.root, "clone", "--depth=1", "--branch=main", source.as_uri(),
                 str(self.checkouts / "ethos"))
        with self.assertRaisesRegex(SystemExit, "shallow clone"):
            self.pin()
        self.assertFalse(self.manifest.exists())

    def test_merged_history_counts_every_reachable_commit(self):
        repo = self.checkouts / "ethos"
        self.git(repo, "checkout", "main")
        self.git(repo, "commit", "--allow-empty", "-m", "main advances")
        self.git(repo, "merge", "--no-ff", "topic", "-m", "merge")
        self.git(repo, "checkout", "topic")
        sources = self.pin()["commit_tracking"]["sources"]
        self.assertEqual(next(s for s in sources if s["id"] == "ethos")["commits"], 4)


class TrackingCoverage(unittest.TestCase):
    def test_every_ecosystem_subject_requires_both_main_branches(self):
        for path in (ROOT / "subjects").glob("eunoia-ecosystem*.json"):
            with self.subTest(subject=path.name):
                sources = json.loads(path.read_text())["tracked_sources"]
                self.assertEqual([(s["id"], s["ref"]) for s in sources],
                                 [("cvc5", "main"), ("ethos", "main")])

    def test_generator_keeps_tracking_even_outside_the_member_set(self):
        register = {n: {"status": status, "url": f"https://example.org/{n}"}
                    for n, status in (("kanon", "president"), ("cvc5", "foundation"),
                                      ("ethos", "candidate"))}
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "register.json"
            path.write_text(json.dumps(register))
            result = subprocess.run(["python3", str(ROOT / "subjects/derive_sources.py"),
                                     str(path), "future"], check=True,
                                    capture_output=True, text=True)
        subject = json.loads(result.stdout)
        self.assertEqual([s["id"] for s in subject["sources"]], ["kanon"])
        self.assertEqual([(s["id"], s["ref"]) for s in subject["tracked_sources"]],
                         [("cvc5", "main"), ("ethos", "main")])

    def test_latest_figure_context_matches_main_branch_manifest(self):
        rd = ROOT / "runs/eunoia-ecosystem-s2/2026-09-18"
        corpus = json.loads((rd / "corpus.json").read_text())
        sources = {s["id"]: s for s in corpus["commit_tracking"]["sources"]}
        figures = json.loads((rd / "figures.json").read_text())
        for row in figures["context"]["repositories"]:
            src = sources[row["id"]]
            self.assertEqual((row["ref"], row["pin"], row["all_time"]),
                             (src["ref"], src["commit"], src["commits"]))


if __name__ == "__main__":
    unittest.main()
