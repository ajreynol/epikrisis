# Epikrisis

Epikrisis provides evidence and analysis for repositories in the **Eunoia
ecosystem**: how projects evolve, how their size and composition change, and
where their recorded accounts differ from the work in their Git histories.

**[Read the published analyses](https://ajreynol.github.io/epikrisis/).**

## Analyses

| Analysis | What it shows | Guide |
| --- | --- | --- |
| [History](https://ajreynol.github.io/epikrisis/history.html) | Commit activity, changes over time, and retrospective reports. | [History analyzer](history_analyzer/README.md) |
| [Lines of code](https://ajreynol.github.io/epikrisis/loc/) | Repository size, implementation and documentation, and language percentages. | [LOC analyzer](loc_analyzer/README.md) |

Both analyses include **eunoia and paideia**, alongside the ecosystem's other
repositories and **cvc5 and ethos on `main`**, and identify the commits behind
their results. The language breakdown
includes per-repository comparisons and links to the largest files.

## Reading the results

History reports are **self-assessments** of the ecosystem that contains this
tool. They help us examine our work; their conclusions are not evidence that
these practices work elsewhere. Reports separate evidence from judgement so
readers can inspect the basis for an assessment and challenge it.

LOC reports measure physical lines of source, scripts and documentation,
including comments and tests. JSON, CI metadata and other data files are excluded.
They describe size and composition, not quality or effort. The analyzer guides
explain the methods and their limits.

## Direction

The longer-term ambition is to develop into Eunoia's **judicial branch**:
examining whether projects and decisions live up to their stated aims, testing
claims against evidence, and making assessments open to review and correction.
Its responsibilities and authority remain to be defined as the ecosystem grows.

## Documentation

The [documentation index](docs/README.md) links to the methods, known limitations
and contributor guides. Browse the [history reports](history_analyzer/runs/README.md)
and [LOC snapshots](loc_analyzer/runs/README.md) for the committed results and evidence.
Setup and usage instructions live in the analyzer guides above.
The [ecosystem report publisher](ecosystem_report/README.md) builds their shared
public site.

## The name

*Epikrisis* (Greek **ἐπίκρισις**) means a retrospective judgement: events first,
then an assessment grounded in them.

## How this repository is maintained

This repository is part of the **Eunoia ecosystem** and follows its
[shared repository policy](https://github.com/ajreynol/kanon/blob/main/docs/policy.md),
kept by kanon.

**Written by AI agents, under light human supervision.** A human directs the
work, decides what this repository is for, and reads what is published here;
nobody vets the internal design, and nothing here is carried into another project
without review.
