# Epikrisis

Epikrisis provides evidence and analysis for GitHub repositories in the **Eunoia
ecosystem**. Its purpose is to explain how projects evolve: **what happened, what
worked, what went wrong, and where the recorded account differs from the changes
in the tree.**

**The reports are published at
[ajreynol.github.io/epikrisis](https://ajreynol.github.io/epikrisis/)** — the
index, every report, and the evidence each rests on. It is built by CI from what
is committed under
[`history_analyzer/runs/`](history_analyzer/runs/README.md); nothing appears
there that is not in this tree. **Every run is a self-assessment and its
conclusions do not travel** — see [what that means for a reader from
outside](#what-it-has-produced).

Its first tool is a **GitHub history analyzer**. The longer-term ambition is to
provide deeper analyses across Eunoia and develop into the ecosystem's
**“judicial” branch**: examining its work, testing claims against evidence, and
making assessments that others can inspect and contest.

## The GitHub history analyzer

**[`history_analyzer/`](history_analyzer/) is the whole of it** — the tool, what
it reads, and what it has produced. It is a directory rather than a scattering
of top-level ones because this repository intends to carry more than one
analysis, and a second tool arriving into a flat tree is the point at which
every path and every link has to move at once.

| under `history_analyzer/` | what it holds |
| --- | --- |
| `bin/epikrisis` | the program: one Python file, standard library only |
| `bin/figures` | a renderer, and never part of the pipeline: it turns a run's evidence into SVG and decides nothing |
| `bin/site` | the other renderer: it builds the published report site from what is under `runs/`, and refuses any markdown it has not been taught |
| `subjects/` | what may be analysed — the repositories a run reads, and the settings it reads them under |
| `questions.md` | the questions, pre-registered, with their digest pinned into every run |
| `calibration/` | what a reader predicted before the detectors ran, and how that scored |
| `runs/` | the committed evidence and the reports written from it |

The program reads local Git checkouts at pinned commits. It supports individual
repositories and subjects spanning several repositories, with configuration in
[`history_analyzer/subjects/`](history_analyzer/subjects/).

| Tooling | What it provides |
| --- | --- |
| `pin` | A manifest of the source repositories, commit pins, thresholds, and questions for a run. |
| `events` | Candidate events such as releases, rewrites, file moves, governance changes, and ecosystem membership transitions, with supporting commits and paths. |
| `record` and `delta` | Claims extracted from the repository's own documents, compared with detected events to identify matches, omissions, and disagreements. |
| `prompt` and `check` | Evidence assembled for a separately written report, plus checks on its citations, assessments, and treatment of unused candidates. |
| `ratio`, `panel`, and `recent` | Code/prose counts, activity by path prefix, and recent work grouped into sessions. |
| `detectors` and `budget` | The detector catalogue with known failure modes, and checks on implementation size and dependencies. |
| `subjects` and `selftest` | What is defined and what each subject reads, and a proof that `check` and `budget` can fail rather than only pass. |

**The command surface is defined in [the pipeline design](history_analyzer/docs/design.md), and
that page is the ground truth.** The table above and the tool's own `--help` are
copies of it. **Nothing compares them**, so a command added to one and not the
others is drift that has not been reported yet; that is stated here rather than
left for a reader to discover.

## What it has produced

**The reports are published at
[ajreynol.github.io/epikrisis](https://ajreynol.github.io/epikrisis/)**, built by
CI from what is committed under `runs/` — the index derived from each run's
`corpus.json`, each page that run's own markdown. Nothing is written there that
is not in this tree.

**[`history_analyzer/runs/`](history_analyzer/runs/) holds twelve runs and four of
them carry prose; [its index](history_analyzer/runs/README.md) says which, and is
the page to open when you know a thing was written and not where.** The rest are
evidence — a pin and its candidates, with nothing anybody wrote.

| | |
| --- | --- |
| **[Stretch 2 — case study](history_analyzer/runs/eunoia-ecosystem-s2/2026-09-18/case-study.md)** | A stress test of the analyzer at the register's full size: the **per-repository commit census** for kanon's term, nine defects the run exposed, five things worth measuring next, and advice. **Not a report** — [`judgement.md`](history_analyzer/docs/judgement.md) forbids a report from saying what a subject should do next, which is why the advice lives beside one instead of inside it. Renders on GitHub, charts included. |
| **[Snapshot history — Stretch 1 and Stretch 2](history_analyzer/runs/eunoia-ecosystem-s2/2026-09-18/stretches.md)** | The two presidential terms compared at one pin — 439 commits against 221, and the eleven days of the first that carried none. |
| [Stretch 2 — report](history_analyzer/runs/eunoia-ecosystem-s2/2026-09-18/report.md) | The report for the same run. Ten sources, 1,355 commits, eleven assessments, `check` accepted. |
| [anoieu — report](history_analyzer/runs/anoieu/2026-09-01/report.md) | The first report this tool produced, with its [evidence](history_analyzer/runs/anoieu/2026-09-01/). The worked example. |
| [ecosystem — report](history_analyzer/runs/eunoia-ecosystem/2026-09-01/report.md) | The first ecosystem report. Five sources, 889 commits. |
| [census — note](history_analyzer/runs/eunoia-ecosystem/2026-09-02-census/note.md) | Stages 1–2 only, published because the evidence bore on a figure already in somebody's record. |

For an example of the historical account this tooling is intended to support,
see **[anoieu's `history.md`](https://github.com/ajreynol/anoieu/blob/main/docs/history.md)**,
which records repository development and ecosystem events.

**Every run in this repository is a self-assessment, and its conclusions do not
travel.** The subject of each is a family of trees that contains this tool, so
each run is marked `self` and [`judgement.md`](history_analyzer/docs/judgement.md)
forbids citing what it concluded outward — not as evidence that these practices
work, not in a vision document, not in a README, including this one. A family
grading itself with its own instrument produces something useful to the family
and worthless to anybody else.

**So if you have arrived from outside the Eunoia ecosystem, the method is the
part addressed to you** — [the pipeline design](history_analyzer/docs/design.md),
[the detector catalogue](history_analyzer/docs/events.md) with its failure modes,
[the report requirements](history_analyzer/docs/judgement.md), and
[the open defects](history_analyzer/docs/notes.md). The runs above are worth
reading as worked examples of that method and **not as findings you should
believe**: what they assess is us, by us. A finding about a repository outside
this family is that repository's, is carried by a person rather than published
here, and is asked for first.

The analyzer is experimental. Its completed assessments cover anoieu and the
Eunoia ecosystem and are marked as self-assessments. Known limitations include
**no windowing** -- every run reports over whole histories up to the pin, so a
figure scoped to a stretch or any other period is not a product of this pipeline
-- missed governance events, and unreliable event-to-claim matching; see
[open defects](history_analyzer/docs/notes.md) before relying on the results.

## Using it

Requires Python 3 and Git, with no third-party Python dependencies. The analyzer
reads existing local checkouts and makes no network requests.

```sh
python3 history_analyzer/bin/epikrisis subjects
python3 history_analyzer/bin/epikrisis detectors
```

Before starting a run, review the subject configuration and write the questions
in [`history_analyzer/questions.md`](history_analyzer/questions.md). For the supplied `anoieu` subject, place a
full checkout at `/path/to/checkouts/anoieu`, then run from this repository:

```sh
python3 history_analyzer/bin/epikrisis pin anoieu --from /path/to/checkouts
python3 history_analyzer/bin/epikrisis events anoieu --from /path/to/checkouts
python3 history_analyzer/bin/epikrisis record anoieu --from /path/to/checkouts
python3 history_analyzer/bin/epikrisis delta anoieu
python3 history_analyzer/bin/epikrisis prompt anoieu
```

`pin` records the checkout's current commit and creates a dated directory under
`history_analyzer/runs/anoieu/`. Subsequent commands use the newest run unless given
`--run <stamp>`. The prompt prints evidence and questions for a writer; the
analyzer does not generate the narrative. Write the report and assessment files
using the [report requirements](history_analyzer/docs/judgement.md), then validate them with
`python3 history_analyzer/bin/epikrisis check anoieu --run <stamp>`.

An existing report can be checked directly:

```sh
python3 history_analyzer/bin/epikrisis check anoieu --run 2026-09-01
```

## Toward Eunoia's judicial branch

The future purpose is **deeper analysis of GitHub repositories across Eunoia**.
History analysis supplies the foundation: a record of changes that can be
reconstructed and compared with what projects say about themselves. From there,
Epikrisis can develop more substantial reviews of how the ecosystem's projects,
decisions, and governing practices hold up against their own stated aims.

That work should make it possible to:

- Follow consequential changes across repositories, including shifts in
  membership, responsibilities, and shared tooling.
- Examine whether declared decisions and commitments are reflected in the
  artifacts, and identify gaps that deserve closer review.
- Produce retrospective assessments with explicit evidence, limits, and grounds
  for correction, including closer analysis of commits and their messages.

The likely long-term role is judicial: scrutiny, accountability, and reasoned
assessment within Eunoia. This is a direction for the project to develop, with
its responsibilities and authority to be defined as the ecosystem takes shape.
The immediate work is to improve detector coverage, event grouping, and the
reliability of comparisons between the declared and derived records.

## How an analysis earns trust

**Evidence and judgement are separate outputs.** The pipeline derives evidence
from pinned histories; a writer selects the significant events and makes the
assessment. Mechanical checks require citations, falsifiers, negative findings,
and an account of dropped candidates. Readers can rebuild the evidence and
challenge the conclusions.

The current corpus is public Git history and the files published in it. GitHub
issues, pull-request discussions, and CI run logs are outside the implemented
analyzer's scope. Analysis concerns artifacts and their evolution; it does not
grade contributors. Assessments of other projects remain internal until their
publication is agreed, and ecosystem self-assessments are not evidence that
Eunoia's practices work elsewhere.

The implementation should stay small and inspectable as the questions grow.
The practical test is whether an analysis tells someone who knows a repository
something useful that they did not already know.

## Documentation

Start with the [documentation index](docs/README.md), which names everything in
the repository. The analyzer's own documents sit with the analyzer, under
[`history_analyzer/docs/`](history_analyzer/docs/):

- [Pipeline design](history_analyzer/docs/design.md): evidence, outputs, and the boundary with judgement.
- [Detector catalogue](history_analyzer/docs/events.md): event definitions, thresholds, and failure modes.
- [Report requirements](history_analyzer/docs/judgement.md): assessments, falsifiers, and self-assessment rules.
- [Open defects](history_analyzer/docs/notes.md): current limitations and how to reproduce them.
- [Runs](history_analyzer/runs/README.md): the index of every run — which carry a report, a case study or a note, and which are evidence only.

## The name

*Epikrisis* (Greek **ἐπίκρισις**) is a judgement made retrospectively. The medical
term *epicrisis* describes a case's course of events followed by an assessment:
events first, judgement grounded in them.[^origins]

[^origins]: Started on 2026-09-01 inside [eudaimonia's workflow launcher](https://github.com/ajreynol/eudaimonia/tree/main/tools/workflow-launcher), whose comparison of recorded claims with observed changes informed the approach. Epikrisis became a separate repository on 2026-09-14, retaining its Git history.

## How this repository is maintained

This repository is part of the **Eunoia ecosystem** and follows its
[shared repository policy](https://github.com/ajreynol/kanon/blob/main/docs/policy.md),
kept by kanon.

**Written by AI agents, under light human supervision.** A human directs the
work, decides what this repository is for, and reads what is published here;
nobody vets the internal design, and nothing here is carried into another project
without review.
