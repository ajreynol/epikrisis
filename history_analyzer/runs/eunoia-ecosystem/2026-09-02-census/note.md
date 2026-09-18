# Note — not a report

> [!NOTE]
> **Commit-tracking amendment, 2026-09-18.** cvc5 `main`: **14,072** commits; ethos `main`: **1,058**. These whole-history counts are reconstructed at `2026-09-02T09:25:07-05:00`, the latest original source-commit time; the original wall-clock pin time was not recorded. Full pins and the reconstruction command are in [`corpus.json`](corpus.json), under `commit_tracking`. The assessments and their totals below retain their original source scope.

**Stages 1–2 only.** No claims were extracted, no delta was computed, no
assessment was written, and `check` has not been run over anything here. This
file exists because the evidence bears on a figure somebody else has already
published, and holding it would be the failure this project named for itself:
*silence is also a way of being wrong.*

**Occasion.** anoieu's `docs/history.md`, the ecosystem's presidency record,
published a commit census for Stretch 0 on 2026-09-02 and wrote beside it:
*this is the figure `laws.md` now requires and epikrisis is asked to produce
... counted by the party it describes, because no epikrisis report exists.*

## What this tool derived

Pin `2026-09-02-census`: five sources, **1,019 commits, 2026-03-03 to
2026-09-02**, whole histories rather than the stretch — this tool has no window
and reports over everything up to the pin, which is the limitation `D4` is
about.

**`ai-attribution` emitted exactly one candidate across all five trees**, and it
is quoted as emitted:

```text
anoieu  2026-08-30  {"claude": 3}
```

No other source discloses an agent co-author at any point in its history, not
merely during the stretch.

That **agrees with the census on the trees it covers** and is stronger than it
in one respect: the census says three, this stretch; this says three, ever.

## What this tool did not derive, and it is the half that matters

**`ethos` is not a source of this subject.** The census counts **six**
repositories; `subjects/eunoia-ecosystem.json` reads **five**. So the sentence
*across the whole ecosystem, three carry a `Co-Authored-By` trailer naming an
agent, all three in this repository* covers a tree this pin cannot see, and the
tool would have missed it for exactly the reason the census would.

**Read by hand with `git log`, and marked as such because no detector in this
catalogue produces it:**

| | |
| --- | --- |
| `ethos`, agent trailers in the census window | **1** — `24d02c47`, 2026-09-01, *Finalize eoc compiler (#236)* |
| `ethos`, agent trailers across its whole history | **22**, first on **2026-05-11** |

> **Corrected 2026-09-17, and the correction is left visible.** The second row
> first read **32, first on 2024-01-24**. That count was every
> `Co-authored-by:` trailer in the tree, and most of the early ones name a
> person: at `ethos` `6e70e0a7`, read 2026-09-17, **2,410 commits carry 37
> co-author trailers, of which 22 name an agent family.** The 2024-01-24
> trailer is one of the people. The hand-read that produced the original row
> used a looser test than `ai-attribution`'s own — which matches the *name*
> field against a family list and would have got it right — so this repository
> published, about somebody else's tree, the error its own detector exists to
> avoid. The window row is unchanged and was re-derived.

**So the count is four rather than three, and they are not all in one
repository.** The commit totals in the census are confirmed exactly — 186, 68,
43, 13, 10, 3, summing to 323 — and it is the disclosure sentence beside them
that does not hold.

**The interesting half is not the arithmetic.** The census concludes that the
record says a person wrote all of it, *because nothing in the commit format was
asked to record the difference.* One tree in its own table has been recording
that difference since **May 2026** — **the practice the entry says is missing
already exists inside the census**, in the tree that declined to join. It is
four months of practice rather than the two years first published here, which
weakens the point without removing it.

## What this note is not

**Not a verdict on anybody's tree**, and `ethos` has not agreed to be read: what
is above is a check of a claim made *about* that tree by somebody else, and it
goes to a person rather than outward. **Not a correction to `history.md`** —
only the president may write that file, its own LAW 4 requires the demonstration
to travel with the edit, and this is the demonstration and not the edit. **Not a
finding this tool can take credit for**: the pipeline missed it, and the reason
it missed it is that a subject's source list was narrower than a claim's scope.
