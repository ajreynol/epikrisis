# Epikrisis

A **repository of the Eunoia ecosystem**. Until 2026-09-14 it was a child
project of a child project, at `tools/workflow-launcher/tools/epikrisis` inside
[eudaimonia][]; the history came with it, and the paths in it are this
repository's own.

Its question is not *what does this code do*. It is: **what were the events, and
what has the way this thing evolved done well and badly?**

[eudaimonia]: https://github.com/ajreynol/eudaimonia
[the workflow launcher]: https://github.com/ajreynol/eudaimonia/tree/main/tools/workflow-launcher

## Where it came from, why it moved, and what the move does not mean

**The debt to [the workflow launcher][] is unchanged, and it runs in one
direction.** The launcher is about the first hour of a tool's life; this is about
reading the whole of one backwards. Its findings register is described on its own
front page as *what is captured across the ecosystem, what is retyped, and what
is not in the record at all* — the gap between what a project's history **says**
happened and what its tree **shows** happened, answered by hand, once, by
reading. That gap is the central mechanism here. Its stretch goal needs the same
instrument: that somebody starts a real repository through it and the result is
better than what they would have typed, *measured by what the first week of that
repository needed corrected*. Nothing here can measure that, and moving out did
not settle it — if this repository is deleted, that goal is exactly as unmeasured
as it is today, which is to say nothing breaks, because nothing was ever
measured.

**Why it moved: reachability, and not merit.** anoieu asked as `D20` and staged
it as `B23` — this is the ecosystem's only history analysis, anoieu's `laws.md`
requires a president to quote it, and it sat where the ecosystem's own inventory
validator could not list it, a child whose parent is a child. **A tool other
repositories are expected to rely on should not be findable only by knowing where
somebody filed it.** Eudaimonia's argument for the old nesting — the host asks a
question it has no instrument for, and this is the instrument — is the paragraph
above, it was good, and it was outweighed by a law written against a tool nobody
could find.

**What the move does not mean.** It is not the graduation named under *How it
ends*: that one means somebody outside the family wanted to run this on a subject
of their own, and nobody has. It is not evidence the work is good — two runs,
both self-assessments, is still the whole of the record. What changed is where
the tree sits and who can see it.

## The charter

**The question.** For a tool or an ecosystem: what were the major events in its
history, and what has its evolution done well and badly — with the first
answerable from the tree and the second answerable only with evidence from the
first?

**The scope is an edge rather than an emphasis: git histories, and nothing
else.** The corpus is what a repository's history and published trees contain —
commits, paths, dates, files as published, and what those files say about the
project. Not issue trackers, not pull requests, not discussion threads, not
anybody's account of what happened, and **not development in the abstract.** A
question unanswerable from a history is not one this answers. Narrowed by the
maintainer on 2026-09-01, because every subject this has been offered a view on
— a build system, an ethics register, a role inventory — is one a history says
less about than a reader wants, which is exactly when a tool starts answering
from the prose lying beside the evidence.

**The goals, in order.**

1. **The evidence pipeline, and the boundary in the middle of it.** Everything
   up to and including the delta between the derived and declared records is a
   program: same input, same output, byte for byte. Everything after it is
   judgement and is never written into the same file.
   [docs/design.md](docs/design.md).
2. **The detector catalogue.** What counts as a candidate event, one entry per
   detector, each with its inputs, the evidence it emits, its threshold and
   **its known failure mode** — because a detector whose failure mode is
   unwritten will be trusted exactly where it is wrong.
   [docs/events.md](docs/events.md).
3. **Making an assessment falsifiable.** A report that says a project evolved
   well is worthless unless it could have said otherwise. The pre-registered
   questions, the required negative findings, the per-assessment falsifier, and
   the mechanical checks that enforce all three.
   [docs/judgement.md](docs/judgement.md).
4. **The two subjects**, below; one has been run and one has not.
5. **Later**, and a scope change rather than an elaboration: the postmortem on
   the commits themselves.

**The stretch goal.** That a report produced this way tells somebody who knows
the subject well something they did not already know — and that they say so.
That is the only test of this kind of tool that is worth anything, it cannot be
self-administered, and it is not close.

**The standing.** Nothing here argues for its own authority, in any document.
What a reader is offered is evidence they can rebuild and a witness they can
impeach; if that is not enough, nothing said on top of it would help. Below, in
full: a responsibility and not a rank, and being relied on makes it one.

**What is out of scope.**

- **Judging people.** The unit of analysis is the artifact. Author names do not
  leave the first stage of the pipeline, and this is enforced by the schema
  rather than promised in prose — counts and anonymous ids may travel, names may
  not. A history-of-a-project report is one careless step from a performance
  review of the people in the log, and that step is not taken here.
- **Publishing about somebody else's project without asking.** Inherited, not
  invented: see below.
- **Generating the report.** The pipeline assembles evidence and checks a report
  against it. It does not write the narrative — the split is the launcher's own,
  and the reasons are in [docs/design.md](docs/design.md).
- **Prediction.** What a project should do next is not this. Every claim is about
  what happened, and the tense is the boundary.
- **Grading the ecosystem outward.** A run whose subject is a tree this family
  owns is marked as a self-assessment and is held to a stricter standard, and its
  conclusions are never cited outward as evidence that the family's work is good.
- **Any subject that is not a history.** Conduct, intent, design quality and
  what a document means are not readable from a tree.
- **Being fast, being general, being a product.** No users, no stability, no
  promise that any of it survives the first real run.

## The agenda, revised against EXT-1

Revised 2026-09-02, after scanning the only worked example of this kind of tool
we have access to: **`EXT-1`**, the external repository index that approached
cvc5 with a badge. It is named, linked and scanned feature by feature as `N14`
in the launcher's findings register, and the code name is deliberately not from
the ecosystem's own register — a Greek name would read as membership, and
allocating one is not ours to do. (`D7` and `D8` predate the name and identify
the service in full, so nothing there is ambiguous.)

**The altitude, added 2026-09-02 after the tool failed on it.** The job is to
**explain a history at the right level of abstraction** — not to list what
changed. Two things follow, and only the second is a licence to build anything.

- **The abstraction is stage 5 and stays there.** *A protocol register was
  created* is a sentence a person writes; a program that produced it would be
  summarising documents, which is refused. Nothing here changes that.
- **But the evidence has to be assemblable at that altitude**, and twice it was
  not. **Coverage:** ten commits creating this ecosystem's newest governing
  documents produced **zero candidates**, because `governance` decides what
  governs from a filename list baked into the code and neither file is on it.
  **Aggregation:** where it does fire it emitted nine separate *revised*
  candidates on one file in one day, leaving a reader to do the grouping by hand.
  A tool that reports nine line-counts where the event was *a register was
  written* has answered at the wrong altitude even when every number is right.

**And the repair is not to add the two filenames.** A list edited after seeing
what it missed is a threshold fitted to the answer, which this tool flags when it
happens to a number and should not do quietly to a regex. The list belongs in the
subject file, where what governs a tree is declared, pinned and arguable —
which is the guardrail's own instruction on breach, applied to itself.

**Three things to build.**

1. **Release recency from tags.** The `release` detector reads tags and stops.
   Days since the newest tag matching a subject's version pattern is cheap, in
   scope, and is the exact reading `EXT-1` got wrong by a factor of 13.6 — by
   taking it from a platform release object instead of from the history.
2. **Agent-context arrival.** When agent-guidance files first appeared, and
   whether they have moved with the code since. Presence is a snapshot anybody
   can take; arrival and drift are history, and this is the one place our
   subject and `EXT-1`'s genuinely overlap.
3. **A second subject for `panel`.** Four of the scan's *we do better* claims
   rest on a single run inside this family. **An instrument that has only been
   pointed at its owner has not yet earned a comparative claim**, and the scan
   says so about itself.

**Five things not to build, and the reasons are not the same reason.**

- **Security posture and dependency advisories.** Useful, and somebody else's
  reviewed instruments. Citing beats reproducing, which this ecosystem already
  argues elsewhere.
- **Popularity, ecosystem adoption, issue responsiveness.** Platform data, not
  reproducible from a pin — the scope edge, not a preference.
- **Maintainer resilience.** Out by the schema. *Does this project have one
  maintainer* is a fair question from a consumer and we will not answer it, and
  that is a cost rather than a virtue.
- **Code legibility, or any quality score.** Already refused in the catalogue.
- **A composite.** The deepest defect in `EXT-1` is that a weighted average made
  a contradiction vanish — Development Activity 99 beside release recency 0/36,
  reported as Vitality 81. **This tool will not acquire one**, and if a reader
  ever wants a single number out of it, the answer is that there is not one.

**The question that stays open, recorded so it is not mistaken for settled:**
what `EXT-1`'s error rate actually is. We have reproduced one defect. **One is
not a rate**, and the party most tempted to treat it as one is the party that
found it.

## The role it is asking to hold

Added 2026-09-01 by the maintainer, in an explicit instruction, which is the
decision a scope change needs. **It is asked for and not claimed** — standing in
this ecosystem is conferred by somebody choosing to rely on a tool, never by the
tool saying so, and the register that would record it is in another tree.

**The audit of how this repository and its ecosystem have evolved:** what
happened, in what order, and what the way they changed did well and badly —
answered from the trees, with every claim resting on evidence a reader can
re-derive.

The precedent is one subject over: **euthyna**, a child project in eudaimonia,
holds the audit of what a proof development is *made of*, statically. This is
the same shape asked of a trajectory rather than an artifact.

**Not this role**, and the exclusions are the part that makes it safe to grant:

- **Deciding whether the evolution was good.** That is contestable, nobody has
  the authority to settle it, and it may never acquire a checker. What this
  produces is evidence and an argument answerable to it.
- **Grading any tree that has not agreed to be read.** The constraint above
  governs; a run on somebody else's subject is internal by default.
- **Anything about people.** Enforced by the schema, not by discipline.
- **Speaking for anybody else.** Its conclusions are not eudaimonia's positions,
  not anoieu's, and not the ecosystem's, and none of them leave by machine.
- **Auditing itself into significance.** Every run whose subject includes this
  family is marked a self-assessment, a self-assessment with no negative
  findings is void, and its conclusions are never cited outward — not as
  evidence that these practices work, not in a vision document, not in a README.

**What it has actually done, so that the ask is not read as more than it is:**
one run, on a self-assessment, and the next section gives it at full size
because the record is the whole of the argument.

## Why any of this should be taken seriously: a duty, and not an argument

Added 2026-09-01 by the maintainer, in an explicit instruction, and put to the
ecosystem's chief executive role as topic `D5` rather than asserted here. The
occasion is that the role is building a **build system** and this reads how
things have been built in these trees, so the question arrives in the form that
makes it real: *why should this count?*

**It dissolves on contact with results.** An argument for one's own authority is
only needed where the evidence is missing: where evidence exists it is redundant,
and where it does not it is what a tool offers *instead* of findings. So there is
no case for standing here — two things stand in its place, neither rhetoric.

1. **Evidence.** Stages 1–4 are re-derivable byte for byte from a pin and stage
   5 is a different file, so a reader who distrusts the conclusion rebuilds the
   evidence and disagrees with the writing having established that the writing
   is the only thing in dispute — a property of the file layout, not a claim
   about quality: it holds whether this tool is good or bad.
2. **The standing of an expert witness, never an advocate**, which is the whole
   of the position; the rest of this section is what it costs.

### What the witness distinction actually commits this to

A witness testifies to what they observed. They do not argue for the verdict or
decide the case, and their standing comes not from being right but from being
**examinable**: one who cannot be cross-examined is worth nothing however
accurate they are, and one who advocates is impeached whatever they know.

Read that against machinery already built, none of it for this argument:

- **The 4/5 boundary** keeps what was observed apart from what is concluded.
- **`questions_digest`** fixes what was asked before the evidence was seen and
  **`thresholds_changed_after_events`** flags a parameter tuned after it: a
  question fitted to an answer and a judgement moved into a constant both leave
  a mark.
- **A written failure mode per detector**, before anybody has to find out.
- **A self-assessment with no negative findings is void**, so *we looked and it
  was fine* is unavailable rather than merely discouraged.
- **Names never leave stage 1**, by schema.

**Every one makes this tool easier to impeach — the exposure is the
credential**, and there is nothing else on offer.

### The testimony so far, at its honest size

Two runs, both self-assessments, and what each found wrong with itself is the
part worth citing. The first retracted two of its eight questions, declared two
more unsafe, called its own calibration optimistic and "not this tool's
performance", and four defects were found in the tool by running it a second
way. The second reproduced the first's matcher defect on a new subject — its
one match was a word collision — was blind in the place the subject had told it
in advance mattered most, and had to mark its most legible finding as hand-read
because no detector in the catalogue produces it.

That is small, and it is the only kind of record that could support a position
like this: **a run finding everything it looked for and nothing wrong with
itself would be the best reason available to disbelieve the next one.** What is
cited here is what those runs found about *this method*, which is this project's
to keep; what they concluded about their subjects appears nowhere here.

### Why this is a responsibility and not a rank

**Because being taken seriously moves the cost.** If a build system is designed
partly on what this reports and this was wrong, the loss lands on whoever relied
on it, and there is no version where the tool pays. A position that transfers
cost to whoever relies on it is a duty in exact proportion to its usefulness.
Three obligations follow, none optional:

- **Be checkable.** Never say more than a reader can re-derive from a pin; a
  finding somebody must take on trust is not this tool's to offer.
- **State the limit out loud.** *This tool cannot establish that* is a result,
  given as freely as any other; answering a smaller question because the
  machinery reaches it is the failure the guardrail below names.
- **Speak.** Silence is also a way of being wrong. The chain from here to
  anywhere the output could matter was two hops, and it was recorded here that a
  finding could die in it unnoticed; the move shortened it to one. Holding
  evidence that bears on a live decision and saying nothing is not modesty: the
  duty forbidding overclaiming is the one requiring volunteering.

### The tense boundary, applied to the occasion

A build system is a decision about what to do next, so what this brings to it is
not advice: what happened when things were built in these trees before, in what
order and at what intervals, and never what should therefore be done. That is
the verdict, it belongs to whoever is accountable, and a witness who reaches for
it stops being one — **which is what makes the position safe to grant**, since a
role abusable only by a tool willing to argue costs nothing to give to one that
refuses to.

**What of this is transferable is a design and not a conclusion**, so it travels
where claims about practice are supposed to: `N13` in the launcher's findings
register, with its falsifier attached and nothing about this family attached.

### What would forfeit the position

Stated now, because standing that cannot be lost was never standing:

- a run about this family cited outward as evidence that these practices work —
  in a vision document, a README, or one sentence to anoieu;
- a report whose confidence outruns what stages 1–4 emitted, anywhere, once;
- an answer to *what should we do*, however lightly phrased;
- an argument offered in place of evidence — **including this section**, if it
  is ever doing work the runs cannot back. It is not evidence of anything, and
  on the day it is cited as though it were, delete it.

## The guardrail on the role: ambitious in functionality, unambitious in implementation

A granted role is a licence to grow, so the limit is attached to the request
rather than left for later. **The ambition goes into the questions and the
evidence. It does not go into the machinery.**

### Why this particular guardrail, and not a general plea for simplicity

Because there is a specific way an analysis tool goes wrong, and it does not
look like sprawl. **Implementation ambition in a tool like this takes the form
of absorbing judgement into code, where nobody can see it.** A cleverer detector
is one that has swallowed a decision somebody should have been able to argue
with. Four instances from this project's own first week:

- a matcher joined 105 claims to 123 events and produced **982 matches**. A
  smarter matcher would have produced a plausible number and hidden the fact
  that its window was wider than four of the five subjects' entire histories;
- a classifier filed a 750-line program as neither code nor prose. A cleverer
  classifier would have guessed right and been unfalsifiable;
- reading commit messages to decide what happened is refused outright, and is
  the single most tempting improvement available;
- a threshold edited after the events exist sets a flag on the run, because a
  threshold fitted to the answer is a judgement that has moved into a constant.

In every case the *dumber* implementation is the one whose errors were visible.
That is the whole argument.

### What is held small, counted

`epikrisis budget` counts it, exits non-zero over any limit, and the selftest
proves that check can fail:

| | limit | why |
| --- | --- | --- |
| the tool | **1,500 lines** | a reader must be able to check the whole of it in an hour. A tool whose findings can only be trusted is not evidence |
| prose about the tool | **no more than the tool** | the account may not outgrow the thing it accounts for. Counted over `docs/` and this file |
| third-party imports | **zero** | stdlib only: no install, no version skew, no supply chain |
| network imports | **zero** | the corpus is on disk. Nothing here fetches, and nothing here can be pointed at a service |
| subprocess call sites | **two**, both git wrappers | **the derivation path may run `git` and nothing else.** This is the limit that matters: it is what makes it structurally impossible for a model, a service or any other program to enter stages 1–4 |

**On breach, the first move is not to raise a limit.** It is to delete a
detector whose candidates are always dropped, or to move a judgement out of the
code and into the report where a reader can disagree with it. Raising a number
is a person's decision and is recorded as one.

**It is in breach twice today, and the second one is the promotion's bill.** The
tool is 1,511 lines against 1,500, crossed in the last commit to touch it. Prose
is 1,687 against the 1,511 the first number allows, because becoming a repository
required two documents the shared policy asks of a repository and asked of no
directory — a maintenance note and a correspondence file — and the counter reads
every `.md` under `docs/` as prose about the tool. **A channel to other
repositories is not an account of this one.** So either the counter is wrong or
the limit is, one is a change to a tool already over its own line budget and the
other is a number, **and both are a person's decision rather than an agent's.**
Neither was taken here. `D1` puts it to anoieu, whose policy the second half of
the bill is for.

### And the other half, which is not negotiable either

*Unambitious in implementation* must not become an excuse to ask a smaller
question. So, held large:

- **The question stays whole.** What happened, in what order, and what the way
  it changed did well and badly — over a whole ecosystem, across repositories,
  over its entire history. Nothing is narrowed to fit the machinery.
- **It may be pointed at any subject a person names**, at any scale, including
  ones far larger than anything it has run on.
- **It may say hard things**, including about the family that carries it, and
  the arrangement that a self-assessment is void without negative findings
  exists to make that likelier rather than safer.
- **Refusing to answer is allowed; shrinking the question is not.** *This tool
  cannot establish that* is a result. *This tool answers a smaller question
  instead* is a failure, and the second is what a budget tempts you toward.

The test, in one line: **if this became twice as useful, the code should not get
much bigger** — the detector catalogue would get better failure modes and the
questions would get sharper. If usefulness and size move together, judgement is
being absorbed and the guardrail has already failed.

## Receiving an epoch

Global announcements reach the ecosystem from whoever holds its chief executive
role — **currently anoieu**, and the role rather than the tree is what this is
keyed to, since the shared machinery may move. An **epoch announcement** marks
a boundary in the ecosystem's life, and that makes it directly this project's
business for a reason that is not deference:

**An epoch is the window this tool does not otherwise have.** Everything here is
reported per month, and a month is an arbitrary unit borrowed from the calendar
— it has no relationship to anything the ecosystem did. An epoch boundary is a
unit the subject itself declares, which turns *what happened between these two
points* from a choice this tool makes into a fact it reads. That is a better
instrument, and it is free.

**What this needs an announcement to carry**, stated now because it is far
cheaper to say before the first one exists than after:

| | why |
| --- | --- |
| a stable **identifier** | so two runs can name the same epoch and be compared |
| a **start**, as a commit or a date | so a window has an edge a program can find |
| **where it is recorded, as data** | the detectors here read status transitions out of an inventory file's own history. If an epoch is recorded that way it is readable on the day it lands; if it is recorded in prose, nothing here can see it and the audit reverts to months |
| what it **declares** | an epoch that names nothing changed is a date, and this tool would have nothing to report about it |

The last two are carried upstream in `D4`, and raising them before the format
exists is the cheap moment.

**An office now holds that role.** Two things it may ask for cannot be answered
here, and both are recorded in [docs/notes.md](docs/notes.md) as defects rather
than as deference: the CI run history, which is outside the corpus permanently,
and the documents that constitute the office, which no detector saw.

**Until an announcement arrives, nothing here waits on it.** A tool that cannot
work without a thing that does not exist yet has made itself somebody's
dependency: this one reports per month today and gains a better window when
there is one.

## The two initial subjects

Chosen because they are as different as two histories can be while both being
readable, and a detector set that works on one and fails on the other has told us
which of the two it was actually written for.

| | **cvc5** | **the Eunoia ecosystem** |
| --- | --- | --- |
| shape | one repository, long, many hands | several repositories, young, few hands |
| derived record | rich — the thing the detectors were designed for | thin: too few commits for anything statistical |
| declared record | conventional — releases, notes | unusually dense: dated correspondence, decided proposals, a register of names, roadmaps with checkboxes, retirement notes |
| what it tests | whether the detectors find events at all in a real history | whether the delta between what a tree says about itself and what it shows is computable |
| what it constrains | somebody else's project. See below | our own. Self-assessment rules apply in full |

The ecosystem case needs machinery the single-repository case does not: events
that live in no repository's log — a repository being created, a name being
taken, a role moving, a child project retired. The design carries both and
[docs/design.md](docs/design.md) says where they diverge.

**Two subjects have been run, both self-assessments**: the ecosystem, and a
single tree — `anoieu`, added 2026-09-01 at the maintainer's instruction and run
at `prefix_depth` 2 to correct a recall miss the first run published about
itself. **cvc5 has not been checked out and has not been read**: the constraint below
binds before a first run, and there has not been one.

## The constraint it inherits

cvc5 is somebody else's work, and a public account of what a project's evolution
did badly is the kind of thing its authors did not ask for and cannot answer.
That is not a new problem and this project does not get to solve it from scratch:
the position is the one the family has just had to work out — that published is
not the same as available, that unpublished work is its authors' alone, and that
the trigger for asking is **who carries the cost if the output is misread**
rather than whether the reading was permitted.

Concretely, and these bind before the first run:

- **Unpublished material is out**, absolutely: no private branches, no drafts, no
  anything shared in confidence. Public history in the form its authors published
  it, and nothing else.
- **A run on somebody else's subject is internal by default.** Nothing about
  cvc5 leaves this repository without going through the ordinary reporting
  discipline and, per the position above, without asking. There is no route by
  which an assessment of another project's evolution becomes a public artifact on
  this project's own initiative.
- **The report may not be a verdict on a project that did not ask for one.** A
  finding about *this method* — that a detector missed something, that a delta
  class was empty — is this project's to keep. A finding about *them* is theirs.

It is worth saying which way this cuts: the constraint is not a formality here.
The most interesting subject available is somebody else's, the analysis is cheap,
and the output would be publishable and would get read. Every part of that is the
reason to write the rule down before the first run rather than after it.

The general position is open with the ecosystem as topic `D1` in eudaimonia's
correspondence — raised by the tree this used to sit in, because this one could
not raise anything: two levels inside a repository, everything it wanted to say
travelling by a person up through the launcher, up through Eudaimonia, and out.
**That chain is now one hop** and this repository keeps
[its own correspondence](docs/discussion.md). The risk recorded then — that a
finding dies in the chain and nobody notices — is smaller and is not gone:
nothing leaves here by machine, and a person still carries it.

## The name

*Epikrisis* (Greek **ἐπίκρισις**, from ἐπικρίνειν "to judge upon, to determine")
is judgement passed over something already complete. Medicine took it and gave it
the exact shape this project wants: an *epicrisis* is the summary written at the
close of a case — the course of events set down in order, followed by an
assessment of how the case was handled. Two parts, the second resting on the
first, and the whole of it retrospective.

That is the argument for the name and it is the argument somebody should attack.
The obvious objection is that a project is not a patient, is not finished, and
has no attending physician to be judged — and the strongest form of it is that
the medical word carries an authority this tool has not got. The reply is that
the *structure* is what is borrowed, not the standing: events first, assessment
second, assessment answerable to events. If the name ever starts doing work the
tool cannot back, it is the wrong name.

It is deliberately not **historia** — the account of what happened — because a
name that needs no explanation is not following the ecosystem's convention, and
because the account is only half of this. It is deliberately distinct from
**euthyna**, the audit at end of term, which is taken and is a child project in
eudaimonia: that one asks what an artifact is *made of*, statically. This one
asks what a trajectory *did*. Adjacent, and not the same question.

The register of names is anoieu's. `epikrisis` reaches it only as a row in the
table of names chosen in somebody else's tree, recorded there as *proposed for a
repository of its own* — a proposal that has now been acted on, in an entry that
has not moved. Correcting it is a person's edit in somebody else's tree; nothing
here makes it, and until somebody does, the name is used here and claimed
nowhere.

## Still an island, and now a checked one

Nothing in the launcher links here, imports from here, or runs anything here, and
nothing in Eudaimonia does either. This repository is on no build path, in no CI
job, in no generated document, and deleting it changes nothing anywhere —
deleting it is the test, and it still has to pass against both former ancestors.

It reads whatever it likes: checkouts staged elsewhere on disk, this family's
own trees, published history. It writes only inside itself.

**A program checks this page now, and that is the substantive change.** The old
position was one directory deeper than anoieu's `policy_check.py` enumerates, so
the rules it enforces were not enforced here, and what stood in place of a
guarantee was a sentence saying that if this README drifted no program would say
so. It runs against a checkout at `--root`; it was run on the day of the move and
**it failed here in five places**. What it found, and what was done about each, is
[docs/discussion.md](docs/discussion.md). It is no longer this page's word for it.

**There are two copies of this tool and the second is not ours to delete.**
Eudaimonia still tracks the whole of it at
`tools/workflow-launcher/tools/epikrisis`, byte-identical at the moment of the
move: promotion was a copy, so the ecosystem's only history analysis now exists
twice, once where nothing can list it. **This copy is the authoritative one**, by
the decision that made it a repository. Removing the other is eudaimonia's edit
in eudaimonia's tree, it is raised there rather than performed here, and until it
happens a reader can find a stale front page by the route the old one documents.

**And the count that was unflattering has not improved by moving.** The old
paragraph here observed that eudaimonia was carrying four speculative directories
against one framework that ships — a tree becoming a speculation warehouse, in
the ecosystem's own phrase, raised elsewhere as a reason to refuse a child
project rather than as a compliment. Promotion subtracts one from that count and
adds a repository to the ecosystem's, which is the same measurement wearing
different clothes. Two runs, both self-assessments. The ending this should still
expect is retirement, and **a repository is a more expensive thing to retire.**

## Later: the postmortem on the commits themselves

**Added 2026-09-01 by the maintainer, in an explicit instruction; a scope change
and not an elaboration, since generating prose is out of scope above.**

**The service.** For a commit: what it did, derived from the tree; what its
message said; and where those differ, the message it should have carried. Truth
first and clarity second — the name's own structure, at the smallest unit there
is. A postmortem and not a correction: the original stands, and the pair is the
finding.

**A commit message is the declared record at its finest grain**, so this is the
delta already designed, one level down — and the standing refusal to read
messages to decide what happened is what qualifies this to grade one: a tool
that inferred events from messages would be checking a message against itself.

**The expensive decisions, taken now.** It **never rewrites** — a pin is a sha.
**The corpus may not eat its own output** — an annotation is declared record,
and extracting it collapses the delta into agreement with itself. **The boundary
holds** — what it did is derived, what it should have said is judgement, stage 6
checks the second against the first unmodified. **The unit stays the artifact** —
never a fact about whoever wrote it, and per-author roll-ups are refused before
anybody wants one.

**The active version is refused here and proposed elsewhere.** A *why* demanded
at write time puts this tool in the commit path and makes development depend on
it, which is what it has refused to be. So it is a rule for people, on the one
file worth the cost — `D6` puts it to the kernel's owner — and this stays
retrospective and audits compliance afterwards. That rule also supplies the
delta's missing control: a tree where every change carries its why is the only
place a `derived_only` pile means absence rather than a record nobody kept.
**What would kill the whole of it:** annotations that paraphrase `--stat`.

## How it ends

Three endings and a person picks: it **graduates**, which for this would mean
somebody outside the family wanted to run it on a subject of their own; it is
**folded** into the launcher, meaning the delta machinery becomes how that
project's findings register is maintained and the rest is dropped; or it is
**retired in place**, with a line here saying what the design got wrong, which is
the ending to expect.

**Moving to a repository of its own is what the shared policy calls graduation,
and this page does not get to call it that.** That test is the boundary; the test
written here is that somebody outside the family wanted this, and nobody has. So
all three endings stay open, and the middle one got dearer: folding back is now a
decision between two repositories rather than a directory being deleted.

A fourth, specific to this one: **retired at the first real run**, because the
detectors found nothing a person reading the log would not have found faster.
That is a live possibility, it is what the calibration step in
[docs/judgement.md](docs/judgement.md) exists to detect early, and it would be a
result rather than a failure.

Going quiet is not one of them.

*Started 2026-09-01 by the maintainer, in an explicit instruction, on the
principle that the design was the deliverable and that evidence gathered before
the boundary in it was agreed would be evidence nobody could check. Two runs have
been made since, both self-assessments, both under `runs/`. Promoted out of
eudaimonia to a repository of its own on 2026-09-14.*

## How this repository is maintained

This repository is part of the **Eunoia ecosystem** and follows its shared
repository policy, kept by [anoieu](https://github.com/ajreynol/anoieu) in
[`docs/policy.md`](https://github.com/ajreynol/anoieu/blob/main/docs/policy.md).
It came under that policy on 2026-09-14, on being promoted out of eudaimonia, and
was checked against it the same day — `policy_check.py --root` from an anoieu
checkout is what a reader runs to see whether this paragraph is still true.

**Written by AI agents, under light human supervision.** A human directs the
work, decides what this repository is for, and reads what is published here;
nobody vets the internal design, and nothing here is carried into another project
without review.
