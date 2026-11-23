# Run a repeatable evaluation

## Set up

1. Choose one comparison axis and a matched baseline. Freeze source,
   requirements, case reference answers, tools, rubric, prompt snapshots,
   model selectors and expected response identities. A single supplied
   target supports a case-specific comparison. To test transfer, include
   a production-defect case and an untouched verification case. A clean
   or mixed case can test unsupported findings. Verify oracle witnesses
   independently when available.
2. Decide the consequence of a missed high-impact defect, what severity
   needs supporting operational evidence, and the acceptable additional
   cost. Treat one run per configuration as an observation. Repeat on
   the same case to estimate variability, and use another case for
   transfer. Keep development and transfer scores visible separately.
3. Assign random report labels before handing reports to a judge. Provide
   the labels, case and independent oracle. Withhold the label key,
   model, mode and run history. Preserve one verdict per diagnostic
   assertion with the report line and the validating source or witness.
   Use the verdict values in **Run**. Track priority, duplicate
   mechanisms and test-only gaps independently.

## Record a reusable review target

Give each example a stable case ID. Store its manifest in the evaluation
workspace, outside reviewer-visible source. Point every arm at that case
ID and an exact manifest digest. Use these fields or their equivalents:

| Field | What to pin |
| --- | --- |
| Case ID and role | A stable label and whether it is a development, clean-control, or held-out example. |
| Source locator | A retrievable immutable source, such as a repository with retained objects, an artifact identified by digest, or archived source bytes. Use a path relative to the evaluation root when the files travel with the campaign. |
| Compared states | Git base and head commit IDs for a revision or PR. For local changes, pin the comparison base and checkout HEAD, then archive the staged and unstaged diffs and relevant untracked files. For a plain folder, archive the scoped files and list their paths and content hashes. Preserve file modes, symlinks and dependency contents when they affect the reviewed snapshot. |
| Scope and requirements | Included paths, exclusions, and pinned requirement or test references. Record what the reviewer can actually see. |
| Integrity and replay | Hash the manifest and archived inputs. Record how to reconstruct the copy and recheck the hash before each run. |
| Independent checks | In a separate grader-only record, list reference issue IDs, source coordinates, witness locations and digests, and how to rerun each witness. |

Record the case ID, manifest location and digest in every trial record.
Verify the archived inputs and compare the materialized reviewer-visible
tree, requirements and scope with the manifest before each run. Recheck
the same inputs afterward. Any change to them requires a new manifest
identity.

Cite evidence as `case:<id>@<revision>:<relative-path>:<line>`. Use the
base revision for deleted lines and the head revision for added lines.
For a folder or dirty worktree, use the digest and coordinates of the exact archived state, including staged or baseline preimages and the previous path for removed or renamed lines. Give each citation an exact link to the pinned source or
archived copy when available. Point executed checks to the saved witness
and result. In the report, link the case ID to its manifest so another
evaluator can reconstruct the target. Use relative links for artifacts in
the bundle and immutable locators for external evidence. Keep case names,
locators, oracle data and report artifacts in their evaluation workspace.

## Run

Use the launch adapter supplied by the evaluation workspace or caller.
Map its parameters to the case ID and manifest, skill configuration,
model route, repeat, allowed tools, and output location. When no adapter
is supplied, use the available host to start fresh sessions with those
same inputs and save a trial record for each attempt. Mark comparisons
unqualified where the host cannot verify the required delivery or model
identity. Mark usage or pricing unavailable when it cannot be verified.
Use a new campaign directory and a versioned skill snapshot per cycle.
Freeze or counterbalance launch order across comparable arms. Record order
and cache conditions, including shared provider cache when observable.
Before contacting the host, persist the campaign, case, arm, repeat and
attempt IDs and the input digests. Associate returned host IDs with that
record. Pass a searchable attempt ID to the host if it supports one, or
save a durable host receipt. Before starting paid work, prefer a correlation
or idempotency key recoverable from the host after interruption. Record the
actual effective target, baseline, scope, request, skill snapshot and granted
tools. Preserve commands, selectors and response identities,
permission scopes, isolated briefs, request and handoff traces, reports,
and qualification receipts. Keep token counts when a verified price is
unavailable.

For an independent-review arm, use the current host's delegation tool
with its empty-history option or documented fresh-task mode. Pass a
self-contained brief. Verify the recorded launch options and reviewer
history for inherited conversation, tool calls, or outputs before
accepting the arm. An independent reviewer ID verifies delegation alone.
Preserve an inherited-context attempt as diagnostic evidence and exclude
it from the fresh-context comparison.

Retry only eligible missing or incomplete arms under the same frozen
configuration. Reconcile a pending attempt with host records before
relaunching it. If launch acceptance cannot be determined, retain an
unknown-submission state. Reconcile it before rerunning unless the frozen
budget and user authorization cover a possible duplicate. Carry forward
any unknown spend. Preserve every attempt, skill snapshot and launch adapter.
Replay archived verification before paying for another model request and
disclose any attempt whose outcome or usage cannot be recovered.
Freeze the finite attempt and time budgets, qualification cutoff, and
selection rule with the test matrix before the first launch. Reuse them on resume. A useful default is the
earliest eligible qualifying attempt in the planned sequence. Preserve
other qualified attempts and their costs.

Before launching, freeze a reference plan with the batch. Its
`reference_ids` list identifies independently verified scenarios. Its
`witnesses` list records each evidence path relative to the artifact
directory and its digest. Leave both lists empty when the case has only
a retrospective inventory. Keep the evidence outside candidate briefs.
For a follow-up campaign, pin prior verified issues with their archived
evidence as a separate comparison set. Preserve the independent witness
score so the prior issue pool does not stand in for an independent oracle.

Once a batch qualifies, mask report copies and keep the label key and
masked-to-original line map private. Remove route-only metadata before
numbering the judge-facing copies. Check the complete judge-visible packet for arm identifiers,
including roster counts, completion metadata, method headings, reviewer
attribution, report prose, code blocks, command arguments, working
directories and linked artifact contents. Keep exact delivery metadata
in the separate audit. Keep proof and line mappings intact using
neutral aliases for identical evidence. Verify their digests. Withhold any
evidence whose identifying content cannot be masked without losing proof
and mark dependent results unavailable. Give the judge the masked copies,
read-only access to the verified target and requirements, and any grader-only witnesses. Keep
the key and route history closed until adjudication is saved. For each anonymous label,
bind its masked digest to one qualified attempt and original report
digest. Verify the masked copy and its line mapping against the original.
Check witness readability and digests before grading or replay. If evidence
is unavailable, keep the planned denominator, record the affected report
and issue with the reason, and mark dependent scores unavailable. Give a fresh judge the same
input packet without any previous verdict outputs.
Writer style and phrasing may still hint at the route.

If a route is deferred, prepare a separate packet of completed arms only
when an interim evaluation is useful. Label it provisional and keep the individual
failed-attempt costs. Deliver the matched comparison locally after every
planned slot has qualified or reached its cutoff. Mark missing slots and
compare report quality on qualified matched slots. Show first-attempt
and within-budget delivery against all planned slots, with all known
attempt costs. Report both selected qualified-attempt costs and the
campaign's observed spend per delivered slot, including metered spend
on cutoff and failed slots in the latter numerator. State the counts
of planned and delivered slots and unpriced attempts. When zero slots
deliver, show spend per delivered slot as unavailable and retain known
total spend. Use a fresh masked backmatch when a later arm proves another issue.

Save the adjudicator's judgment as `verdicts.json` inside the masked directory.
Use `reference_ids` and one `reports` entry per anonymous label. Each
entry has a `claims` list. A claim has `line`, `claim`, `evidence`,
`kind` (production, test-gap, decision, maintenance), and `verdict`
(supported, partial, unsupported, uncertain, duplicate).
When applicable add `reference` for a predeclared ID, and
`reported_priority` and `supported_priorities` for the published finding.
Use an optional `issue` ID for a later discovery. Set `line` to the findings
table row or standalone finding heading where the finding is published.
Use that same line for every atomic claim from the finding. When proof
appears separately, match it by finding ID and cite its location in
`evidence` alongside the validating source or witness. Use judge-facing
report lines in the verdict and validate the mapping to original lines
before scoring. Explain any report tally mismatch with
`tally_reconciliation` after reading the published findings.
Reconcile the verdict list against every material assertion in the report.
A finding tally can reconcile grouping and formatting differences. Each
material assertion still needs its own verdict.
Full credit requires a supported claim with an actionable trigger,
consequence and evidence. Record relevant incomplete proof separately.
For original oracle coverage, use the reference IDs in the immutable
reference plan bound to that packet. When that plan has no independent
oracle, show its oracle coverage as unavailable and give the verified
inventory coverage. For a zero denominator,
report coverage as unavailable and still show claim counts.
Validate references and report hashes, unmask the judgments, and
calculate per-arm coverage, errors, token categories and costs.

## Recalculate issue coverage

Build `verified-issues.json` in `CAMPAIGN/CASE` from the independent
oracle and all verified report discoveries for that case. Add a new
issue only when evidence establishes an actionable trigger, mechanism,
observable consequence and correction. Keep independently actionable
consequences distinct even when they share a cause or correction. Merge
reports of the same failure and consequence. Keep test gaps, decisions and
maintenance issues in their own coverage counts. Backmatch every earlier
and later report with the same frozen case manifest digest, including
requirements and scope. Reverify applicability before carrying a prior
issue to a different manifest, and retain separate inventories and scores.
Save the judge's matches in masked coordinates. After adjudication is
saved, verify the binding and translate matched lines to the originals.

The inventory contains an `issues` list and a `reports` object. Each
issue contains `id`, `kind`, `title`, `trigger`, `consequence`, `evidence`,
`priority`, and `first_cycle`. `reports` is keyed by the masked directory
name and then the anonymous report label. Use a unique packet name when
combining judgments from different campaigns, and preserve each label's
attempt and report digest binding. Bind each packet to its frozen reference
plan and its digest. Each report entry has `found` and `partial` mappings
from issue ID to original report lines and an `unavailable` mapping from
affected issue IDs to evidence or access reasons. Preserve the planned
denominator and keep unavailable items out of definitive misses. An older
inventory without availability metadata needs its evidence and verdicts
rechecked when availability is uncertain. Keep the key hidden while
adjudicating these matches.

Verify that every qualified report was scored. Include the production numerator and
current denominator, independent oracle score, exact missed issues, and
partial proof. An earlier 6/6 becomes 6/7 when a later report proves a
seventh issue and the earlier one missed it. Save an inventory snapshot
when adding issues so earlier and updated scores are reproducible. For
real changes without a complete oracle, describe the denominator as all
verified issues discovered to date on that frozen case.

The reviewer sees the case and skill. Supply the frozen status and diff
for Git cases, or the archived file inventory and no-Git-baseline statement
for plain-folder cases. Use
inspection tools with no unrestricted shell. Keep scoring inputs and
other results out of the review brief. Scoped tool arguments are
audited, but the path audit does not guarantee operating-system
isolation. Escalate the isolation method when the task needs a strict
access boundary.

## Compare

- Qualify only when the recorded effective target, baseline, scope,
  request, skill and tool permissions match the frozen attempt. Check the
  expected reviewer identities, assignments and final handoffs, unchanged
  inputs, response identities and material scope completion. Preserve
  incomplete attempts and costs outside matched report quality scores.
- Verify the current report artifact and the required chat content,
  including the correct report link, tally, findings, material gaps and
  decisions. Record any file or chat delivery failure with the attempt.
  Reconcile token usage before reporting token or cost comparisons.
- Match every reference mechanism at most once by trigger, cause and
  observable consequence. Give separate credit to additional supported
  findings and to material counterfactual test gaps. Show factual
  errors and urgency disagreements beside those gains.
- Compare costs and elapsed time per route and case. Track fresh
  input, cached input, cache writes, output and reasoning within output.
  State the price schedule. Compare model routes as configured, with
  requested and observed effort disclosed. Only price an estimate when
  the actual response model and cache accounting match a known schedule.
- After each cycle, name the actual prompt changes and record which
  evidence justified retaining or reverting each change. Show the
  strongest examples and losses before selecting the finalist. Preserve
  all qualifications, adjudications, oracles and exact prompts.

Use a host-specific launch adapter when handoff events or reviewer
rosters differ. Match source pins, independent grading and cost evidence
across those arms. For meaningful differences, trace confirmed issues
from publication back through the reviewer handoff and the inspection
that produced it. Compare lookup tools, handoff and approval behavior,
and metered coordinator and reviewer usage. Distinguish a divergence
observed in the trace from a claim about what caused it. Use a separate
matched check when attributing the difference to a single host behavior.
A campaign may use its own HTML renderer.

## Track in MLflow

Use an authorized tracking destination and the workspace's adapter.
Confirm which data may be sent. Minimize or redact private prompts, source
and reports before sending them. Keep omitted evidence in authorized local
storage and mark dependent metrics unavailable.
Give each attempt a stable run identifier. Log its case and manifest
digest, arm, repeat, response model, delivery status, token categories,
and cost. Persist the attempt-to-run mapping and recover an existing run
by that identifier after interruption. Keep failed attempts in the campaign
and count metered retry costs once. Preserve the report and qualification
receipt. Check the expected attempt and score records against the tracker
before marking the campaign complete.

For a report-scoring trace, use the authorized portions of the review
request and report. Compute exact-artifact scores against the protected
original locally when a remote copy has been redacted. Link it to the execution trace and exact report digest. Attach
independently witnessed defect mechanisms as expectations after the
attempt closes. Keep the linked trace and route data outside blind
adjudication. Join the identities after the blind verdict is saved.
A tool-use score needs actual tool calls, and a retrieval score needs an
actual retrieval stage. Record insufficient inputs as unavailable.
Exclude unqualified attempts from report scoring.

Replay blind adjudication as separate coverage, unsupported-claim, and
priority-disagreement scores. Verify each input report against its graded
digest. Link the scores to the exact verdict and inventory snapshots and
record the manifest digest, numerator and denominator for each basis.
Use each packet's frozen reference plan for its original witness score.
Honor saved unavailability during replay. Report witness, verified inventory,
and partial coverage separately.
Before expanding a model judge, pin its prompt and settings and verify
each intended metric on a known positive and negative. Keep scores outside
the comparison if the judge misses that gate. Record judge scope, errors,
model, and cost separately from review execution.

## Completion checklist

Carry this list into the campaign record. Add any tasks the caller gives
you and save evidence for each completed item.

- [ ] When creating or revising the evaluator, exercise the full workflow
  with the revised skill against a frozen snapshot of itself. Compare
  one broad reviewer, one reviewer using all three investigation methods,
  and three independent reviewers using one method each. Supply the
  one-reviewer three-method variant as a frozen comparison configuration.
  Record each arm's verified delivery, findings and grading. Run this self-check
  once for the revised snapshot. Treat nested trials as evidence for it.
- [ ] For a transfer claim, run a matched comparison on fresh, independent
  changes the evaluated instructions were never tuned on. Prefer changes
  from two unrelated projects where available. Record each target by its
  case manifest and report which quality and cost differences transfer.
- [ ] Regrade earlier reports against every newly verified issue on the
  same frozen case. Include both reference and current issue coverage,
  with linked proof, false reports, priority errors and cost.
- [ ] Complete the caller's additional end-stage tasks and record any
  limits on the evidence, including deferred or unqualified trials.
