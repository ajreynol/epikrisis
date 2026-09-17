# Epikrisis

Epikrisis provides evidence and analysis for GitHub repositories in the **Eunoia
ecosystem**. Its purpose is to explain how projects evolve: **what happened, what
worked, what went wrong, and where the recorded account differs from the changes
in the tree.**

Its first tool is a **GitHub history analyzer**. The longer-term ambition is to
provide deeper analyses across Eunoia and develop into the ecosystem's
**“judicial” branch**: examining its work, testing claims against evidence, and
making assessments that others can inspect and contest.

## The GitHub history analyzer

[`bin/epikrisis`](bin/epikrisis) is a Python command-line tool that reads local
Git checkouts at pinned commits. It supports individual repositories and subjects
spanning several repositories, with configuration in [`subjects/`](subjects/).

| Tooling | What it provides |
| --- | --- |
| `pin` | A manifest of the source repositories, commit pins, thresholds, and questions for a run. |
| `events` | Candidate events such as releases, rewrites, file moves, governance changes, and ecosystem membership transitions, with supporting commits and paths. |
| `record` and `delta` | Claims extracted from the repository's own documents, compared with detected events to identify matches, omissions, and disagreements. |
| `prompt` and `check` | Evidence assembled for a separately written report, plus checks on its citations, assessments, and treatment of unused candidates. |
| `ratio`, `panel`, and `recent` | Code/prose counts, activity by path prefix, and recent work grouped into sessions. |
| `detectors` and `budget` | The detector catalogue with known failure modes, and checks on implementation size and dependencies. |
| `subjects` and `selftest` | What is defined and what each subject reads, and a proof that `check` and `budget` can fail rather than only pass. |

**The command surface is defined in [the pipeline design](docs/design.md), and
that page is the ground truth.** The table above and the tool's own `--help` are
copies of it. **Nothing compares them**, so a command added to one and not the
others is drift that has not been reported yet; that is stated here rather than
left for a reader to discover.

For an example of the historical account this tooling is intended to support,
see **[anoieu's `history.md`](https://github.com/ajreynol/anoieu/blob/main/docs/history.md)**,
which records repository development and ecosystem events. For a worked analyzer
output, see the [anoieu report](runs/anoieu/2026-09-01/report.md) and its
[accompanying evidence](runs/anoieu/2026-09-01/).

The analyzer is experimental. Its completed assessments cover anoieu and the
Eunoia ecosystem and are marked as self-assessments. Known limitations include
missed governance events and unreliable event-to-claim matching; see
[open defects](docs/notes.md) before relying on the results.

## Using it

Requires Python 3 and Git, with no third-party Python dependencies. The analyzer
reads existing local checkouts and makes no network requests.

```sh
python3 bin/epikrisis subjects
python3 bin/epikrisis detectors
```

Before starting a run, review the subject configuration and write the questions
in [`questions.md`](questions.md). For the supplied `anoieu` subject, place a
full checkout at `/path/to/checkouts/anoieu`, then run from this repository:

```sh
python3 bin/epikrisis pin anoieu --from /path/to/checkouts
python3 bin/epikrisis events anoieu --from /path/to/checkouts
python3 bin/epikrisis record anoieu --from /path/to/checkouts
python3 bin/epikrisis delta anoieu
python3 bin/epikrisis prompt anoieu
```

`pin` records the checkout's current commit and creates a dated directory under
`runs/anoieu/`. Subsequent commands use the newest run unless given
`--run <stamp>`. The prompt prints evidence and questions for a writer; the
analyzer does not generate the narrative. Write the report and assessment files
using the [report requirements](docs/judgement.md), then validate them with
`python3 bin/epikrisis check anoieu --run <stamp>`.

An existing report can be checked directly:

```sh
python3 bin/epikrisis check anoieu --run 2026-09-01
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

Start with the [documentation index](docs/README.md), or go directly to:

- [Pipeline design](docs/design.md): evidence, outputs, and the boundary with judgement.
- [Detector catalogue](docs/events.md): event definitions, thresholds, and failure modes.
- [Report requirements](docs/judgement.md): assessments, falsifiers, and self-assessment rules.
- [Open defects](docs/notes.md): current limitations and how to reproduce them.
- [Runs](runs/): committed evidence and reports.

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
