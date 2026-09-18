# Documentation

**The reports are published at
[ajreynol.github.io/epikrisis](https://ajreynol.github.io/epikrisis/)**, built by
CI from the runs in this tree. This page is about the documents; the site is the
output. Neither describes the other, and
[`../history_analyzer/runs/README.md`](../history_analyzer/runs/README.md) says
how a run gets from one to the other.

Every document in this repository, and what each one is for. The charter,
[`../README.md`](../README.md), is the entry point and assumes it has been read.

**Documents sit with the thing they describe.** This directory holds what is
true of the repository; a tool's own documents live under that tool, so a
reader who has found the tool has found its documentation and a tool that is
retired takes its pages with it. The repository has one analyzer today, so the
split looks like overhead — it is here because the alternative, one flat
directory serving an unknown number of tools, is the arrangement that cannot be
introduced later without moving every page and every link at once.

| document | what it is for |
| --- | --- |
| [`discussion.md`](discussion.md) | Correspondence with other repositories: what is open, to whom, and what settles it. Not a findings ledger. |

## The GitHub history analyzer

[`../history_analyzer/`](../history_analyzer/) holds the tool, what it reads and
what it has produced: the program in `bin/`, subject configuration in
`subjects/`, the pre-registered [`questions.md`](../history_analyzer/questions.md),
the calibration priors and their results in `calibration/`, and the committed
evidence and reports in `runs/`.

| document | what it is for |
| --- | --- |
| [`../history_analyzer/docs/design.md`](../history_analyzer/docs/design.md) | The pipeline: six stages, the boundary between the four that are programs and the one that is judgement, what each stage produces, what is committed, the command surface, and the hazards that produce plausible wrong answers rather than errors. Goal 1. |
| [`../history_analyzer/docs/events.md`](../history_analyzer/docs/events.md) | The detector catalogue: what counts as a candidate event, how each is found, how each is known to be wrong, what was deliberately refused as a detector, and the rule for adding one. Goal 2. |
| [`../history_analyzer/docs/judgement.md`](../history_analyzer/docs/judgement.md) | Everything standing in for the fact that the second half cannot be checked by a program: pre-registration, the shape of an assessment, required negative findings, the dropped-candidate record, the stricter rules when the subject is ours, and what calibration can and cannot establish. Goal 3. |
| [`../history_analyzer/docs/notes.md`](../history_analyzer/docs/notes.md) | Open defects in that tool: what is wrong with each, how to re-derive it, and what would fix it. |

The standard each had to meet: a document displaces a question or an hour of
somebody's reading, because writing another page is the comfortable alternative
to doing the work. The three above the line are held to it as the analyzer's
account of itself; `notes.md` is held to it separately, and is what is left of a
page that failed it — written before any request had arrived, and cut to the
open defects it was carrying, each of which does displace something by being a
finding somebody would otherwise have to make twice.

**This index names documents the checker cannot see.** It reads `docs/` and
requires every markdown file there to appear here; the four rows above are
outside its reach, so a document added under `history_analyzer/docs/` and not
listed here is drift that nothing will report. Said here rather than left for a
reader to discover.

Nothing in either place describes a run. Evidence and reports live beside the
subject that produced them, under
[`../history_analyzer/runs/`](../history_analyzer/runs/): documentation says how
the tool works, and a report is the tool's output.
[`runs/README.md`](../history_analyzer/runs/README.md) indexes them — which runs
carry a report, a case study or a note, and which are evidence only. It is not
listed in the table above because it describes runs rather than the tool, which
is the same line this section draws.
