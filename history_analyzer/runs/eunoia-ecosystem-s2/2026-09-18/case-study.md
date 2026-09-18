# Stretch 2 — a stress test of the history analyzer

> [!IMPORTANT]
> **This is a self-assessment.** The run it describes carries `"self": true` — the
> subject is a family of trees that contains this tool. Under
> [`judgement.md`](../../../docs/judgement.md) its conclusions **are never cited
> outward**: not as evidence that these practices work, not in a vision document,
> not in a README. What may travel outward is the method, never the findings.

| | |
| --- | --- |
| **Run** | `eunoia-ecosystem-s2` / `2026-09-18` |
| **Corpus** | 10 sources, 1,355 commits, 2026-03-03 → 2026-09-18 |
| **Target** | Stretch 2, kanon's term, opened 2026-09-15 16:15:45 −05:00 |
| **Stage 6** | `check` ok — 11 assessments, 43 ids cited, 554 candidates accounted for |

**Contents** — [The census](#the-census) · [What the stress test broke](#what-the-stress-test-broke) · [Five things worth measuring next](#five-things-worth-measuring-next) · [Advice](#advice-which-is-why-this-is-not-a-report)

**What this file is.** A stress test of the analyzer, written up beside the run
that produced it. [`report.md`](report.md) is the report and is held to
[`../../../docs/judgement.md`](../../../docs/judgement.md); this is not, and the
difference is the last section. The defects found here are recorded as defects in
[`../../../docs/notes.md`](../../../docs/notes.md), which is the page that carries
them; they are summarised rather than restated.

**Occasion.** The census accepted in `D4` had never been run at the register's
full size, and the term it was accepted for — Stretch 2, kanon's — had opened
three days earlier. The run was built to be hard on purpose: ten sources instead
of the five and seven the existing subjects read, a corpus twice the size of any
previous run, a labelled run stamp, and a subject whose source list is **derived
from the register rather than hand-written**.

## What was run

`eunoia-ecosystem-s2`, pinned 2026-09-18 at ten checkouts — every repository
`kanon scripts/ecosystem/ecosystem.json` records with `status` of `member` or
`president`. Full pipeline, `pin` through `check`.

```sh
python3 history_analyzer/subjects/derive_sources.py \
    <checkouts>/kanon/scripts/ecosystem/ecosystem.json eunoia-ecosystem-s2 \
  > history_analyzer/subjects/eunoia-ecosystem-s2.json
python3 history_analyzer/bin/epikrisis pin    eunoia-ecosystem-s2 --from <checkouts> --date 2026-09-18
python3 history_analyzer/bin/epikrisis events eunoia-ecosystem-s2 --from <checkouts> --run  2026-09-18
python3 history_analyzer/bin/epikrisis record eunoia-ecosystem-s2 --from <checkouts> --run  2026-09-18
python3 history_analyzer/bin/epikrisis delta  eunoia-ecosystem-s2 --run 2026-09-18
python3 history_analyzer/bin/epikrisis check  eunoia-ecosystem-s2 --run 2026-09-18
```

**1,355 commits, 554 candidates, 169 claims, 20 seconds.** `check` reports 11
assessments, 43 ids cited, 554 candidates all accounted for.

## The census

The figure `D4` accepted. **The whole-history column is derived and is
`corpus.json`. The Stretch 2 column is hand-read and is not a product of this
pipeline**, because no stage takes a window; it is `git rev-list --count --since`
at the same commits `corpus.json` pins. Stretch 2 opened at kanon `7eb9973`,
2026-09-15 16:15:45 −05:00.

> [!NOTE]
> **The charts below are derived, not drawn.** `figures` renders them from this
> run's own `corpus.json` and from [`figures.json`](figures.json), which declares
> the hand-read panel together with the command that produces it. Re-running it
> after a re-pin redraws them or fails; it cannot quietly disagree with the
> evidence. Blue is derived, ochre is hand-read, hatched is a zero rather than a
> short bar.
>
> ```sh
> python3 history_analyzer/bin/figures history_analyzer/runs/eunoia-ecosystem-s2/2026-09-18
> ```

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="census-dark.svg">
  <img alt="Commits per repository across ten Eunoia members, two panels sharing a row order. Whole history: logos 711, anoieu 261, kanon 104, eudaimonia 97, dokimasia 52, koine 41, tachyon 37, epikrisis 32, eschaton 11, aisthesis 9 — 1,355 total. Stretch 2: kanon 85, koine 28, eudaimonia 26, tachyon 25, anoieu 20, eschaton 11, dokimasia 9, epikrisis 9, aisthesis 8, and logos 0 — 221 total." src="census-light.svg">
</picture>

| repository | whole history | Stretch 2 *(hand-read)* | share of stretch |
| --- | ---: | ---: | ---: |
| logos | 711 | **0** | 0% |
| anoieu | 261 | 20 | 9% |
| kanon | 104 | **85** | **38%** |
| eudaimonia | 97 | 26 | 12% |
| dokimasia | 52 | 9 | 4% |
| koine | 41 | 28 | 13% |
| tachyon | 37 | 25 | 11% |
| epikrisis | 32 | 9 | 4% |
| eschaton | 11 | 11 | 5% |
| aisthesis | 9 | 8 | 4% |
| **total** | **1,355** | **221** | |

**Commits believed AI-generated: not measurable, by anybody, including this
tool.** Disclosure is measurable and is reported beside the count every time it
is asked for: five commits of 1,355 have ever carried an agent trailer, and
**zero of the 221 in Stretch 2 do**, in any of the ten trees — nor in `ethos`,
which is outside this corpus and has 22 in its own history. A trailer is opt-in,
so the floor is zero and there is no ceiling.

## What the stress test broke

Nine findings, six of them new. Each is written up with its re-derivation in
[`../../../docs/notes.md`](../../../docs/notes.md).

| finding | new? | why it matters |
| --- | --- | --- |
| **No window, so the census is a hand count** | new | the duty accepted in `D4` is per-tool commits *for a stretch*; what the pipeline produces is per-tool commits for all time |
| **A stale source list costs 4× more on a stretch than on a history** | new | the seven-source subject is 4.2% short over whole histories and **19.9% short over Stretch 2**, because the unread trees are the newest |
| **The register's transition history was truncated by the handoff** | new | 29 entries dated one afternoon, three `joined` candidates in a ten-member ecosystem |
| **`governance` reached three of kanon's fourteen documents** | known, worse | `laws.md`, `history.md`, `board.md`, `discussion.md`, `glossary.md`, `protocols.md` all unread |
| **The delta is void a third time, and the void grew** | predicted | 14 matches, all collisions; the count rises with corpus size and reads as progress |
| **Result data counted as prose** | new | `ratio` reported tachyon at 1,098:1 on benchmark gap-sets |
| **Run stamp written into the `pinned` date** | new | `panel` cannot run on six of the twelve runs committed here |
| **`--date` honoured only by `pin`; "newest run" is lexicographic** | new | a stage writes into a different run and says nothing |
| **Seven trees stopped at once, and no claim accounts for it** | new | the largest *derived, not declared* finding in the run |

**What held.** Two runs over the same corpus produced byte-identical events.
`selftest` fires all six of its conditions. Stage 6 refused the report until all
554 candidates were cited or dropped with a reason. Stdlib only, no network, 20
seconds. **The parts that are supposed to be deterministic are**, and that is the
half of this tool worth keeping.

## Five things worth measuring next

Ideas, not commitments. Each is derivable from git alone and answers a question
somebody here has already asked in prose.

1. **A window, and a stretch as a first-class object.** One `--since`/`--until`
   on `pin`, plus a stanza in the subject naming the opening commit. Every
   existing measure — `ratio`, `panel`, `recent`, `ai-attribution` — becomes
   stretch-scoped for free, and the census stops being a hand count.
2. **Derive every source list from the register.** This subject was generated
   rather than typed. Making that the only way a subject exists removes the
   19.9% error above by construction instead of by remembering.
3. **Follow the register across repositories.** Its `joined` field already names
   the repository *and* commit that held the policy at each join, precisely
   because the policy moves. Reading it recovers the seven join events the
   handoff truncated.
4. **Retire the matcher, or give claims explicit event ids.** Three runs, three
   voids, collisions rising with corpus size. The catalogue's own rule is that a
   detector whose candidates are always dropped is deleted rather than tuned.
5. **A concentration measure per stretch** — what share of a stretch's commits
   landed in one tree. One line over what `pin` already holds. It reads 38% for
   kanon and 0% for logos this stretch, and it is what makes *the governance
   layer has outgrown what it governs* checkable rather than arguable.

## Advice, which is why this is not a report

`judgement.md` forbids a report from saying what a subject should do next: every
claim there is about what happened, and the tense is the boundary. The following
is advice, it is **a person's to carry or discard**, and it is written down here
rather than left out so that the reason it is not in `report.md` is visible.

**To this repository.** *Ship the window before shipping another census.*
Publishing an all-time count under the name of a stretch count is the failure
this project named for itself. And *stop making the denominator something anybody
has to remember* — the gap was declared honestly in `not_in_corpus` and still
produced a number a fifth short on the window a reader would actually use.

**To kanon, carried by a person and not fired from here.** The Stretch 2 figure
exists and is above. Two things travel with it every time: it is hand-read rather
than pipeline-derived, and the share believed AI-generated **is not measurable by
anybody**. A required field nobody can measure stays a standing admission and
never an invitation to estimate.

**On the docs-flat measure**, which is kanon's own and not ours to grade: its
baseline sits at `anoieu 579aae7` and the documents have since moved to kanon, so
it reads 1.03, 2.19 or 7.83 depending on which tree it is pointed at. Choosing
after seeing the numbers is the fitted-threshold problem in prose form. *(The
reading that follows the documents — anoieu and kanon together — is 2.59 → 2.19,
and `docs/` against Python is 1.83 → 1.63. It is met, and the margin comes from
code growing faster rather than from prose growing less: `docs/` grew 1,066 KiB →
1,107 KiB in absolute terms. Hand-read, and the stretch has not closed.)*

**To a person.** Everything here is marked `self`, and under `judgement.md` none
of it may be cited outward. The calibration question — whether somebody who knows
these trees learns anything here they would not have got faster from `git log` —
is the one test that cannot be self-administered, and it is still the thing that
decides whether this pipeline is worth keeping.
