# LOC snapshots

Each snapshot counts the committed trees at the pins in its `corpus.json`.
The report is generated from per-file evidence and can be reproduced with the
checkouts. Reports use counting rules v2: documentation follows the shared
layout, while JSON, repository metadata and other data files are ignored.
An explicit recount records its timestamp and preserves the snapshot's pins.
See the [LOC analyzer README](../README.md) for the counting rules.

| Subject | Snapshot | Report | Evidence |
| --- | --- | --- | --- |
| Eunoia ecosystem, including cvc5 and ethos `main` | 2026-09-18 | [LOC report](eunoia-ecosystem/2026-09-18/report.md) | [Manifest](eunoia-ecosystem/2026-09-18/corpus.json), [totals](eunoia-ecosystem/2026-09-18/loc.json), [per-file counts](eunoia-ecosystem/2026-09-18/files.jsonl) |

The [published LOC index](https://ajreynol.github.io/epikrisis/loc/) discovers
snapshots from their manifests. This Markdown index is maintained alongside the
committed runs.
