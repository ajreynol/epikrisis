# Two presidencies, in commits

The **Eunoia ecosystem** is a group of repositories built around one proof
calculus. One of them holds an office called the *presidency* for a stretch of
time, sets the direction of the shared work, and hands it on. **Two stretches
have now run.** This page is what the git histories say about them — how much
was done, where, and when — at a single pinned moment, **2026-09-18**.

| | |
| --- | --- |
| **Stretch 1** | anoieu's term · 2026-08-29 → 2026-09-15 16:15:45 −05:00 · eighteen days |
| **Stretch 2** | kanon's term · opened 2026-09-15 16:15:45 −05:00 · **still running** |
| **Counted** | the ten repositories the ecosystem's register holds under its policy |

<div class="stats">
<div class="stat h"><b>439</b><span>commits in Stretch 1, across eighteen calendar days</span><i>Stretch 1</i></div>
<div class="stat h"><b>221</b><span>commits in Stretch 2 so far, across four</span><i>Stretch 2</i></div>
<div class="stat h"><b>11</b><span>of Stretch 1&rsquo;s eighteen days carried no commit anywhere</span><i>the finding below</i></div>
<div class="stat h"><b>49</b><span>commits of Stretch 1 fall outside the window its own record publishes</span><i>never reported</i></div>
</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="stretches-dark.svg">
  <img alt="Commits per repository across three windows, all panels sharing a row order. Stretch 1, the whole eighteen-day term: anoieu 241, eudaimonia 71, dokimasia 43, epikrisis 23, kanon 20, logos 15, koine 13, tachyon 12, aisthesis 1, eschaton 0 — 439 total. Stretch 1 as its own record counts it, a five-day window: anoieu 217, eudaimonia 70, dokimasia 43, epikrisis 20, kanon 14, logos 13, koine 13, and zero for tachyon, eschaton and aisthesis — 390 total. Stretch 2: kanon 85, koine 28, eudaimonia 26, tachyon 25, anoieu 20, eschaton 11, dokimasia 9, epikrisis 9, aisthesis 8, logos 0 — 221 total." src="stretches-light.svg">
</picture>

| repository | what it is | whole history | **Stretch 1** | **Stretch 2** |
| --- | --- | ---: | ---: | ---: |
| logos | the Lean development, and the calculus itself | 711 | 15 | **0** |
| anoieu | static analyzer, fuzzer, policy checker · *president in Stretch 1* | 261 | **241** | 20 |
| kanon | the ecosystem's policy, laws and register · *president in Stretch 2* | 104 | 20 | **85** |
| eudaimonia | the calculus template | 97 | 71 | 26 |
| dokimasia | finds gaps in cvc5's proof production | 52 | 43 | 9 |
| koine | shared tooling and the bug database | 41 | 13 | 28 |
| tachyon | searches for cvc5 performance improvements | 37 | 12 | 25 |
| epikrisis | audits these histories · *this tool* | 32 | 23 | 9 |
| eschaton | compares better-founded solver designs | 11 | 0 | 11 |
| aisthesis | writing about how this ecosystem develops | 9 | 1 | 8 |
| **total** | | **1,355** | **439** | **221** |

## Stretch 1 was idle for eleven of its eighteen days

| | Stretch 1 | Stretch 2 |
| --- | ---: | ---: |
| calendar days | 18 | 4 *(and counting)* |
| days with a commit anywhere | **7** | **4** |
| days with none | **11** | 0 |
| commits | 439 | 221 |
| per calendar day | 24.4 | 55.2 |
| **per active day** | **62.7** | **55.2** |

**Stretch 2 looks more than twice as busy as Stretch 1, and it is not.** Take the
idle days out of the denominator and the two terms run at the same pace — 62.7
commits per working day against 55.2, a difference of no consequence. What
separates them is that **Stretch 1 stopped**: work ran from 2026-08-29 to 09-02,
then nothing at all until 09-14.

**Seven repositories went quiet within a day of each other and resumed within
two**, in the middle of a term that was running throughout. Independent projects
do not do that, and nothing in the ecosystem's own written record accounts for
the gap. Anybody comparing the two terms on their headline rates would conclude
the second president doubled the pace of the ecosystem. **The evidence does not
support that.**

## Forty-nine commits nobody has published

Anoieu's term record carries a section headed *the commit census, this stretch*,
covering **2026-08-29 to 2026-09-02** — and it dates that window in the same
sentence, which is the honest way to publish a partial count.

**It is five of the term's eighteen days.** Across the ten repositories counted
here, that window holds **390** commits and the whole term holds **439**. So the
published census covers **28% of the term's days and 89% of its commits**, and
**forty-nine commits have never appeared in anybody's record.** This page is the
first place the full-term figure has been put.

## The president's own tree is always the busiest

| | president | its own tree's share of its own term |
| --- | --- | ---: |
| Stretch 1 | anoieu | **241 of 439 — 55%** |
| Stretch 2 | kanon | **85 of 221 — 38%** |

**In both terms, the repository holding the office was the most active tree in
the ecosystem** — by a wide margin, and in neither case is it where the calculus
lives. The pattern survives a change of president, of repository, and of what the
office was for. It is two observations, and it is two observations of the same
thing.

## The tree all of this serves has stopped

**logos holds 711 of the 1,355 commits here — 52.5% of everything ever committed
across these repositories.** It contributed 15 commits to Stretch 1 and **none at
all** to Stretch 2; its last commit landed four hours and fifty-four minutes
before the second term opened.

Meanwhile the ecosystem grew. **eschaton, aisthesis and tachyon** hold 13 commits
across the whole of Stretch 1 and **44 of Stretch 2's 221** — a fifth of it. Two
of the three did not exist when the published census was taken.

## Where these numbers come from

**Every count is a `git rev-list` over a named window, taken at commits recorded
in advance**, so anybody with the checkouts can reproduce them exactly. The pins,
the windows and the commands are in
[`figures.json`](figures.json) and [`corpus.json`](corpus.json), and the chart
above is drawn from those files rather than typed.

**The dates are the subjects' own.** Stretch 1 is dated by anoieu's own term
record. Stretch 2 opens at kanon `7eb9973`, the commit in which the ecosystem's
register first records `status: president` against kanon.

**The windows are read by hand**, because this analyzer cannot do it. It reports
over whole histories up to a pin and takes no date range; that limitation is
[recorded as a defect](https://github.com/ajreynol/epikrisis/blob/main/history_analyzer/docs/notes.md).

## What this cannot settle

> [!IMPORTANT]
> **This is a self-assessment, and its conclusions do not travel.** Epikrisis is
> one of the ten repositories it is counting here. Under its own
> [report requirements](https://github.com/ajreynol/epikrisis/blob/main/history_analyzer/docs/judgement.md)
> nothing on this page may be cited as evidence that these practices work —
> a family grading itself with its own instrument produces something useful to
> the family and worth little to anybody else.

**Stretch 2 has not ended.** Every figure for it is four days of an unfinished
term. It is not a result.

**Commits are not work.** Every column counts landings. A repository can be
worked on for a week and land one commit, or land forty in an afternoon that
undo each other.

**Two trees are missing from the counts.** `ethos`, which holds the proof checker
and the compiler, is somebody else's repository and is outside this corpus while
being inside anoieu's published census. `cvc5`, which all of this exists to
serve, is outside it too.

**Issue trackers, pull requests and discussion threads are not read**, for any
repository, by design — and that is where the explanation for an eleven-day idle
stretch would be, if it is written down anywhere.

---

**Going deeper.** [The full report for this run](report.md) answers eight
pre-registered questions against the same evidence.
[The case study](case-study.md) is about the instrument rather than the
ecosystem: what broke when this analysis was run, and what it cost.
[Every run](../../README.md) lists the committed evidence behind all of it.
