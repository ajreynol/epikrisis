"""What the site builder must not be allowed to do quietly.

A renderer is dangerous in a repository like this one in a specific way: it
produces a page that reads correctly and is wrong. These tests are aimed at that
-- that nothing is dropped, that no link goes nowhere, and that an unfamiliar
construct stops the build instead of being guessed at.

    python3 -m unittest discover -s history_analyzer/tests
"""
import importlib.machinery
import json
import importlib.util
import os
import re
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
# bin/site carries no .py suffix, so the loader is named rather than guessed.
_p = os.path.join(ROOT, "bin", "site")
spec = importlib.util.spec_from_loader("site", importlib.machinery.SourceFileLoader("site", _p))
site = importlib.util.module_from_spec(spec)
spec.loader.exec_module(site)


def build():
    out = tempfile.mkdtemp()
    site.main.__globals__["sys"].argv = ["site", out]
    site.main()
    return out


class Converter(unittest.TestCase):
    def test_it_refuses_what_it_has_not_been_taught(self):
        for src, why in [("![a](b.png)", "image"),
                         ("text[^1] more", "footnote"),
                         ("~~gone~~", "strikethrough"),
                         ("#### too deep", "deep heading"),
                         ("<table><tr></tr></table>", "raw html")]:
            with self.subTest(why=why):
                with self.assertRaises(site.Unsupported):
                    site.convert(src, "t.md", "s/d")

    def test_a_paragraph_opening_with_a_block_character_still_advances(self):
        # The first version of this looped forever on a line beginning with a
        # code span, which is how most sentences about a command begin here.
        for src in ["`ratio` reported a number.", "`a` and\n`b` and\n`c`."]:
            with self.subTest(src=src):
                self.assertIn("<p>", site.convert(src, "t.md", "s/d"))

    def test_code_spans_are_not_searched_for_markup(self):
        out = site.convert("use `a**b**c` here", "t.md", "s/d")
        self.assertIn("a**b**c", out)
        self.assertNotIn("<strong>", out)

    def test_a_link_to_evidence_leaves_the_site_and_prose_stays_in_it(self):
        self.assertTrue(site.link("figures.json", "s/d").startswith("http"))
        self.assertTrue(site.link("../../../docs/notes.md", "s/d").startswith("http"))
        self.assertEqual(site.link("report.md", "s/d"), "report.html")
        self.assertEqual(site.link("census-light.svg", "s/d"), "census-light.svg")


class Site(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.out = build()

    def test_every_local_link_resolves(self):
        bad = []
        for dirpath, _, files in os.walk(self.out):
            for f in files:
                if not f.endswith(".html"):
                    continue
                p = os.path.join(dirpath, f)
                for t in re.findall(r'(?:href|src|srcset)="([^"]+)"', open(p).read()):
                    if t.startswith(("http", "mailto", "#")):
                        continue
                    if not os.path.exists(os.path.normpath(os.path.join(dirpath, t))):
                        bad.append(f"{os.path.relpath(p, self.out)} -> {t}")
        self.assertEqual(bad, [])

    def test_every_run_with_a_corpus_reaches_the_listing(self):
        # The index is a landing page and names a chosen few; runs.html is the
        # page that must account for all of them.
        listing = open(os.path.join(self.out, "runs.html")).read()
        for r in site.runs():
            self.assertIn(r["stamp"], listing, f"{r['subject']}/{r['stamp']} missing")
            self.assertIn(r["subject"], listing)

    def test_the_index_reaches_every_document_site_json_advertises(self):
        idx = open(os.path.join(self.out, "index.html")).read()
        cfg = json.load(open(os.path.join(site.HERE, "site.json")))
        items = [cfg["highlight"]] + [i for s in cfg["sections"] for i in s["items"]]
        for it in items:
            href = f"{it['subject']}/{it['stamp']}/{it['doc'][:-3]}.html"
            self.assertIn(href, idx)
            self.assertTrue(os.path.exists(os.path.join(self.out, href)))

    def test_nothing_is_dropped_from_a_source_document(self):
        for r in site.runs():
            for f in r["prose"]:
                md = open(os.path.join(r["dir"], f)).read()
                out = open(os.path.join(self.out, r["subject"], r["stamp"],
                                        f[:-3] + ".html")).read()
                fence, heads, cells = False, 0, 0
                for ln in md.split("\n"):
                    if ln.lstrip("> ").startswith("```"):
                        fence = not fence
                        continue
                    if fence:
                        continue
                    if re.match(r"^#{1,3} ", ln):
                        heads += 1
                    # A separator carries dashes; `| | |` is an empty header
                    # row and is a row. Testing only for "no letters" counts
                    # such a header as a separator and under-counts by one.
                    if ln.startswith("|") and not re.match(r"^\|[\s:|-]*-[\s:|-]*\|$", ln):
                        cells += 1
                with self.subTest(doc=f"{r['subject']}/{r['stamp']}/{f}"):
                    self.assertEqual(len(re.findall(r"<h[123] id=", out)), heads)
                    self.assertEqual(len(re.findall(r"<tr>", out)), cells)

    def test_the_self_assessment_marking_is_on_every_page(self):
        for dirpath, _, files in os.walk(self.out):
            for f in files:
                if f.endswith(".html"):
                    with self.subTest(page=f):
                        self.assertIn("self-assessment",
                                      open(os.path.join(dirpath, f)).read())

    def test_it_will_not_write_the_site_into_the_evidence(self):
        site.main.__globals__["sys"].argv = ["site", os.path.join(site.RUNS, "x")]
        with self.assertRaises(SystemExit):
            site.main()


if __name__ == "__main__":
    unittest.main()
