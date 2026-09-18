# LOC analyzer

The central repository-size census for Epikrisis. `loc_analyzer` counts lines in
Git trees at recorded commits and publishes a per-repository split between
**implementation** and **documentation (`.md`)**. It runs alongside the
[history analyzer](../history_analyzer/README.md).

Read the [published LOC analysis](https://ajreynol.github.io/epikrisis/loc/) or
browse the [committed snapshots](runs/README.md). The shared
[homepage](https://ajreynol.github.io/epikrisis/) presents both analyses.

## What is counted

This is a deliberately broad count of physical lines, including blank lines and
comments. A final line without a newline counts; an empty file has zero lines.

| Category | Definition |
| --- | --- |
| Documentation | Regular UTF-8 text files ending in `.md`, case-insensitive. |
| Implementation | All other regular UTF-8 text files, including source, tests, configuration, generated files and data. |
| Skipped | Files containing NUL bytes or invalid UTF-8, symlinks, submodules and explicitly excluded paths. |

This is a rough size split, not a language-aware source-code metric. For example,
reStructuredText documentation and test fixtures fall under implementation.
Generated and vendored text is included by default. The per-file evidence makes
that scope inspectable, and each run records any path exclusions. Duplicate
content at different paths counts once for each path.

Only committed files at the recorded pins are read. Dirty files, untracked build
outputs and local configuration do not affect the count. Symlinks and submodules
are recorded but never followed. These numbers measure size, not quality or effort.

## Run a census

Requires Python 3 and Git, with no third-party packages or network access. Run
the commands below from the repository root.

```sh
python3 loc_analyzer/bin/loc subjects
python3 loc_analyzer/bin/loc run eunoia-ecosystem --from /path/to/checkouts --run 2026-09-19
```

Choose an unused run stamp; an existing run is never overwritten. Omit `--run`
when creating a run to use today's date. The stamp labels the snapshot; it does
not select a historical date.

The [ecosystem subject](subjects/eunoia-ecosystem.json) shares the history
census's repository list, including cvc5 and ethos, and pins `main` in each
checkout. Supply directories or symlinks named after the repository IDs under
`--from`. The checked-out branch may differ: `main` means `refs/heads/main`, and
a missing branch fails rather than falling back to `HEAD`. Full history is not
needed for LOC, but the pinned commit and all its tree objects must be available.

Subjects live in [`subjects/`](subjects/). A subject can name its own `sources`
(each with `id`, `origin` and optional `ref`) or use `sources_from` to read the
`sources` and `tracked_sources` of another subject file. That path is relative to
the LOC subject file. `ref` defaults to `main`; `exclude` lists exact paths or
directory prefixes. The resolved repository set, pins, exclusions and counting
rules are frozen in every run.

## Outputs and verification

Each run creates a directory under `loc_analyzer/runs/<subject>/<stamp>/`:

| File | Contents |
| --- | --- |
| `corpus.json` | Commit pins, timestamp, counting rules, exclusions and the per-file evidence digest. |
| `files.jsonl` | One record per tracked path: Git object, category, byte size and line count where applicable. |
| `loc.json` | Per-repository and combined line totals, file counts and skipped-entry counts. |
| `report.md` | A generated table and explanation of the counting method. |

Check that the totals and generated report match the per-file evidence:

```sh
python3 loc_analyzer/bin/loc check eunoia-ecosystem --run 2026-09-18
```

Add `--from /path/to/checkouts` to recount the pinned trees and compare every file
with the stored evidence. This uses the recorded SHAs, even if branches have
advanced. A check without checkouts verifies internal consistency, not the
contents of the original Git trees.

## Publish and maintain

```sh
python3 bin/site site
python3 -m unittest discover -s loc_analyzer/tests
python3 -m unittest discover -s tests
```

The shared builder renders both analyses. Preview `site/index.html` for the
homepage or `site/loc/index.html` for LOC snapshots. It validates the stored LOC
counts before rendering and copies the evidence beside each public report.
Commit the run artifacts; the [Pages workflow](../.github/workflows/pages.yml)
builds and deploys them when they are pushed to `main`.

[`bin/loc`](bin/loc) owns the counting rules and checks;
[`bin/site`](bin/site) renders the LOC pages from those artifacts. Neither
fetches repositories. Re-running the census is an explicit action so that the
published numbers always identify the commits they describe.
