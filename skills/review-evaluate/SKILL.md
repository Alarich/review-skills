---
name: review-evaluate
description: Compare review skills, delegation modes, harnesses, or model routes against frozen cases. Run matched trials, audit delivery and usage, grade individual claims, and produce an evidence-linked evaluation.
---

# Evaluate review workflows

Find what the user wants to compare, the allowable models and runtime, and
which behavior counts as an improvement. Benchmark in fresh sessions.
For a change to testing methodology, delegate an independent review of the
existing evidence first. Keep its findings and the verified corrections.

Use [the evaluation workflow](references/evaluation.md) to prepare cases,
record reusable target references, freeze the test matrix and decide how
to score it. Take target locations and the runner from the caller or the
evaluation workspace. Hold source, tools,
priority rubric, and delivery instructions constant under a matched
comparison. Treat differences in finding eligibility as part of the tested configuration.
When estimating the effect of distributing work, compare one reviewer
performing all three investigation methods with three independent reviewers
performing one method each. Pin the same method instructions for both arms. State which other instructions changed.

Use actual host events to verify fresh reviewer context, independent starts,
completed submissions and handoffs. Check the provider response identity and reconcile token
usage. Preserve each failed attempt and its reason. Read the evidence
before accepting a result, retrying or promoting a candidate.

Keep a verified issue inventory for each frozen case. Independently
confirm new defects, merge equivalent mechanisms and rescore all earlier
reports on that case against the expanded inventory. Show the original
oracle score and current inventory score together. Track partial proof,
missed issue IDs, priority, and standalone test gaps.

Deliver an HTML report locally when requested. Start with the decision, then show
what changed, which individual findings or errors changed, and how much
each route cost. Link to exact report lines and checks. Report reference
coverage, supported additional defects, unsupported claims, priority
errors and test gaps separately. Show successful-run costs and the
observed costs of obtaining a successful result.

Log to a tracking service only when the destination and permitted data are authorized. Otherwise keep evaluation artifacts local.
For MLflow, use the [tracking workflow](references/evaluation.md#track-in-mlflow)
to connect scoreable reports to their audited executions.

Carry forward the caller's end-stage tasks and complete the
[completion checklist](references/evaluation.md#completion-checklist).
