# Writing and checks

Use the evaluator's [reference](skills/review-evaluate/references/evaluation.md)
as the style example. Wrap source lines at 80 columns or less.
This limit applies to repository documentation and skill files.
Keep a paragraph focused on one instruction or decision. Use a short list
for fields or explanations that need more room than a table row. Keep exact
links and fenced examples copyable. Put long YAML descriptions in folded
block scalars using the proper indentation.

After editing, run these checks from the repository root.

```bash
markdownlint-cli2
yamllint . .yamllint
for skill in skills/*/SKILL.md; do
  sed -n '2,/^---$/{ /^---$/d; p; }' "$skill" | yamllint -
done
```
