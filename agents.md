# agents.md — Main Router

## Purpose
This is the first file the Builder reads every sprint. It defines the operating model, reading order, and non-negotiable workflow rules.

## Project Identity
- **Project:** TakeMeter — Fine-Tuned Discourse Quality Classifier
- **Course:** AI201 | Applications of AI Engineering
- **Type:** Fine-tuning pipeline — Google Colab + GitHub repo (no local app)
- **Repo name:** ai201-project3-takemeter (create fresh — no fork)

## Reading Order (Builder reads in this sequence before every sprint)
1. `agents.md` (this file)
2. `docs/architecture.md`
3. `docs/data-model.md`
4. `docs/label-taxonomy.md`
5. `docs/evaluation-plan.md`
6. `planning/state.md`
7. `planning/decisions.md`
8. `planning/risks.md`
9. Current sprint: `sprints/sprint-N/requirements.md` → `blueprint.md` → `acceptance.md`

## Builder Rules (Non-Negotiable)
- DO NOT write planning.md or README.md until the human has completed the prior sprint's human tasks (community choice, annotation, etc.).
- DO NOT design labels from memory — labels must be grounded in real posts from the chosen community.
- DO NOT pre-split the CSV into train/val/test — the Colab notebook handles splitting automatically (70/15/15).
- DO NOT commit the Groq API key to GitHub under any circumstances.
- The CSV must have at minimum two columns: `text` and `label`. A third `notes` column for difficult cases is recommended.
- No single label may account for more than 70% of the dataset — flag this if detected.
- All output files from Colab (`evaluation_results.json`, `confusion_matrix.png`) must be downloaded and committed to the repo.
- After each sprint, update `planning/state.md`.
- If a contradiction is found between files, STOP and flag it — do not resolve silently.

## Workflow Per Sprint
1. Read all files in reading order above.
2. Read current sprint Architect Pack (requirements → blueprint → acceptance).
3. Produce Dry Run Summary: what is being built, what is OUT OF SCOPE, any ambiguities found.
4. Wait for Architect approval.
5. Execute only what is in scope for this sprint.
