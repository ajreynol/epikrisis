# Open defects in this tool

Findings about this tool that are not yet fixed, kept here so the same one is
not rediscovered from scratch. Each says how to re-derive it. Nothing here
describes a run, and nothing reads this file.

It was cut down from a document addressed to the ecosystem's president on
2026-09-14. That document was written before any request had arrived, it
displaced no question by its own index entry's admission, and it had already
begun going stale against another repository's laws. These four findings are
what was worth keeping; they were true before the office existed and would
survive it being abolished.

## A source list narrower than the claim it supports

`ai-attribution` emits one candidate across five trees and 1,019 commits of
whole history:

```text
anoieu  2026-08-30  {"claude": 3}
```

The census entry beside it says *all three in this repository*, and **that is
wrong**. `ethos` carries an agent trailer in the same window and **32 across its
history, first on 2024-01-24** — so the count is four, and a tree concluded to
record no agent authorship has been recording it for two years, inside the
entry's own table.

**This tool missed it too**, and that is the defect rather than the arithmetic:
`ethos` is not among the subject's five sources while the census counts six. **A
source list narrower than a claim's scope** produces a confident wrong answer
rather than an error, which is the failure mode the design is supposed to be
built against. Evidence:
[`../runs/eunoia-ecosystem/2026-09-02-census/note.md`](../runs/eunoia-ecosystem/2026-09-02-census/note.md).

## `governance` decides what governs from a compiled-in filename list

Eight commits on 2026-09-02 created `docs/history.md` and `docs/laws.md` in
anoieu, 609 lines of churn, and **no detector emitted anything for either** —
because neither filename is on the list compiled into the tool. Re-derive by
running `events` at `runs/anoieu/2026-09-02-presidency/` and searching the paths.

This is the coverage defect the project published about itself, landing on two
of the most consequential documents in the family. The repair it named —
**declare what governs in the subject file** — is still unbuilt.

## CI run history is outside the corpus, permanently

Run history is platform data; the corpus is git history on disk, network imports
are zero by budget, and the scope was narrowed to git histories on 2026-09-01.
So figures like *171 CI runs, 37 green, 22%, a longest red streak of 112* are
**not derivable here and never will be**. Asked for a build colour, this tool
answers *cannot establish that* — a result, not a miss.

Worth saying out loud because a rule elsewhere reads *epikrisis analyses GitHub,
as a service*, which is true of history and false of the run log. **Who can
produce run-history figures is unanswered.**

## The delta has been void on both subjects it has run on

Each time on a word collision. A third void is **the expected outcome, not a
risk**, and it should be said in advance rather than discovered in a report.

## `budget` is in breach, in two places

1511 lines of tool against a published limit of 1500, crossed in the last commit
to touch the tool, and 1687 lines of prose against the 1511 that limit allows.
No CI job covers either. The rule is that the first move is to delete a detector
or move a judgement into the report, and that raising a limit is a person's
decision recorded as one. **Nothing should be added while the tool is in breach
of the limit it published** — least of all by a tool whose whole offer is that
its own numbers can be checked.
