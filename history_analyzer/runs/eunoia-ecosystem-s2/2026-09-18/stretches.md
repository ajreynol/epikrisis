# Snapshot history — Stretch 1 and Stretch 2

> [!IMPORTANT]
> **This is a self-assessment.** The subject is a family of trees that contains
> this tool. Under [`judgement.md`](../../../docs/judgement.md) its conclusions
> **are never cited outward**: not as evidence that these practices work, not in
> a vision document, not in a README. What may travel outward is the method,
> never the findings.

| | |
| --- | --- |
| **Run** | `eunoia-ecosystem-s2` / `2026-09-18` |
| **Corpus** | the 10 repositories the register holds under the policy, at the commits [`corpus.json`](corpus.json) pins |
| **Stretch 1** | anoieu's term — 2026-08-29 → 2026-09-15 16:15:45 −05:00, eighteen calendar days |
| **Stretch 2** | kanon's term — opened 2026-09-15 16:15:45 −05:00, **unfinished** at the pin |

**Contents** — [What is being compared](#what-is-being-compared) · [The two terms](#the-two-terms) · [Tempo](#tempo-the-difference-is-idleness-not-speed) · [The published window](#the-window-one-stretch-published-and-the-thirteen-days-after-it) · [What the presidency does to a tree](#what-the-presidency-does-to-a-tree) · [What this cannot settle](#what-this-cannot-settle)

## What is being compared

> [!NOTE]
> **Every figure on this page is hand-read, and none of it is a pipeline
> product.** The analyzer has no `--since`: it reports over whole histories up to
> the pin. Each window below was counted with `git rev-list` **at the commit
> `corpus.json` pins for that source**, so it describes the same corpus as every
> other figure in this run. The commands are in
> [`figures.json`](figures.json), which is also what draws the chart — a panel
> whose derivation is not stated is refused by the renderer.

**The boundaries are the subjects' own, not this tool's.** Stretch 1 is dated by
anoieu's `history.md`: *2026-08-29 through 2026-09-15 — eighteen calendar days
inclusive, ended with the manual handoff to kanon.* Stretch 2 opens at kanon
`7eb9973`, the commit in which the register first reads `status: president`
against kanon, at 2026-09-15 16:15:45 −05:00. No detector emits either boundary;
both are read by hand, and a stretch boundary being invisible to this catalogue
is a defect the subject declared before this run existed.

**The numbering is anoieu's.** It was renamed on 2026-09-02 to line up with the
epoch machinery, and the two governing documents disagreed about it for a while.
*Stretch 1* here means the term anoieu's own record calls Stretch 1.

## The two terms

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="stretches-dark.svg">
  <img alt="Commits per repository across three windows, all panels sharing a row order. Stretch 1, the whole eighteen-day term: anoieu 241, eudaimonia 71, dokimasia 43, epikrisis 23, kanon 20, logos 15, koine 13, tachyon 12, aisthesis 1, eschaton 0 — 439 total. Stretch 1 as its own record counts it, a five-day window: anoieu 217, eudaimonia 70, dokimasia 43, epikrisis 20, kanon 14, logos 13, koine 13, and zero for tachyon, eschaton and aisthesis — 390 total. Stretch 2: kanon 85, koine 28, eudaimonia 26, tachyon 25, anoieu 20, eschaton 11, dokimasia 9, epikrisis 9, aisthesis 8, logos 0 — 221 total." src="stretches-light.svg">
</picture>

| repository | whole history | **Stretch 1** *(18 days)* | Stretch 1, as published *(5 days)* | **Stretch 2** *(4 days, open)* |
| --- | ---: | ---: | ---: | ---: |
| logos | 711 | 15 | 13 | **0** |
| anoieu | 261 | **241** | 217 | 20 |
| kanon | 104 | 20 | 14 | **85** |
| eudaimonia | 97 | 71 | 70 | 26 |
| dokimasia | 52 | 43 | 43 | 9 |
| koine | 41 | 13 | 13 | 28 |
| tachyon | 37 | 12 | 0 | 25 |
| epikrisis | 32 | 23 | 20 | 9 |
| eschaton | 11 | 0 | 0 | 11 |
| aisthesis | 9 | 1 | 0 | 8 |
| **total** | **1,355** | **439** | **390** | **221** |

<div class="stats">
<div class="stat h"><b>439</b><span>commits in Stretch 1, across eighteen calendar days</span><i>hand-read</i></div>
<div class="stat h"><b>221</b><span>commits in Stretch 2, across four — and it is not finished</span><i>hand-read</i></div>
<div class="stat h"><b>11</b><span>of Stretch 1&rsquo;s eighteen days carried no commit anywhere</span><i>hand-read</i></div>
<div class="stat h"><b>49</b><span>commits of Stretch 1 fall outside the window its own record publishes</span><i>hand-read</i></div>
</div>

## Tempo: the difference is idleness, not speed

| | Stretch 1 | Stretch 2 |
| --- | ---: | ---: |
| calendar days | 18 | 4 *(open)* |
| days with a commit anywhere | **7** | **4** |
| days with none | **11** | 0 |
| commits | 439 | 221 |
| per calendar day | 24.4 | 55.2 |
| **per active day** | **62.7** | **55.2** |

**Per working day the two terms are almost the same, and the averages are not.**
Stretch 1 looks less than half as busy as Stretch 2 until the idle days come out
of the denominator, at which point 62.7 against 55.2 is a difference of no
consequence. **What separates the terms is that Stretch 1 was idle on eleven of
its eighteen days** — the work happened on 2026-08-29 through 09-02, then
nothing until 09-14.

**That gap is the ecosystem-wide stop this run's report treats as its largest
derived finding**, and it belongs to Stretch 1 rather than sitting between the
terms: seven repositories went quiet within a day of each other and resumed
within two, inside a term that was running throughout. A reader comparing the
two rates without the active-day column would conclude the new president more
than doubled the ecosystem's pace. **Nothing in this evidence supports that.**

## The window one stretch published, and the thirteen days after it

Anoieu's `history.md` carries a section headed **The commit census, this
stretch** reading *331 commits across seven repositories, 2026-08-29 to
2026-09-02.* **The window is dated in the same sentence**, which is the honest
way to publish a partial figure, and it is five of the term's eighteen days.

**What has never been published is the other thirteen.** Over the ten members
this run reads, the five-day window holds **390 commits** and the whole term
holds **439** — so the published window covers **28% of the term's days and 89%
of its commits**, and **49 commits have sat outside anybody's record.** The
figure is not misleading about volume. It is a census named for a stretch,
taken before two-thirds of the stretch had happened, and never revisited.

> [!NOTE]
> **The denominators differ and the totals are not comparable.** Anoieu counted
> seven repositories including `ethos` and `cvc5`, which are not members and are
> not in this corpus; this run counts the ten the register holds under the
> policy, three of which did not exist for most of the window. `331` and `390`
> are measurements of different sets, not a disagreement.

**One figure in that census understates its own window, for a reason worth
recording.** It reports **186** commits for anoieu; the same window at this run's
pin holds **217**. The census pinned anoieu at `f2f5c8e`, **09:25:07 on
2026-09-02** — the last day it counted — and **31 further commits landed that
afternoon**. The census pin is an ancestor of this one, so nothing was rewritten:
a census taken mid-morning on its own closing day misses the rest of the day.

## What the presidency does to a tree

| | president | its own tree's share of its own term |
| --- | --- | ---: |
| Stretch 1 | anoieu | **241 of 439 — 55%** |
| Stretch 2 | kanon | **85 of 221 — 38%** |

**In both terms the president's own repository is the busiest tree in the
ecosystem**, by a wide margin and without either tree being where the calculus
lives. The pattern holds across a change of president, a change of repository and
a change of what the office was for, which is as close to a structural finding as
two observations can get — and two observations is what it is.

**The tree the ecosystem exists to serve went the other way.** logos holds 711 of
the 1,355 commits in this corpus — 52.5% of everything — and contributed 15 to
Stretch 1 and **none at all** to Stretch 2.

**The ecosystem grew under the second term, not the first.** eschaton, aisthesis
and tachyon hold 13 commits across the whole of Stretch 1 and **44 of Stretch 2's
221**, a fifth of it. Two of the three did not exist when the published census
was taken.

## What this cannot settle

**Stretch 2 has not ended.** Every figure for it is four days of an unfinished
term, three of them full. It is not a result and nothing here should be read as
one.

**Stretch 0 is not on this page.** Anoieu's record places it before the ecosystem
existed and counts it in another unit entirely — just under twenty thousand
commits of work this arrangement is built on top of. Nothing in this corpus
reaches it.

**Commits are not work.** Every column counts landings. A repository can be
worked on for a week and land one commit, or land forty in an afternoon that
undo each other — this run's `reversal` detector emits 192 candidates and none of
them is subtracted anywhere above.

**A stretch boundary is invisible to every detector in the catalogue**, so both
of the dates this page is organised around are hand-read. The subject said so
before this run existed, and it is still true.

**`ethos` is outside the corpus** — a candidate rather than a member, and
somebody else's tree — while being inside anoieu's published census and inside
every sentence anybody writes about *the ecosystem*.

**Issue trackers, pull requests and discussion threads are outside the corpus**,
for every source, by design, and that is where the coordination behind an
eleven-day idle stretch would be if it is anywhere.
