# GitHub history analyzer

The history analyzer reads local Git repositories at pinned commits, detects
candidate events, and compares them with the repositories' own accounts of what
happened. It produces evidence for a separately written report, then checks the
report's citations, assessments and treatment of unused candidates.

Read the [published reports](https://ajreynol.github.io/epikrisis/) or browse the
[run index](runs/README.md) for the committed evidence. The
[Epikrisis README](../README.md) explains the wider project.

## What is here

| Path | Purpose |
| --- | --- |
| [`bin/epikrisis`](bin/epikrisis) | The analyzer: pin histories, derive evidence, assemble a prompt and check a report. |
| [`bin/figures`](bin/figures) | Render a run's counts as light and dark SVG charts. |
| [`bin/site`](bin/site) | Render history pages for the shared site builder. |
| [`subjects/`](subjects/) | Repository lists, exclusions, detector thresholds and tracked branches. |
| [`questions.md`](questions.md) | Questions registered before a run; their digest is recorded in its manifest. |
| [`calibration/`](calibration/) | Predictions made before detection and comparisons with the resulting evidence. |
| [`runs/`](runs/README.md) | Pinned manifests, derived evidence, reports and figures. |
| [`site.json`](site.json) | Homepage copy and the choice of highlighted run and chart. |
| [`tests/`](tests/) | Checks for commit tracking, site rendering and homepage counts. |

## Run an analysis

Requires **Python 3 and Git**, with no third-party Python packages. The analyzer
reads existing full checkouts and makes no network requests. Commands below run
from the repository root, the directory containing `history_analyzer/`.

Inspect the available subjects and detectors:

```sh
python3 history_analyzer/bin/epikrisis subjects
python3 history_analyzer/bin/epikrisis detectors
```

Review the chosen [subject configuration](subjects/) and write the questions in
[`questions.md`](questions.md) before pinning. Place each repository under the
checkout directory using its source ID as the directory name; symlinks to full
checkouts also work. For the `anoieu` subject, that means a checkout at
`/path/to/checkouts/anoieu`.

Choose an unused date for the run stamp. The date names the output directory;
it does not select historical commits. `pin` reads the configured refs, using
`HEAD` when no ref is specified. Reusing a stamp overwrites its manifest.

```sh
checkouts=/path/to/checkouts
run_stamp=2026-09-19  # Example: replace with an unused YYYY-MM-DD date.

python3 history_analyzer/bin/epikrisis pin anoieu --from "$checkouts" --date "$run_stamp"
python3 history_analyzer/bin/epikrisis events anoieu --from "$checkouts" --run "$run_stamp"
python3 history_analyzer/bin/epikrisis record anoieu --from "$checkouts" --run "$run_stamp"
python3 history_analyzer/bin/epikrisis delta anoieu --run "$run_stamp"
python3 history_analyzer/bin/epikrisis prompt anoieu --run "$run_stamp"
```

The output goes to `history_analyzer/runs/anoieu/<run_stamp>/`. Later stages read
the commits in `corpus.json`, even if the checkouts have moved. `prompt` prints
the evidence and questions for a writer. Write `report.md`, `assessments.jsonl`
and the dropped-candidate records in `selection.jsonl` beside that evidence,
following the [report requirements](docs/judgement.md), then validate:

```sh
python3 history_analyzer/bin/epikrisis check anoieu --run "$run_stamp"
```

Use `--date` only for `pin` and explicit `--run` values for subsequent commands.
The current default run selection is lexicographic; labelled stamps can select
an unintended run, and `panel` requires a plain ISO date. These limitations are
documented in [open defects](docs/notes.md).

The additional `ratio`, `panel` and `recent` commands read the same pinned
histories and require both `--from` and, to select a particular run, `--run`.
See the [pipeline design](docs/design.md) for the command reference and artifact
formats.

## Ecosystem runs and commit tracking

The [Stretch 2 subject](subjects/eunoia-ecosystem-s2.json) takes its assessed
source list from the ecosystem register. For a new ecosystem subject,
[`subjects/derive_sources.py`](subjects/derive_sources.py) derives the list from
kanon's `scripts/ecosystem/ecosystem.json`; its usage is documented in the script.

All supplied ecosystem subjects also track **cvc5 and ethos on `main`**. Supply
full checkouts named `cvc5` and `ethos` alongside the assessed repositories.
`pin` resolves `refs/heads/main` regardless of the checked-out branch and writes
full commit IDs and whole-history counts under `commit_tracking` in
`corpus.json`. Missing checkouts, missing refs and shallow histories stop the pin.

The homepage's table, stretch charts and summary totals include both tracked
repositories. Report assessments use the subject's assessed `sources`; their
scope is recorded separately from the supplemental commit counts. Existing
ecosystem runs carry dated amendments with reconstruction cutoffs and pins.

**Stretch counts still require a separate Git count.** The analyzer has no date
window. A run's `figures.json` records window counts and their derivation commands;
tracked window counts must name the same pins and branches as `corpus.json`.
Recompute those counts when advancing the pins. The homepage build rejects
missing tracked counts and mismatched pins.

## Build the reports site

```sh
python3 bin/site site
```

Open `site/index.html` to preview both analyses, `site/history.html` for history,
or `site/runs.html` for the full history listing. The generated `site/` directory
is ignored by Git. The [shared builder](../bin/site) renders
run Markdown, copies report figures and regenerates the homepage charts from
the same evidence as its table and summary totals. It also builds the parallel
[LOC analysis](../loc_analyzer/README.md) under `site/loc/`.

To regenerate the SVG files stored beside a run:

```sh
python3 history_analyzer/bin/figures history_analyzer/runs/eunoia-ecosystem-s2/2026-09-18
```

The [Pages workflow](../.github/workflows/pages.yml) checks the reports and builds
and deploys the site when its watched inputs change on `main`.

## Checks and further reading

```sh
python3 -m unittest discover -s history_analyzer/tests
python3 history_analyzer/bin/epikrisis selftest
python3 history_analyzer/bin/epikrisis check anoieu --run 2026-09-01
python3 history_analyzer/bin/epikrisis budget
```

`budget` currently reports an existing breach of the analyzer's line-count limit;
see [open defects](docs/notes.md). Detector coverage and event-to-claim matching
also have known limitations. GitHub issues, pull-request discussions and CI logs
are outside the analyzer's corpus.

- [Pipeline design](docs/design.md): stages, commands, evidence formats and reproducibility.
- [Detector catalogue](docs/events.md): candidate event types and failure modes.
- [Report requirements](docs/judgement.md): assessments, falsifiers and selection records.
- [Open defects](docs/notes.md): limitations and how to reproduce them.
- [Run index](runs/README.md): reports, case studies, notes and evidence-only runs.

The existing reports are **self-assessments** of the ecosystem containing this
tool. Their conclusions are not evidence that these practices work elsewhere;
the report requirements explain that scope.
