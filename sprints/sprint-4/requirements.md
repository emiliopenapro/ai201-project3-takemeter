# Sprint 4 — Requirements

## What Is Being Built
The complete evaluation report in README.md, the spec reflection, AI usage section, and demo video.

## Scope
| In Scope                                              | Out of Scope           |
|-------------------------------------------------------|------------------------|
| Write README.md — all required sections               | Any further Colab work |
| Confusion matrix as markdown table in README          | Changing the model     |
| 3 wrong prediction analyses                           | Stretch features*      |
| Sample classifications table (3–5 posts)              |                        |
| Model reflection (intended vs. learned behavior)      |                        |
| Spec reflection                                       |                        |
| AI usage section (2+ instances)                       |                        |
| Record 3–5 min demo video                             |                        |

*Stretch features may be added after Sprint 4 core is complete, with planning.md updated first.

## Deliverables
1. `README.md` — all required sections complete
2. Demo video (3–5 min) recorded
3. Final git commit with all files

## Success Definition
README contains evaluation report with both models' metrics, confusion matrix as markdown table, 3 analyzed wrong predictions, sample classifications, and reflection. Demo video shows classifications with label + confidence visible.

---

# Sprint 4 — Blueprint

## Step 1: AI-Assisted Failure Analysis (Before writing)
1. Collect all wrong predictions from Colab Section 4 output
2. Paste into Claude with this prompt:
```
Here are misclassified posts from my text classifier. 
Each entry shows: post text, true label, predicted label.
[paste examples]

Identify any systematic patterns in these errors. 
Look for: similar post length, use of sarcasm, specific label pairs 
that keep getting confused, short or low-information posts, 
topic vs. structure mismatches.
```
3. **Verify every pattern yourself** by re-reading the examples
4. Discard any AI-identified pattern you can't confirm by eye
5. Include what you found AND what you had to correct/discard in the README

## Step 2: README Structure

### Required Sections

**Community and Labels**
- Community choice and reasoning
- Label taxonomy: definition + 2 examples per label

**Data**
- Collection source and process
- Label distribution (count per label)
- 3 difficult-to-label examples with your decisions

**Fine-Tuning Approach**
- Base model: distilbert-base-uncased
- Training setup: epochs, lr, batch size
- At least one hyperparameter decision you made

**Baseline**
- Prompt used (paste the actual prompt)
- How results were collected

**Evaluation Report**
- Overall accuracy: both models
- Per-class metrics table: both models (precision, recall, F1)
- Confusion matrix as markdown table (fine-tuned model):

```markdown
| True \ Predicted | analysis | hot_take | reaction |
|------------------|----------|----------|----------|
| analysis         |    X     |    X     |    X     |
| hot_take         |    X     |    X     |    X     |
| reaction         |    X     |    X     |    X     |
```

- 3 specific wrong predictions with analysis (use guiding questions from docs/evaluation-plan.md)

**Sample Classifications** (3–5 posts, markdown table)
```markdown
| Post (truncated) | Predicted Label | Confidence |
|------------------|-----------------|------------|
| "..."            | analysis        | 0.91       |
```
Include at least one sentence explaining why one correct prediction is reasonable.

**Reflection**
- What the model captured vs. what you intended (specific, not generic)
- What did it overfit to? What did it miss?

**Spec Reflection**
- One way the spec helped your implementation
- One way implementation diverged from spec and why

**AI Usage** (2+ instances)
- What you gave the AI tool as input
- What it produced
- What you changed or overrode
- Disclose any annotation assistance

## Step 3: Demo Video (3–5 minutes)
Show:
- [ ] 3–5 posts classified by fine-tuned model with label AND confidence visible
- [ ] One correct prediction narrated — explain why it's reasonable
- [ ] One incorrect prediction narrated — explain what went wrong
- [ ] Brief walkthrough of your evaluation report

---

# Sprint 4 — Acceptance Criteria

### AC-1: README
- [ ] Community + label taxonomy section complete
- [ ] Data section: source, process, distribution, 3 difficult cases
- [ ] Fine-tuning section: base model, training settings, 1 hyperparameter decision
- [ ] Baseline section: prompt pasted, collection process described
- [ ] Evaluation report: both models' accuracy + per-class metrics
- [ ] Confusion matrix as markdown table (not only the .png)
- [ ] 3 wrong predictions analyzed with specific root cause (not just "it was wrong")
- [ ] Sample classifications table with 3–5 posts + label + confidence
- [ ] At least one correct prediction in sample table with explanation
- [ ] Reflection addresses gap between intended and learned behavior specifically
- [ ] Spec reflection present
- [ ] AI usage section with 2+ specific instances

### AC-2: Repo Complete
- [ ] planning.md in repo root (written in Sprint 1)
- [ ] labeled_posts.csv in data/ folder (or linked from README)
- [ ] evaluation_results.json in repo root
- [ ] confusion_matrix.png in repo root
- [ ] README.md complete
- [ ] Final commit: "Sprint 4 complete — all submission requirements met"

### AC-3: Demo Video
- [ ] 3–5 minutes long
- [ ] Shows 3–5 classifications with label + confidence visible
- [ ] One correct + one incorrect prediction narrated
- [ ] Evaluation report walkthrough included

---

# Sprint 4 — Handoff Prompt

**HANDOFF PROMPT — SPRINT 4 (README.md writing)**

You are the Builder for TakeMeter. Before writing anything, read these files:

1. `agents.md`
2. `docs/label-taxonomy.md`
3. `docs/evaluation-plan.md`
4. `planning/decisions.md`
5. `sprints/sprint-4/requirements.md` (this file)

Also have ready:
- `evaluation_results.json` (from repo root)
- Your notes on 3 wrong predictions (from Sprint 3)
- Your AI-assisted failure analysis results (Step 1 of blueprint)
- The baseline prompt you used in Colab

Produce a **Dry Run Summary**:
- Which README sections you will write and a 1-sentence description of what goes in each
- What is OUT OF SCOPE (no new Colab runs, no model changes)
- Any information you need from the human before you can draft a section

**DO NOT write README.md yet. Wait for Architect approval.**
