#!/usr/bin/env python3
"""Emit an ecosystem subject from the register and explicit coverage requests.

The defect this exists against, measured rather than asserted: a subject whose
sources are hand-written falls behind the register silently, and the cost is not
the size the declaration implies. At the 2026-09-18 pin the seven-source subject
reported 1,298 of 1,355 commits over whole histories -- 4.2% short -- and 177 of
221 over the current stretch, 19.9% short, because the trees it does not read are
the newest ones. A stale source list under-reports exactly what is new, and the
whole-history view hides it. See ../docs/notes.md.

The register is already inside the corpus: `kanon scripts/ecosystem/ecosystem.json`
is what `inventory` reads, and membership is decided there and nowhere else. This
reads the same file and adds the explicitly requested projects below. Inclusion
in an analysis does not assign ecosystem membership; the selection records both.

Stdlib only, like the analyzer. It is not part of the analyzer: `epikrisis budget`
parses bin/epikrisis alone, so nothing here is metered by it -- which is recorded
in ../docs/notes.md rather than relied on.

    derive_sources.py <path to ecosystem.json> <subject-id> > subjects/<id>.json

Regenerate rather than edit. A hand-edit to the output is the defect returning.
"""
import hashlib
import json
import sys

# A president is a member that also holds an office; both are under the policy.
# Every other footing -- candidate, associate, outsider, foundation, child --
# is outside the member set, and `child` is never a checkout of its own.
UNDER_POLICY = {"member", "president"}
TRACKED = ("cvc5", "ethos")
# Explicitly requested analysis coverage, independent of registry footing.
INCLUDED = {"eunoia": "https://github.com/ajreynol/eunoia",
            "paideia": "https://github.com/ajreynol/paideia"}


def main():
    if len(sys.argv) != 3:
        raise SystemExit(__doc__.strip().splitlines()[-3].strip())
    reg_path, subject_id = sys.argv[1], sys.argv[2]
    with open(reg_path, "rb") as f:
        raw = f.read()
    reg = json.loads(raw)
    members = sorted(n for n, e in reg.items()
                     if isinstance(e, dict) and e.get("status") in UNDER_POLICY)
    names = sorted(set(members) | INCLUDED.keys())

    out = {
        "subject": subject_id,
        "kind": "ecosystem",
        "self": True,
        "_source_list_derived": {
            "from": "kanon scripts/ecosystem/ecosystem.json",
            "rule": "status in {member, president}, plus explicitly requested project coverage",
            "by": "history_analyzer/subjects/derive_sources.py",
            "count": len(names),
            "member_count": len(members),
            "register_digest": hashlib.sha256(raw).hexdigest(),
            "explicit_inclusions": [{"id": n, "registered_status": reg.get(n, {}).get("status", "unlisted")}
                                    for n in INCLUDED],
            "note": ("Members are derived from the committed register; eunoia and "
                     "paideia are explicitly requested coverage. Analysis inclusion "
                     "does not establish or change a project's ecosystem footing."),
        },
        "sources": [{"id": n, "origin": reg.get(n, {}).get("url") or INCLUDED.get(n, ""),
                     "ref": "main"} for n in names],
        "tracked_sources": [{"id": n, "origin": reg[n]["url"], "ref": "main"}
                            for n in TRACKED],
        "exclude": ["deps/", "checkers/", ".lake/"],
        "not_in_corpus": [
            ("cvc5 and ethos have commit counts and main-branch pins in "
             "commit_tracking. They are outside the primary analysis corpus; "
             "events, claims and assessments do not cover them. Ethos compiler "
             "work on ethosEoc3 is outside the tracked main history."),
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
