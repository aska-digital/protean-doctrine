---
name: protean-operating-doctrine
description: Use when running any project with the Protean pipeline. Default stages, delegation map, handoff protocol, and QA gates.
version: 1.3.0
license: MIT
---

# Protean Operating Doctrine (platform-agnostic, always active)

The default working procedure for executing projects with the Protean System. The
orchestrator applies this project and session workflow identically on every
platform. A separate operator-relay layer sits above this doctrine for
cross-project coordination. A minimal generalist profile sits outside the
workflow and is used only when the structure would add overhead.

Platform mechanics (how a delegation is actually launched on a given surface)
are intentionally not part of this doctrine. It names the constant both
surfaces share: the stage order, the ownership boundaries, and the gates.

---

## 1. The default pipeline (research -> analysis -> design -> build -> QA)

Sequential value-adding stages, run in this order, with a QA gate at the end. Do
not skip stages and do not merge roles.

| Stage | Owner | Deliverable |
|---|---|---|
| Research | research | decision-ready brief |
| Analysis / Architecture | architecture | system architecture, build-handoff spec, design-input brief, locked decisions |
| Design / UX | design | information architecture, flows, content inventory, copy tone, mockup |
| Build | build | working, tested artifacts |
| QA gate | QA | test plan, adversarial tests, scope guardrails, gate verdict, loop-back findings |

**Contribution order (default):** orchestrator -> research -> architecture ->
design -> build -> QA -> orchestrator (QA gate last). The QA gate cuts across
overengineering at every stage and loops findings back to the owning role. After
the gate passes, work is delegated dynamically within roles.

**Meta hierarchy.** An operator-relay profile condenses information and
coordinates across projects and orchestration instances. The orchestrator owns
orchestration inside one project or session. The generalist is outside the core:
use it for basic self-contained tasks when this pipeline would add overhead; it
never substitutes for the relay or the orchestrator, and it does not ship.

## 2. Role delegation map (universal)

| Task | Route to |
|---|---|
| Code, features, debugging from an approved design | build |
| Deep research, hidden connections, writing, documentation, communications | research |
| Stress-test, devil's advocate, find flaws | QA |
| Solution and software architecture, structural codebase changes, invariants, interfaces | architecture |
| UX/UI, user-facing work, interaction and visual design | design |
| Decision that changes scope or overrides a domain boundary | orchestrator (never pushed down) |

**Ownership hard gate.** The build role must not invent or revise architecture,
data models, module boundaries, invariants, public interfaces, clustering
semantics, migration strategy, or acceptance-test structure. Those decisions
require a stable architecture handoff. Build implements the approved decision and
writes implementation tests. Architecture owns technical decisions and receipt
structure; research owns all wording, docs, delta language, and
architecture-facing prose; build supplies evidence but does not author claims
about architectural compliance. QA may identify defects and required evidence but
may not redesign the system. Design owns UX layout and interaction; wording
sign-off sits with research; architecture owns software and solution decisions.

**Decision routing.** All command-level judgment routes up to the orchestrator,
never down to sub-agents. Domain expertise stays inside the owning domain. A task
that crosses domains is split into sequential handoffs with explicit file
ownership, stable inputs, and a named approver before implementation begins.

**Required dispatch fields.** Every brief states role, allowed decisions,
forbidden decisions, owned files, upstream stable handoff, and exit evidence. A
worker may not modify a file outside its owned boundary.

## 3. Lean and Six Sigma flow (Lean-Sigma fusion)

- **Parallel, not sequential:** hand off partial work the moment a section is
  stable (just-in-time pull). Do not wait for one role to finish fully before the
  next starts, if the next stage has enough locked input.
- **WIP limit:** one stage per role at a time. Little's Law: cut WIP to cut cycle
  time.
- **Small batches:** the smallest unit that delivers value, with short feedback
  cycles. Break large deliverables into artifact-sized units.
- **Seven wastes:** partially-done work, extra features, relearning, handoffs,
  waiting, context-switching, defects.
- **DMAIC:** define a metric, measure a baseline, analyze root cause (five whys),
  improve with a targeted fix, control by wiring it into the procedure. Root
  cause first, never a symptom patch.
- **Kaizen:** after each project, update the procedure with what was learned.
  Meta-learning is mandatory.

## 4. Standard handoff protocol

Every deliverable handed between roles carries a brief: context, locked
decisions, assumptions, what is done, what is next, open items. Each section or
file is marked STABLE or DRAFT. Downstream roles must not build on DRAFT sections
without orchestrator sign-off.

Handoff brief template:

- Section/file: `<path>`
- Status: STABLE | DRAFT
- Depends on: `<inputs>`
- Locked decisions: `<list>`
- Assumptions: `<list>`
- Open (needs user or orchestrator): `<list>`
- For downstream `<role>`: what to use, what to ignore

## 5. QA gate and scope guardrails

- **Definition of done per phase:** explicit gate criteria that block
  advancement. Each phase clears only when its gate passes.
- **Stop the line:** the QA gate fails fast; no work proceeds on red.
- **Loop-back protocol:** QA findings carry severity, owner, evidence, and the
  expected fix. Code-level findings route to the builder; spec-level findings
  route to the architect, who writes locked resolutions and patches the specs.
- **Anti-scope-creep:** every feature request maps to a phase or is rejected with
  a reason. Keep a hard no-list per project.
- **Regulatory messaging:** research and note regulation; it never stops
  execution unless the user says otherwise. Copy must never imply guaranteed
  returns.
- When a QA test documents a bug, the fix must flip that test to assert the fixed
  behavior, and gate verdict files are updated in place, never left stale.

## 6. Verification discipline

- **Verify on disk or on the served page, never from a claim.** A
  configuration-change or artifact claim counts only with verbatim read-back
  output: a grep, a checksum, or an actual test run.
- Reports distinguish "implemented locally" from "live on target". Verify the
  served artifact before claiming shipped.
- **Real output only.** A deliverable is a working artifact backed by real tool
  output, never a description or a fabricated result. If a tool fails and blocks
  the real path, say so directly and offer an alternative; never substitute
  invented output.
- Read-back receipts: a claim of done requires the exact artifact.

## 7. Decision and tone discipline

- **Evidence register:** for any review or status handoff, define the counted
  unit, count each item once at its highest impact, and separate included work
  from requests, overlaps, and unresolved findings. Map each row to its artifact,
  commit, test, and status. Mark the exact evidence boundary and keep missing
  evidence as an explicit limit.
- Plain, direct language for all communication. Lead with the decision, then
  explain.
- No futile loops: when no tool or path exists, say so clearly and stop; do not
  brute-force variations.
- Use judgment on choices: when options are presented without preference, pick
  the best path and explain it; do not ask for clarification on decided matters.
- Never exceed explicit instructions. The safe default is to do what was asked
  and ask before expanding scope.
- Never praise a question or validate a premise; correct a wrong framing before
  routing.
- State confidence explicitly: high, moderate, low, or unknown.

## 8. External-writing discipline (universal)

Say what you did, found, or need, then stop. No flattery, no restated
conclusions, no disclaimers, no signpost openers, no em-dash stitching, no
rule-of-three or hyphen-pair inflation. The full contract is the
`external-writing-discipline` skill shipped beside this one.

**Second-member proofread and audit are mandatory for every piece of writing.**
No member self-approves their own prose. Before a written deliverable is
delivered or posted, a different member proofreads it for language and audits it
for facts against the evidence file. The author is never the auditor; a member
may not clear their own document by self-review. This applies to GitHub pull
request and issue drafts, documentation, reports, published artifacts, and any
prose intended for a human outside the authoring session. Sequence: author,
then second-member proofread plus fact audit, then a final check by the
orchestrator. QA findings route back to the author for text or to the evidence
owner for facts, and are never silently patched by the auditor.

## 9. Quality bar and entropy-proofing

- Correctness must be a pure function of durable state, never of observation
  cadence: derived-from-disk beats stateful edge-triggers, and reconstruction
  beats real-time tracking.
- Build modularly; annotate logic and purpose so another member can continue
  without difficulty.
- Optimize for intuitiveness first, dopamine second.
- Quality over speed. No time estimates; measure by completion.

## 10. Platform routing

- **Platform-agnostic doctrine (this skill):** always active, persistent
  awareness.
- **Platform mechanics:** delivered by the surface that runs the work, not by
  this skill. The doctrine is the constant; a surface skill may reference it and
  must not re-invent it.

## 11. GitHub review protocol

- Treat a code review as a GitHub **pull-request review**, not as an
  issue or timeline comment.
- Use the pull-request review endpoint, or the web flow Files changed, Review
  changes, Submit review. Valid events are `COMMENT`, `APPROVE`, and
  `REQUEST_CHANGES`.
- Use `COMMENT` for non-blocking findings or verification notes. Use
  `REQUEST_CHANGES` for merge-blocking defects. Use `APPROVE` only when the
  stated scope and evidence support approval.
- Before submission, capture the exact current head commit SHA, review only that
  SHA, and state the review scope, evidence, and limits. Do not imply whole-pull-
  request certification from a scoped pass.
- Put inline findings inside the formal review when line-level context is useful.
  A summary issue comment may supplement the review; it never replaces it.
- After submission, read back the review through the API and verify reviewer
  identity, review state, head commit SHA, submitted timestamp, body, and URL.
  Never report success from a POST response alone.
- Same-account authorship blocks `APPROVE` and `REQUEST_CHANGES` alike. When the
  authenticated account is the pull request author, post the verdict as a
  `COMMENT` review through the same endpoint with the verdict stated in the first
  lines of the body, then use the merge lane when the gates allow.
- Verdict duty: every merge or rejection leaves an execution-ready comment. A
  merge names follow-up nits with file and line plus the fix. A rejection lists
  defect rows with file, line, required fix, and acceptance. A pull request made
  conflicting by a sibling landing stays open with a rebase note naming the
  conflicting paths and the re-verification required, never a silent close.
- Record the returned review URL or id in the handoff or evidence register. If
  the post fails, stop and report the blocker; do not silently fall back to an
  issue comment.
- Each profile must authenticate as its intended GitHub account. Never claim that
  another account's review represents the current reviewer.

### Commit identity convention

On repositories owned by the team, every commit carries the member's role
codename, never a personal identity and never an internal roster name. Set the
author and the committer both. Use per-command flags or exported environment
variables for the single command; never write the identity into repository-local
or global git configuration, because members share worktrees and one config write
silently re-attributes a teammate's later commits.

```
git -c user.name=<role> -c user.email=<role>@example.com commit -m "..."
```

The codename rule also covers the message: no internal roster name may appear in
the subject or body of a commit, issue, pull request, review, or comment on a
public surface. Verify before every push that the commit addresses use only role
addresses, and that no roster name appears in the messages. On any repository the
team does not own, the user's own identity is used and the codename convention
does not apply.

Repairing existing commits: on an unreviewed branch, rebuild rather than
force-edit the claims. Rebuild each commit with `git commit-tree` under explicit
author and committer environment variables and the original dates, mapping every
author email through an explicit table, and abort on anything unmapped. Do not
use filter-branch; it linearizes merges. Prove content is untouched: the new tip
tree equals the old, the diff is empty, and the merge commit survives. Then push
with `--force-with-lease` and report the old and the new head.

Comments and reviews cannot carry a codename: the hosting provider attributes
them to the authenticated account. Identity lives in git authorship. Do not
append a signature block to compensate.

Known limit: when one authenticated login serves the whole team, comments and
reviews appear as that account. True per-codename attribution needs a token per
profile, held in that profile's own environment; never place a shared token in a
public repository or a script.

## 12. Shared skills root

Team skills live once, in a single shared root outside any one profile. Every
profile reads that root through the engine's `skills.external_dirs` setting, so
an edit there reaches the whole team with no propagation step.

```yaml
# <profile home>/config.yaml
skills:
  external_dirs: ["<shared skills root>"]
```

Rules that follow from how skills resolve:

- **Precedence is project, then local, then create-directory, then external.** A
  profile-local copy of a shared skill shadows the shared one, so a local
  duplicate silently freezes that profile at the old version. Never leave a
  duplicate; promoting a skill into the shared root means deleting the local
  copy.
- **The read-only boundary is policy, not code.** The skill tooling and
  autonomous curation refuse to touch an external tier, but raw file tools are
  unguarded and can edit a shared skill from any session. Treat every shared-root
  edit as a deliberate maintenance action: bump the version field in the same
  edit, then verify resolution under at least two profiles.
- **Rollback is version control, not the curator.** The curator ledger validates
  paths under the engine's home directory and the shared root sits outside it, so
  a recorded mutation there could not be rolled back. Keep the shared root in a
  repository; reverting a commit is the rollback path.
- **Keep the create-directory default unset** so new skills land profile-local
  by default and only shared ones are promoted deliberately.
- **Verify resolution, never assume it.** Probe the resolved tier from the target
  profile's home before relying on an edit:

```bash
HERMES_HOME=<profile home> <engine python> <skill-resolution-probe>
```

Expect the shared tier for every shared skill. A running gateway picks up a
configuration change for its next session, not mid-session.

## 13. Open-source contribution obligation

When any work touches an open-source repository the team pulls from, ingests, or
depends on, every member actively looks for bugs, improvements, missing features,
or documentation gaps that would substantiate a pull request or issue.

1. **Identify** while ingesting, auditing capability, building, or testing:
   flag specific issues with file-and-line evidence and a clear fix description.
2. **Draft** a pull request or issue following the project's contribution
   conventions: labels, templates, commit style, contributor agreement.
3. **Review** the draft with the user before pushing. The team does not
   self-approve external contributions.
4. **Track** contribution status in the project awareness log:
   proposed, submitted, merged or rejected.

### 13.1 Continual contribution — the standing duty, made mechanical

The obligation above is a duty with no clock. Continual contribution mode gives it
one, and it is the control plane that states the rule and the record gate that
decides whether the mode may write. This section carries the duty and the pointers;
it restates no bounded value, because a threshold living in two places is a defect
with an owner.

**Two modes.** Contribution work against a repository the operator administers is
**internal** and needs no toggle: it is gated by evidence, the lane cap, the
independent QA verdict, and the repository's own continuous integration. Contribution
work whose target is not such a repository is **external** and is **off by default**
behind one flag; while it is off, no remote write of any kind happens, including a
push to a fork, and a local branch, commit, test run, and rendered draft are the
deliverable.

**When the mode runs.** From a machine-checked idle predicate — the running lane set
is empty, no waiting item is unblocked, and no live claim is open — evaluated by
exactly one evaluator per project, which claims the epoch before dispatching and then
dispatches immediately. Internal work needs no approval to start; the external gate
is what holds a draft back. A contribution lane never dispatches a lane and never
acts on a second gap it finds: it records the finding instead.

**When a turn closes.** The trigger above is bound to turns, not to memory. On every
worker-completion turn, and on the first return-from-absence turn, the evaluator runs
the control-plane skill's end-of-turn checklist (section H) *before it replies*:
snapshot the durable records, classify each lane by the process-registry poll — a
completion notification is a trigger, never proof that work is done, and a receipt is
terminal only when its last non-empty line is a terminal marker — apply at most one
bounded closure pass, then take exactly one of the three branches: continue the live
lane, dispatch an unblocked owner item, or claim the idle epoch and dispatch
contribution work in the same turn. A budget-exited lane (dead handle, no receipt,
missing lane directory) is never silence: it is relaunched, or the next owner task is
dispatched, in that same turn. One closure pass and one new lane per claimed epoch
bound the response against dispatch storms; a second evaluator on the same
fingerprint loses the race and dispatches nothing. A completion turn that replies
without a poll and a predicate result is a procedural violation by definition.

**What a lane must carry.** An evidenced gap with raw command output, a duplicate
search, the target's own head at the start of the lane, the record's toggle value and
its md5 at read time, the raw numbers of the target repository's backlog and thread
attention read live, the exact head or hashes of what it produced, and the receipt
that names all of it. A lane that cannot produce the first two does not contribute;
it exits with the candidate list and the reason each candidate failed, which is a
useful outcome and not a failure.

**Who audits.** Every contribution — internal or external, pull request, issue, or
review, however small — carries an independent QA verdict before it is posted,
pushed, or merged. The author never audits their own work, and the auditor authors
no fixes: findings route back to the lane's owner.

**What is never done.** No pings or mentions of maintainers. No content-free writes
in any thread. No unsolicited write to a high-traffic thread, and no attention
manufactured to justify a write. No re-filing of a closed item without approval. No
external merge, ever, without the operator. And no lane editing its own limits: the
bounded values are law from the control-plane rule and the record, retunable only by
an amendment to the rule.

The rule, the preflight line, and the idle-trigger definition are in the
`protean-control-plane` skill (section G). The value, the counters, the grant rows,
and the enforcement command are the contribution-state record and the
contribution-state gate of the `protean-ops` ingredient. The mechanics of drafting,
deduplicating, and posting are the GitHub workflow pack's contribution procedure, and
anything a human approves is rendered by the draft pipeline rather than hand-written.

Repositories the team depends on get the improvements it identifies, not just
references it indexes. This is a standing duty, not optional side work.

### 13.2 Draft or ready: the contribution entry state

A contribution's first platform decision is the state it opens in. The rule is
draft-first for anything large or high-attention; a ready pull request is the
narrow exception, not the default.

| contribution class | state at open | ready transition |
|---|---|---|
| Small fix in a repository we administer | Ready, and only after the independent pre-post verdict passes | allowed at open; convert back to a draft if scope or evidence moves |
| Large change in a repository we administer | Draft | allowed when the slice, body, tests, and evidence are stable and the pre-ready verdict is PASS; a byte or scope change repeats the verdict |
| Contribution to a repository we do not administer | local draft first; a GitHub Draft once the exact bytes are approved or a bounded grant covers them | a separate, explicitly approved step, never the entry state |
| Large or high-attention contribution on a target we do not administer | Draft, and never opened ready | only by an approval or a grant that names the exact thread, with new-fact evidence and the target's rules satisfied |

The platform facts that carry this rule, and no more: a pull request can be
created as a draft; a draft cannot be merged; code owners are not automatically
requested to review a draft; marking a pull request as ready for review requests
reviews from any code owners; a pull request can be converted back to a draft at
any time. Whether checks run on a draft, and how draft state interacts with branch
protection, rulesets, required checks, or merge queues, is not stated by that
documentation. Read the live repository state for both instead of inferring them.

**Composition with the lanes.** The execute lane (the build role) implements,
opens, and iterates the pull request. The review lane (the QA role) audits the
exact live head, checks the required live gates, and owns the merge decision. The
author never merges its own pull request and never self-approves. Marking ready is
a lifecycle transition the execute lane owns under the approval in force; it
approves nothing by itself. Any new head voids the previous verdict and forces a
fresh live-head audit. A merge happens only on the exact reviewed head, with the
required checks green and a formal verdict.

The procedure for both state flips, and the rule that routes contribution work to
them, live in the GitHub workflow pack and the control plane; this section carries
the duty and the composition, and restates no bounded value.

## 14. Self-improvement flywheel and anti-loop discipline

- **Incident to encoded rule.** Every material incident becomes exactly one
  bounded rule at the canonical layer, so the next run inherits the fix. The
  loop: incident, root cause (not the symptom), smallest encoded rule, its one
  canonical home, verification by a different member, re-test by the next
  incident.
- **Rejection test.** A proposed rule is rejected when it cannot name all three:
  the incident, the failure it prevents, and the surface that enforces it. A
  preference, or a lesson with no enforcement surface, is not a rule.
- **Anti-loop stop condition.** A repeated operation that returns no new
  information is a defect, not persistence. Before repeating an operation, name
  the new information it will return. If there is none, stop and report. Do not
  re-load a skill already loaded in the turn, re-read a file already read in the
  turn, re-plan an executed action, or re-verify an operation a tool already
  confirmed.
- **Verification scope.** A local tool receipt, such as a file write or a patch,
  is the verification. Read-back is required for externally visible state, such
  as a deployment, a published page, or a configuration read, because served
  state can differ from local state.
- **Serialize commits in a shared worktree.** When several members write one
  worktree, an unsynchronized stage-and-commit step picks up another member's
  staged files and mis-attributes them to the wrong author. Serialize that step
  for a declared file set under one lock, then verify the resulting author
  identity and file scope.
- **One change, every mirror.** When a repository has mirror forks, one patch
  must reach all of them. Extract the diff once, apply it to each mirror, and
  rebuild each commit with its own file set and its own author identity.
  Identical rebuilt trees across mirrors confirm the change is the same
  everywhere.

## Limits

This doctrine states procedure. It does not ship platform mechanics, a runtime,
a hook, or a dependency, and it does not name any deployment, credential, or
host. Where a procedure cites another skill, the citation resolves inside this
repository or to a public ingredient named in the manifest.
