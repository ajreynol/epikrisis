# Runs — the committed evidence, and the four things written from it

**Twelve runs are in this directory and four of them carry prose.** The rest are
evidence: a pin, its candidates, and nothing anybody wrote. This page exists
because the difference is invisible from the directory listing, and opening
twelve folders to find the four with something to read is the cost it removes.

## Start here

| what to read | what it is |
| --- | --- |
| **[Stretch 2 — case study](eunoia-ecosystem-s2/2026-09-18/case-study.md)** | A stress test of the analyzer at the register's full size, with the per-repository commit census for kanon's term, the nine defects the run exposed, five things worth measuring next, and advice. **Not a report**, which is what lets it carry the last two. Also as [one self-contained HTML file](eunoia-ecosystem-s2/2026-09-18/case-study.html) — no network, no dependencies, opens from disk. **GitHub renders markdown and not HTML**, so from a browser that link shows source: use *Download raw file*, or read the markdown. |
| [Stretch 2 — report](eunoia-ecosystem-s2/2026-09-18/report.md) | The report proper for the same run: ten sources, 1,355 commits, Q1–Q8, eleven assessments. Held to [`judgement.md`](../docs/judgement.md) and validated by `check`. |
| [anoieu — report](anoieu/2026-09-01/report.md) | The first report this tool produced. One repository, 132 commits. The worked example the charter points at. |
| [ecosystem — report](eunoia-ecosystem/2026-09-01/report.md) | The first ecosystem report. Five sources, 889 commits, of which 707 are one of them. |
| [census — note](eunoia-ecosystem/2026-09-02-census/note.md) | **Not a report** — stages 1–2 only, published because the evidence bore on a figure somebody else had already put in the record and holding it would have been the failure this project named for itself. |

## Every run

Each row is derived from the run's own `corpus.json` and file list, not from
memory. `stages` is how far the pipeline was taken: **1–2** is a pin and its
candidates, **1–4** adds the declared record and the delta, **1–6** means a
report exists and `check` has accepted it.

| run | sources | commits | candidates | depth | stages | prose |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| `eunoia-ecosystem-s2/2026-09-18` | 10 | 1,355 | 554 | 1 | **1–6** | report + case study |
| `eunoia-ecosystem/2026-09-02-census` | 5 | 1,019 | 253 | 1 | 1–2 | note |
| `eunoia-ecosystem/2026-09-01-status` | 5 | 890 | 147 | 1 | 1–4 | — |
| `eunoia-ecosystem/2026-09-01` | 5 | 889 | 123 | 1 | **1–6** | report |
| `eunoia-ecosystem-d2/2026-09-02` | 5 | 939 | — | 2 | panel only | — |
| `eunoia-ecosystem-d2/2026-09-01` | 5 | 903 | 199 | 2 | 1–2 | — |
| `anoieu/2026-09-02-presidency` | 1 | 186 | 84 | 2 | 1–2 | — |
| `anoieu/2026-09-02-proto` | 1 | 165 | 81 | 2 | 1–4 | — |
| `anoieu/2026-09-02-assess` | 1 | 168 | 82 | 2 | 1–4 | — |
| `anoieu/2026-09-02b` | 1 | 155 | 63 | 2 | 1–2 | — |
| `anoieu/2026-09-02` | 1 | 136 | 60 | 2 | 1–2 | — |
| `anoieu/2026-09-01` | 1 | 132 | 58 | 2 | **1–6** | report |

**The two `-d2` runs exist to test one thing** and the subject says so in its own
`_why`: whether the 2026-09-01 calibration miss was caused by `prefix_depth` 1
collapsing every `tools/<child>` into one prefix. A separate subject rather than
a retune, so both sets of runs stay comparable.

**The five extra `anoieu` runs are evidence and were never written up.** What
each was for is not recorded anywhere, and this page does not invent it: the
columns above are what they can still be shown to be.

## Nothing compares this page to the directory

The table is hand-written and the directory is the truth, so a run added and not
listed here is drift that nothing will report — the same hazard the charter
states about the command surface, in a second place. It is cheap to check:

```sh
for d in history_analyzer/runs/*/*/; do
  printf '%-46s %s\n' "${d#history_analyzer/runs/}" "$(ls "$d" | grep '\.md$' | tr '\n' ' ')"
done
```

Twelve rows, four with prose, or this page is stale.

## What a run directory holds

`corpus.json` the pin · `events.jsonl` the candidates · `claims.jsonl` what the
subject says about itself · `delta.json` the join between them · `ratio.json`,
`panel.json` the measures · `selection.jsonl` every candidate not cited, with the
reason it was dropped · `report.md`, `assessments.jsonl` the judgement, and the
only files in here that a program did not write.

**Reports are marked `self` where the subject contains this tool**, and under
[`judgement.md`](../docs/judgement.md) a self-assessment's conclusions are never
cited outward. Every run in this directory is one.
