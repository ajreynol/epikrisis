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

## The delta has been void on every subject it has run on, and the void grows

Each time on a word collision. A third void was recorded here in advance as **the
expected outcome, not a risk**, and on 2026-09-18 it was the outcome.

**What was not predicted is the direction of the count.** Over ten sources the
matcher reported **14 matched and 8 disagreeing** — its largest join to date,
against 1 and 6 in the five earlier runs — and all fourteen were read
individually and all fourteen are collisions. C0019, a topic titled *we are going
to stop proving our report by re-running our tools*, matched seven candidates
whose only connection to it is a prefix named `tools`; koine-birth-0007 matched
three claims whose titles contain the word *koine*.

**The wrongness scales with the corpus** and it scales upward, so a reader who
does not open `delta.json` sees a match count improving from 1 to 6 to 14. This
family names its directories after the things it writes about, which is the
condition the matcher is least able to survive. Evidence:
[`../runs/eunoia-ecosystem-s2/2026-09-18/`](../runs/eunoia-ecosystem-s2/2026-09-18/).

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

**And the counter reads one file.** `budget_facts` opens `bin/epikrisis` and
nothing else, so any program added anywhere in this tree is unmetered by the
limit it is supposed to be held to. `subjects/derive_sources.py`,
`bin/figures` and `bin/site` are the three such programs and are disclosed here rather than left
for the limit to stop meaning anything quietly. Neither reads a history, runs
`git` or decides anything the pipeline's output depends on — which is the reason
they are allowed to exist and not a reason the counter should keep ignoring
them. The prose half is wider than the code half — it counts
`docs/*.md` and the top-level `questions.md`, and no markdown under `runs/`,
which is correct: evidence is not prose about the tool.

## The run stamp is written into the `pinned` date, and `panel` cannot read it

`cmd_pin` sets `"pinned": stamp`, so one value carries both the date pinned and
the run's directory name. `cmd_panel` then calls `date.fromisoformat` on it and
raises `ValueError` on any labelled stamp. **Six of the twelve runs committed to
this repository carry a non-date `pinned`** — every `-census`, `-status`,
`-proto`, `-presidency`, `-assess` and `2026-09-02b` run — and `panel` cannot be
run on any of them. Re-derive:

```sh
python3 history_analyzer/bin/epikrisis panel eunoia-ecosystem --from <dir> --run 2026-09-02-census
```

The evidence already written is not corrupted by this; the date is recoverable
from each run's directory name and from the pinned commits themselves.

## `--date` is accepted by every stage and honoured only by `pin`

Every subcommand advertises `--date`. Only `pin` reads it. A later stage given
`--date` silently falls through to `run_dir(subject)` with no stamp, which
returns `sorted(os.listdir(...))[-1]` — so `events --date 2026-09-18` wrote its
output into `2026-09-18-stretch2`, a different run, and said nothing. Found
2026-09-18 by doing it.

**This is the same defect that was found and fixed for `--run` on 2026-09-02**,
and the comment recording that fix is directly above the line that still has it
for `--date`: *"`--run` is offered on every stage; honouring it in only some of
them let a pin land in one directory and its events in another, silently."*

## "Newest run" is lexicographic, not chronological

`run_dir` with no stamp returns `sorted(os.listdir(d))[-1]`. For `anoieu` that is
`2026-09-02b`, not the most recent run. Any stage invoked without `--run`
resolves to whichever stamp sorts last in byte order, and labelled stamps sort
after and between dated ones. Re-derive with
`sorted(os.listdir("history_analyzer/runs/anoieu"))`.

## `bucket` counts result data as prose

`PROSE_EXT` contains `.txt`, so `ratio` reported **tachyon at 1,098:1 prose to
tool on 1,805,306 prose lines** in `runs/eunoia-ecosystem-s2/2026-09-18/`. Those
lines are benchmark gap-sets under `tools/heuresis/ledger/data/` — generated
measurement output, and the product of that tree rather than writing about it.
The stretch-wide prose share reads 99% with them in and 69% with them out.

The classifier is declared rather than inferred and its list is published, so
this is predictable from the list. It is here because **no run before this one
contained a tree that ships data**, and the first one that did produced a
confidently wrong number rather than an error — the failure mode this project
names for itself. `prose_is_product` is a per-subject declaration and cannot
express *this path is data*, which is the missing expression.

## The inventory detector's history was truncated by the handoff it should record

`detect_inventory` reads `kanon scripts/ecosystem/ecosystem.json`, which was
**created in that tree on 2026-09-15** by the governance handoff. Its history
before that date is in anoieu, which the detector does not follow across the
repository boundary. The visible result in
`runs/eunoia-ecosystem-s2/2026-09-18/`: 22 revisions read, **29 `listed`
candidates all dated 2026-09-15 carrying `at_inventory_start: true`, and only 3
`joined` candidates in a ten-member ecosystem.** The seven earlier members
appear to have arrived on one afternoon.

The register itself carries the repair: each member's `joined` field names the
repository and commit that held the policy when it joined, precisely because the
policy has moved once and is expected to move again. Nothing reads that field.

## The governance detector reached three of kanon's fourteen documents

Named already on this page as a filename-list defect that landed on two
documents. **It has since landed on a tree.** Across 1,355 commits the detector
emitted 75 candidates over twelve source/path pairs: `policy`, `roles`,
`vision`, `names`, `proposals`, and nothing else. `laws.md`, `history.md`,
`board.md`, `discussion.md`, `glossary.md` and `protocols.md` are unread, in the
repository that holds the ecosystem's governance. Re-derive by grouping the
`governance` rows of `runs/eunoia-ecosystem-s2/2026-09-18/events.jsonl` by path.

## A hand-written source list costs four times more on a stretch than on a history

Measured rather than asserted, at the 2026-09-18 pin. The seven-source subject
reports **1,298 of 1,355 commits, 4.2% short**, over whole histories — which is
the size the `not_in_corpus` declaration implies. Over the Stretch 2 window the
same subject reports **177 of 221, 19.9% short**, because the three unread trees
are the three newest.

**A stale source list under-reports exactly what is new, and the whole-history
view hides it.** `subjects/eunoia-ecosystem-s2.json` is the first subject whose
source list is derived from the register rather than hand-written; it carries
`_source_list_derived` recording the rule (`status` in `member`, `president`)
and is regenerated rather than edited.

## No window: the census that was accepted cannot be produced by this pipeline

`D4` accepted the per-tool commit census. Every stretch-scoped figure in
`runs/eunoia-ecosystem-s2/2026-09-18/report.md` — the census column, the
prose-to-code measure, the disclosure count, the working-summary revision
spacing — is **hand-read with `git` and marked as such**, because no stage takes
a `--since`. The report is a tool-shaped directory around a hand count.

This is not the same defect as `D4`'s second half. That one says a figure is not
measurable by anybody. This one says a figure everybody agrees is measurable is
not measured *here*.
