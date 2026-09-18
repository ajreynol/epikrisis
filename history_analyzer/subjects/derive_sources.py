#!/usr/bin/env python3
"""Emit an ecosystem subject whose source list is derived from the register.

The defect this exists against, measured rather than asserted: a subject whose
sources are hand-written falls behind the register silently, and the cost is not
the size the declaration implies. At the 2026-09-18 pin the seven-source subject
reported 1,298 of 1,355 commits over whole histories -- 4.2% short -- and 177 of
221 over the current stretch, 19.9% short, because the trees it does not read are
the newest ones. A stale source list under-reports exactly what is new, and the
whole-history view hides it. See ../docs/notes.md.

The register is already inside the corpus: `kanon scripts/ecosystem/ecosystem.json`
is what `inventory` reads, and membership is decided there and nowhere else. This
reads the same file and writes the source list from it, so the denominator cannot
drift from the thing that defines it.

Stdlib only, like the analyzer. It is not part of the analyzer: `epikrisis budget`
parses bin/epikrisis alone, so nothing here is metered by it -- which is recorded
in ../docs/notes.md rather than relied on.

    derive_sources.py <path to ecosystem.json> <subject-id> > subjects/<id>.json

Regenerate rather than edit. A hand-edit to the output is the defect returning.
"""
import json
import sys

# A president is a member that also holds an office; both are under the policy.
# Every other footing -- candidate, associate, outsider, foundation, child --
# is outside the member set, and `child` is never a checkout of its own.
UNDER_POLICY = {"member", "president"}


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__.strip().splitlines()[-3].strip())
    reg_path, subject_id = sys.argv[1], sys.argv[2]
    reg = json.load(open(reg_path))
    members = sorted(n for n, e in reg.items()
                     if isinstance(e, dict) and e.get("status") in UNDER_POLICY)

    out = {
        "subject": subject_id,
        "kind": "ecosystem",
        "self": True,
        "_source_list_derived": {
            "from": "kanon scripts/ecosystem/ecosystem.json",
            "rule": "status in {member, president}",
            "by": "history_analyzer/subjects/derive_sources.py",
            "count": len(members),
            "note": ("derived rather than hand-written. The defect it is against "
                     "is a subject whose denominator falls behind the register "
                     "while still reporting a total as though it covered the "
                     "ecosystem."),
        },
        "sources": [{"id": n, "origin": reg[n].get("url", "")} for n in members],
        "exclude": ["deps/", "checkers/", ".lake/"],
        "not_in_corpus": [
            ("ethos, which holds the proof checker and the compiler, is not read "
             "here: its footing is candidate rather than member, so it is outside "
             "the member set as well as outside this corpus. The effect is that "
             "the ecosystem's history as this run sees it is missing one of the "
             "two trees holding its executable artifacts, and ethos is the tree "
             "that has disclosed agent co-authorship since 2026-05-11."),
            ("child projects are not separate sources. Each is read inside its "
             "parent's tree at the parent's pin, so a child that moved between "
             "parents appears here as a directory arriving and a directory "
             "leaving, and never as one event."),
            ("issue trackers, pull requests and discussion threads, for every "
             "source, by design"),
            "anything unpublished, absolutely",
            ("any window. This tool reports over whole histories up to the pin "
             "and has no --since. A stretch-scoped figure cannot be derived by "
             "this pipeline, which is the limitation recorded as D4."),
        ],
        "thresholds": {"prefix_depth": 1, "quiet_min_days": 3,
                       "rewrite_window_days": 7},
        "inventory": {
            "source": "kanon",
            "path": "scripts/ecosystem/ecosystem.json",
            "track": ["status", "proposed", "parent"],
            "note": ("the register is in kanon's tree and its git history is the "
                     "status-transition record. It was created there on "
                     "2026-09-15 by the governance handoff, so its history in "
                     "this tree begins then and every transition before that "
                     "date is not readable here."),
        },
        "prose_is_product": ["anoieu", "kanon", "aisthesis"],
        "_prose_is_product_note": (
            "anoieu ships the checker other repositories' CI depends on; kanon "
            "ships the policy, laws and register those checks are against; "
            "aisthesis is two documents and nothing else. For these a prose line "
            "is a tool line and the ratio is not comparable with the others. A "
            "declared judgement, not a derived fact."),
    }
    json.dump(out, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
