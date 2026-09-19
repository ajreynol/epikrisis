# LOC analyzer

The central repository-size census for Epikrisis. `loc_analyzer` counts lines in
Git trees at recorded commits and publishes a per-repository split between
**implementation** and **documentation**. It runs alongside the
[history analyzer](../history_analyzer/README.md).

Read the [published LOC analysis](https://ajreynol.github.io/epikrisis/loc/) or
browse the [committed snapshots](runs/README.md). The shared
[homepage](https://ajreynol.github.io/epikrisis/) presents both analyses.
Each snapshot also links to a detailed language/file-type breakdown, with
Python, C++, Lean and other percentages for the combined corpus and each repository.

## What is counted

This counts physical lines, including blank lines and
comments. A final line without a newline counts; an empty file has zero lines.

| Category | Definition |
| --- | --- |
| Documentation | UTF-8 text under any `docs/`, `prompts/` or `licenses/` directory, including nested tools; recognized documentation formats and README/license-style filenames elsewhere. |
| Implementation | Recognized source and build files, including tests and proof-language inputs; extensionless scripts with recognized shebangs. |
| Ignored | JSON/JSONL anywhere, `.github/` contents, repository metadata such as `.gitignore`, and other data/configuration or unrecognized text. |
| Skipped | Files containing NUL bytes or invalid UTF-8, symlinks, submodules and explicitly excluded paths. |

The default assumes the [shared repository layout](https://github.com/ajreynol/kanon/blob/main/docs/policy.md).
JSON and metadata exclusions take precedence over documentation paths. A Python
example under `docs/` is documentation; `docs/results.json` is ignored. These
measurement rules apply uniformly to all repositories in a subject.

Source is recognized by explicit filename, path-pattern and suffix lists,
recorded in each manifest. Extensionless `src/theory/*/rewrites` and
`rewrites-*` definitions count as rewrite-rule source. CMake, Make and Docker
build files count as implementation; YAML,
TOML, CSV, lockfiles and arbitrary plain-text fixtures outside documentation
paths do not. Recognized code and proof inputs under tests still count.
Trailing `.in` and `.template` wrappers are removed before classification.
Extensionless scripts require a recognized Python, shell, Perl, Ruby or Node
shebang; executable permission alone does not make a text file implementation.

Documentation formats include Markdown, reStructuredText, TeX/BibTeX and AsciiDoc.
Generated and vendored source follows the same rules. Ignored files remain in
the evidence with a reason but contribute no lines. Duplicate content at
different paths counts once for each path. This measures physical size, without
parsing code or removing comments.

Only committed files at the recorded pins are read. Dirty files, untracked build
outputs and local configuration do not affect the count. Symlinks and submodules
are recorded but never followed. These numbers measure size, not quality or effort.

## Language percentages

The detailed page groups the same pinned physical-line counts by filename and
extension. It reports file counts, lines, percentages and the five largest files
in each group, linked to the recorded commits. Each group separates implementation
and documentation lines. CMake and Make filenames take
precedence over extensions; `.h` files form a separate **C/C++ headers** group.
`.C` and `.H` mean C++; other extensions ignore case. Template wrappers are
removed, and extensionless scripts use their recorded shebang interpreter.
Documentation without a recognized file type remains **Other text**.

The repository comparison gives Python, C++, Lean, shared C/C++ headers,
SMT-LIB, Eunoia, Java, Shell and Markdown their own columns.
Expand an **Other types** percentage to see the remaining types and their
individual shares of the repository. The table scrolls horizontally on smaller
screens, with repository names kept visible.

Two percentage columns make the denominator explicit:

- **Counted lines:** implementation plus documentation in the repository (or
  combined corpus). Ignored files contribute to neither denominator.
- **Implementation:** the group's implementation lines divided by the size
  report's implementation total. For example, Python examples under `docs/`
  affect Python's counted-line share but not its implementation share.

Combined percentages use summed lines, rather than an average of repository
percentages. A missing denominator or documentation-only group has a dash for
its implementation share. Small nonzero shares
below 0.01% are shown as `<0.01%`; other percentages use two decimal places.

Produce the same JSON used by the public language page, without any checkouts:

```sh
python3 loc_analyzer/bin/loc languages eunoia-ecosystem --run 2026-09-18
```

This first validates the snapshot, then derives language counts from `files.jsonl`.
The output includes the classification rules and their version, evidence digest,
commit pins, per-repository and combined totals, and largest-file evidence.
Language views are regenerated with the current classifier when the site builds;
they are derived views, not changes to the original snapshot artifacts.

## Run a census

Requires Python 3 and Git, with no third-party packages or network access. Run
the commands below from the repository root.

```sh
python3 loc_analyzer/bin/loc subjects
python3 loc_analyzer/bin/loc run eunoia-ecosystem --from /path/to/checkouts --run 2026-09-19
```

Choose an unused run stamp; `run` never overwrites an existing snapshot. Omit `--run`
when creating a run to use today's date. The stamp labels the snapshot; it does
not select a historical date.

The [ecosystem subject](subjects/eunoia-ecosystem.json) shares the history
census's repository list, including cvc5 and ethos, and pins `main` in each
checkout. It also includes the explicitly requested eunoia and paideia projects;
the September 19 snapshot covers fourteen repositories. Supply directories or
symlinks named after the repository IDs under
`--from`. The checked-out branch may differ: `main` means `refs/heads/main`, and
a missing branch fails rather than falling back to `HEAD`. Full history is not
needed for LOC, but the pinned commit and all its tree objects must be available.

Subjects live in [`subjects/`](subjects/). A subject can name its own `sources`
(each with `id`, `origin` and optional `ref`) or use `sources_from` to read the
`sources` and `tracked_sources` of another subject file. That path is relative to
the LOC subject file. `ref` defaults to `main`; `exclude` lists exact paths or
directory prefixes. The resolved repository set, pins, exclusions and counting
rules are recorded in every run.

## Outputs and verification

Each run creates a directory under `loc_analyzer/runs/<subject>/<stamp>/`:

| File | Contents |
| --- | --- |
| `corpus.json` | Commit pins, timestamp, counting rules, exclusions and the per-file evidence digest. |
| `files.jsonl` | One record per tracked path: Git object, category, byte size, counted lines, and interpreter or ignore reason where applicable. |
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

To explicitly update an existing report with the current counting rules while
preserving its commit pins and public URL:

```sh
python3 loc_analyzer/bin/loc recount eunoia-ecosystem --from /path/to/checkouts --run 2026-09-18
```

`recount` reads every pinned tree before replacing the four run artifacts. It
keeps the original snapshot timestamp and records `recounted_at`, the current
rules and the previous evidence digest. It does not resolve branch tips or
change subjects, pins or exclusions. Commit the revised artifacts together with
the classifier; validation requires matching schema and counting rules.

## Publish and maintain

```sh
python3 ecosystem_report/site site
python3 -m unittest discover -s loc_analyzer/tests
python3 -m unittest discover -s tests
```

The [shared builder](../ecosystem_report/site) renders both analyses. Preview
`site/index.html` for the homepage or `site/loc/index.html` for LOC snapshots.
It validates the stored LOC counts before rendering and copies the evidence
beside each public report.
It also generates `languages.html` and downloadable `languages.json` for every
snapshot, with links from the homepage, LOC index and snapshot summary. New runs
receive these pages automatically.
Commit the run artifacts; the [Pages workflow](../.github/workflows/pages.yml)
builds and deploys them when they are pushed to `main`.

[`bin/loc`](bin/loc) owns the counting rules and checks;
[`bin/site`](bin/site) renders the LOC pages from those artifacts. Neither
fetches repositories. Re-running the census is an explicit action so that the
published numbers always identify the commits they describe.
