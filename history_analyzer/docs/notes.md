# Open defects in this tool

Findings about this tool that are not yet fixed, kept here so the same one is
not rediscovered from scratch. Each says how to re-derive it. Nothing here
describes a run, and nothing reads this file. A finding that is fixed leaves
this page; what the fix was belongs in the commit that made it.

## A source list narrower than the claim it supports

`ai-attribution` emitted one candidate across the whole of what that run could
see, and the ecosystem census it bears on counts one repository more than the
subject reads. **`ethos` is not among the sources**, and it does disclose: at
`6e70e0a7`, read 2026-09-17, **22 of its 2,410 commits carry a trailer naming an
agent family, first on 2026-05-11.** So a figure derived over the ecosystem was
derived over a narrower set than the claim it was compared with.

**A source list narrower than a claim's scope** produces a confident wrong
answer rather than an error, which is the failure mode the design is supposed to
be built against. Evidence:
[`../runs/eunoia-ecosystem/2026-09-02-census/note.md`](../runs/eunoia-ecosystem/2026-09-02-census/note.md).

**Half of this is now smaller and half of it is not.** On 2026-09-17 the
ecosystem subjects gained `kanon` and `epikrisis`, so they read seven of the ten
repositories the register records as members. `aisthesis`, `eschaton` and
`tachyon` are still unread, and `ethos` — a candidate rather than a member, and
somebody else's tree — is still outside the corpus while still being inside
every claim anybody makes about *the ecosystem*. **The gap is declared in each
subject's `not_in_corpus` and that is not a fix**; a declared narrowness still
produces a number a reader will take for the whole.

**And the same defect bit this page.** The `ethos` figure above first appeared
here and in the census note as *32, first on 2024-01-24*, which was every
co-author trailer rather than every agent one. Re-derive with the detector's own
test — the trailer's **name** field against the family list — rather than by
grepping for the trailer.

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

**1519 lines of tool against a published limit of 1500**, re-derived with
`python3 history_analyzer/bin/epikrisis budget` on 2026-09-17. The prose half is not in breach;
that command prints both numbers and is the only place either should be read
from, since a figure copied into prose is one more thing to go stale.

**The rule's own first move does not apply here, and that is now measured.** It
says to delete a detector whose candidates are always dropped. Across the two
runs that have a report, every implemented detector has at least one candidate
cited or rested on — the thinnest are `governance` at 10 of 28 and `relation` at
6 of 15 in `runs/eunoia-ecosystem/2026-09-01/`, and none is at zero. There is no
dead detector to remove, and there is no unused code: every module-level name in
the tool is referenced.

**Eight of the nineteen lines were added on 2026-09-17**, guarding the inventory
detector against reading a register that has moved out of the tree it is pinned
in — a defect of the same family as the first finding on this page, and one that
was live. The alternative was to leave a silent wrong answer in place to protect
a line count, which is the trade this page exists to refuse in the other
direction.

**Raising the limit is a person's decision and is not taken here.** No CI job
covers the budget; `epikrisis selftest` proves the counter can fail, and
`epikrisis budget` exits non-zero today, which is why adding it to CI would
report the breach by turning the build red rather than by stating it.
