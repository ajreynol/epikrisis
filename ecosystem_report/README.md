# Ecosystem report publisher

[`site`](site) builds the [public reports](https://ajreynol.github.io/epikrisis/)
from the history and LOC analyses. It assembles the shared homepage and invokes
each analyzer's renderer.

Run from the repository root with Python 3:

```sh
python3 ecosystem_report/site site
```

Preview `site/index.html` for the homepage, `site/history.html` for history,
and `site/loc/index.html` for LOC. The generated `site/` directory is ignored by
Git. The builder uses only the Python standard library and needs no network.

The report text, figures and evidence are committed beside their snapshots in
[`history_analyzer/runs/`](../history_analyzer/runs/README.md) and
[`loc_analyzer/runs/`](../loc_analyzer/runs/README.md). Their guides explain
how to produce and validate those inputs. The publisher renders that evidence
and checks the LOC totals before publishing.

The [Pages workflow](../.github/workflows/pages.yml) runs the tests and report
checks, invokes this builder, and uploads `site/` to GitHub Pages on pushes to
`main`. GitHub Pages uses the uploaded artifact; the builder's directory is a
repository layout choice.

The shared publication checks live in [`tests/test_site.py`](../tests/test_site.py):

```sh
python3 -m unittest discover -s tests
```
