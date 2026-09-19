import importlib.machinery
import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
loader = importlib.machinery.SourceFileLoader("shared_site", str(ROOT / "bin/site"))
spec = importlib.util.spec_from_loader(loader.name, loader)
site = importlib.util.module_from_spec(spec)
loader.exec_module(site)


class SharedSite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls.temp.cleanup)
        cls.out = Path(cls.temp.name) / "site"
        site.build(cls.out)

    def test_homepage_has_two_analyses_and_both_tables(self):
        home = (self.out / "index.html").read_text()
        self.assertIn('href="history.html"', home)
        self.assertIn('href="loc/index.html"', home)
        self.assertIn('id="commit-overview"', home)
        self.assertIn('class="loc-counts"', home)
        self.assertIn("History analysis", home)
        self.assertIn("LOC analysis", home)

    def test_loc_counts_and_pins_reach_homepage_and_dedicated_report(self):
        home = (self.out / "index.html").read_text()
        paths = list((ROOT / "loc_analyzer/runs").glob("*/*/loc.json"))
        latest = max(paths, key=lambda p: (
            json.loads((p.parent / "corpus.json").read_text())["recorded_at"],
            p.parent.parent.name, p.parent.name))
        for path in paths:
            data = json.loads(path.read_text())
            report = self.out / "loc" / data["subject"] / data["run"] / "index.html"
            page = report.read_text()
            for src in data["sources"]:
                for text in (src["id"], src["commit"], f'{src["implementation"]["lines"]:,}',
                             f'{src["documentation"]["lines"]:,}'):
                    self.assertIn(text, page)
                    if path == latest:
                        self.assertIn(text, home)
            for name in ("corpus.json", "loc.json", "files.jsonl", "report.md"):
                self.assertEqual((report.parent / name).read_bytes(), (path.parent / name).read_bytes())

    def test_all_local_links_resolve_across_both_analyses(self):
        for path in self.out.rglob("*.html"):
            for target in re.findall(r'(?:href|src|srcset)="([^"]+)"', path.read_text()):
                if target.startswith(("http", "mailto", "#")):
                    continue
                self.assertTrue((path.parent / target.split("#")[0]).exists(), f"{path}: {target}")

    def test_language_breakdowns_are_linked_and_reconcile_with_snapshot_counts(self):
        home = (self.out / "index.html").read_text()
        index = (self.out / "loc/index.html").read_text()
        self.assertRegex(home, r'href="loc/[^\"]+/languages.html"')
        self.assertRegex(index, r'href="[^\"]+/languages.html"')
        for path in (self.out / "loc").glob("*/*/languages.json"):
            data = json.loads(path.read_text())
            counts = json.loads((path.parent / "loc.json").read_text())
            page = (path.parent / "languages.html").read_text()
            summary = (path.parent / "index.html").read_text()
            self.assertIn('href="languages.html"', summary)
            self.assertIn('href="languages.json"', page)
            self.assertIn("C/C++ headers", page)
            self.assertEqual(data["totals"]["total_lines"], counts["totals"]["total_lines"])
            for src, expected in zip(data["sources"], counts["sources"]):
                self.assertEqual(src["commit"], expected["commit"])
                self.assertEqual(sum(g["lines"] for g in src["languages"]), expected["total_lines"])
                self.assertEqual(sum(g["implementation_lines"] for g in src["languages"]),
                                 expected["implementation"]["lines"])
                self.assertEqual(sum(g["documentation_lines"] for g in src["languages"]),
                                 expected["documentation"]["lines"])
                self.assertNotIn("JSON / JSONL", [g["language"] for g in src["languages"]])
                self.assertIn(f'id="repo-{src["id"]}"', page)
                self.assertIn(f'href="#repo-{src["id"]}"', page)
                for group in src["languages"]:
                    self.assertIn(f'{group["lines"]:,}', page)
            # The CLI and public download must describe the same analysis.
            import subprocess
            raw = subprocess.check_output(["python3", str(ROOT / "loc_analyzer/bin/loc"), "languages",
                                           data["subject"], "--run", data["run"]], text=True)
            self.assertEqual(json.loads(raw), data)

    def test_public_reports_use_policy_counts_and_current_denominators(self):
        for path in [self.out / "index.html", self.out / "loc/index.html",
                     *self.out.glob("loc/*/*/index.html")]:
            page = path.read_text()
            self.assertIn("JSON/JSONL", page)
            self.assertNotIn("documentation (.md)", page)
            for name in ("aisthesis", "eschaton"):
                self.assertRegex(page, rf'>{name}</a>.*?<td>0</td>')
        for path in self.out.glob("loc/*/*/languages.html"):
            page = path.read_text()
            self.assertIn("% of implementation", page)
            self.assertNotIn("non-Markdown", page)
            self.assertNotIn("<th>JSON / JSONL</th>", page)

    def test_build_cannot_replace_analyzers_or_repository(self):
        for path in (ROOT, ROOT / "loc_analyzer", ROOT / "history_analyzer", ROOT.parent):
            with self.assertRaisesRegex(ValueError, "ignored site/"):
                site.build(path)


if __name__ == "__main__":
    unittest.main()
