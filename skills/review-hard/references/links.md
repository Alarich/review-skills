# Evidence links

Use the smallest set of inspected references that establishes each finding.
Explain what each reference proves: the problematic code, the caller exposing
it, and the requirement, test, or contract establishing expected behavior. A
supplied URL alone does not establish its contents.

## Local source

In chat and in the Markdown report, label a local code link with the filename
and line. Use the inspected absolute path and line as its destination.
Example: `[pay.ts:81](/home/example/project/src/orders/pay.ts:81)`. If the
path contains spaces, wrap the destination in angle brackets. Use plain paths
with a line number for local files, and preserve line anchors on web and
GitHub PR links.

Verify that the cited location contains the referenced code. Refresh moved
lines or identify the reviewed older revision. For missing behavior, cite the
production location where it belongs. For deleted code use a base-revision
permalink or an isolated base copy rather than a link to a missing
working-tree file.

## GitHub pull requests

Record the PR URL, reviewed head, target and merge-base in the summary. For a
GitHub CLI export, take file coordinates from the unified diff hunk headers.
Retain the inspected revision, path, side and line or range. RIGHT uses
new-side lines and LEFT uses old-side lines. Preserve the old evidence path
for renames and deletions.

Use an exact link to the evidence line. The posting location is a separate
choice. Verify the proposed inline path, side and range against the reviewed
diff. Prefer the verified Files changed URL. When the faulty code is outside
the diff, cite its immutable commit line as evidence and use the changed
caller for placement if it makes the finding relevant. Keep the verified
coordinates even when a Files changed URL is unavailable. In that case use an
immutable commit-and-line link when available and say that the PR line URL is
unavailable. For a bare dump, retain the supported coordinates and link the
saved patch if available. Do not guess URLs. Mark a finding **PR summary** if
it has no verified inline location.

In each PR finding's proof section, retain the placement as `Inline —
path:line (LEFT|RIGHT)` or `PR summary` and provide a short copy-ready comment
with trigger, impact and action. If placement differs from the evidence
location, include the exact evidence link in the comment draft. The exact
placement and draft must be reusable from the report. If the head moves, treat
the placement as stale until rechecked. Keep the original evidence tied to its
reviewed revision. Publish only on separate authorization.

## External context and executed proof

Confluence, Jira, design decisions, and vendor documentation are first-class
evidence. Link the specific section, comment, or version when possible.
Include a short relevant excerpt or precise summary, retrieval time, and
version/updated information when exposed. Distinguish retrieved evidence from
inaccessible references and cite conflicting requirements separately.

For executed checks record command, working directory, relevant
input/environment, observed result and exit status in the report. Redact
secrets. Link extra captured output relative to the report only when needed;
verify it exists. For static findings label the proof as inspection rather
than implying a reproduction ran. Record commit identity for historical source
and snapshot time for local source; use hashes only when needed to distinguish
changing evidence.
