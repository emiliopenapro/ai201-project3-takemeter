# Sprint 3 — Requirements

## What Is Being Built
The complete Colab pipeline: baseline run, fine-tuning, side-by-side comparison, and output file downloads.

## Scope
| In Scope                                              | Out of Scope                          |
|-------------------------------------------------------|---------------------------------------|
| Colab Section 1: upload CSV + define label map        | Writing README.md                     |
| Colab Section 2: split + tokenize                     | Failure analysis writeup              |
| Colab Section 5: Groq baseline (run FIRST)            | Stretch features                      |
| Colab Section 3: fine-tune distilbert-base-uncased    |                                       |
| Colab Section 4: evaluate fine-tuned model            |                                       |
| Colab Section 6: side-by-side comparison + export     |                                       |
| Download + commit evaluation_results.json             |                                       |
| Download + commit confusion_matrix.png                |                                       |

## Critical Ordering Rule
Run Section 5 (baseline) BEFORE Section 3 (fine-tuning). The baseline must be established on the locked test set before the model sees training data.

## Deliverables
1. `evaluation_results.json` — committed to repo root
2. `confusion_matrix.png` — committed to repo root
3. Baseline accuracy and per-class metrics saved/noted
4. Fine-tuned model metrics saved/noted
5. At least 3 wrong predictions identified and noted for Sprint 4

## Success Definition
Fine-tuning completes without error. You have both models' metrics on the same test set. You can compare them directly. If fine-tuned model is worse than baseline across the board, investigate before moving to Sprint 4.

---

# Sprint 3 — Blueprint

## Setup Checklist (do before running any cells)
- [ ] Open your Colab copy (File → Save a copy in Drive if not done)
- [ ] Runtime → Change runtime type → T4 GPU → Save
- [ ] 🔑 icon → Add secret `GROQ_API_KEY` → enable notebook access
- [ ] Have `data/labeled_posts.csv` ready to upload

## Execution Order
```
Section 1 → Section 2 → Section 5 → Section 3 → Section 4 → Section 6
```

### Section 1: Label Map + CSV Upload
- Define your label map matching your 3 labels exactly (case-sensitive)
- Example: `label_map = {"analysis": 0, "hot_take": 1, "reaction": 2}`
- Upload labeled_posts.csv when prompted

### Section 2: Split + Tokenize
- Notebook splits automatically: 70% train / 15% val / 15% test
- Review split sizes and label distribution — should look proportional
- If distribution looks wrong, check CSV for label typos

### Section 5: Groq Baseline (RUN BEFORE FINE-TUNING)
- Write classification prompt using label definitions from docs/label-taxonomy.md
- Prompt must: include all 3 label definitions, instruct "output only the label name"
- Run on test set only
- If >10% responses are unparseable → revise prompt before continuing
- Save baseline accuracy and per-class metrics somewhere accessible

### Section 3: Fine-Tune distilbert-base-uncased
- Default hyperparameters: 3 epochs, lr=2e-5, batch_size=16
- If you change any hyperparameter, note what and why → goes in README
- Training takes 5–15 minutes on T4 GPU
- Do not close the browser tab during training

### Section 4: Evaluate Fine-Tuned Model
- Generates per-class metrics and confusion_matrix.png
- Download confusion_matrix.png immediately (Files panel → right-click → Download)
- Identify 3 wrong predictions to analyze in Sprint 4

### Section 6: Comparison + Export
- Prints side-by-side baseline vs. fine-tuned comparison
- Writes evaluation_results.json
- Download evaluation_results.json immediately

## If Colab Session Resets
Re-run in this order: Section 1 → Section 2 → Section 5 → then wherever you were.
Never skip Section 5 re-run if session resets before fine-tuning completes.

---

# Sprint 3 — Acceptance Criteria

- [ ] Colab ran without errors through all 6 sections
- [ ] Baseline metrics recorded (overall accuracy + per-class)
- [ ] Fine-tuned model metrics recorded (overall accuracy + per-class)
- [ ] `evaluation_results.json` downloaded and committed to repo root
- [ ] `confusion_matrix.png` downloaded and committed to repo root
- [ ] At least 3 wrong predictions identified and noted
- [ ] If fine-tuned worse than baseline: root cause investigated and logged in planning/decisions.md
- [ ] Git commit: "Sprint 3 complete — evaluation outputs committed"

---

# Sprint 3 — Handoff Prompt

> Sprint 3 is primarily human Colab work. The Builder can help write the Groq baseline prompt.

**HANDOFF PROMPT — SPRINT 3 (baseline prompt writing)**

You are the Builder for TakeMeter. Read these files:
1. `docs/label-taxonomy.md` (label definitions)
2. `docs/evaluation-plan.md` (baseline prompt rules)

Write a Groq classification prompt for the baseline that:
- Includes all 3 label definitions exactly as written in docs/label-taxonomy.md
- Instructs the model to output ONLY the label name — no explanation, no punctuation
- Includes a placeholder `{text}` where the post will be inserted
- Follows this structure: system message (task + definitions) + user message (post text)

After writing the prompt, produce a Dry Run showing what the output would look like for 2 example posts from the label-taxonomy.md examples. Wait for approval before this prompt is used in Colab.
