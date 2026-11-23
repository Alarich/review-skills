# Review Skills

Three skills for AI coding agents.

- `review` uses one independent reviewer.
- `review-hard` uses three independent reviewers for recovery, round trips, and interrupted workflows.
- `review-evaluate` compares review approaches on frozen cases.

Copy a skill's directory from `skills/` into a directory your agent loads, or invoke its `SKILL.md` by path. The review skills cover local changes, GitHub pull requests, and folder snapshots. They report P0–P3 findings with source links and evidence.
