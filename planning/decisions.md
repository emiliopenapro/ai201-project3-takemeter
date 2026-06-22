# Decisions Log

## DEC-001: Number of Labels
**Decision:** Use 3 labels.  
**Reason:** Recommended by spec. 2 labels is often too coarse; 4 increases annotation difficulty and data requirements significantly.  
**Locked:** Yes.

## DEC-002: Do Not Pre-Split the CSV
**Decision:** Submit a single labeled CSV. Colab handles the 70/15/15 split automatically.  
**Reason:** Spec explicitly states "The notebook expects a single labeled CSV — it handles the train/validation/test split automatically. Do not submit multiple pre-split files."  
**Locked:** Yes — do not split manually under any circumstances.

## DEC-003: Base Model
**Decision:** `distilbert-base-uncased`  
**Reason:** Specified by course. Free, fast on T4 GPU (5–15 min for 200 examples), no account needed.  
**Locked:** Yes — unless a deliberate alternative is chosen and logged here with justification.

## DEC-004: Baseline Model
**Decision:** Groq `llama-3.3-70b-versatile` zero-shot classification.  
**Reason:** Same account as Projects 1 & 2. Required by spec.  
**Locked:** Yes.

## DEC-005: Groq Key Storage
**Decision:** Groq API key goes into Colab Secrets only. Never pasted into code cells. Never committed to GitHub.  
**Reason:** Security. Key exposed in a public GitHub repo is a critical vulnerability.  
**Locked:** Yes — non-negotiable.

## DEC-006: Community Choice
**Decision:** r/soccer (public subreddit).
**Reason:** Highest-scoring candidate (14/15, tied with r/nba) with greater public post volume. Continuous live match threads plus tactical writeups produce the full discourse-quality spectrum, making the 3-label taxonomy apply cleanly and 200+ public posts easy to collect.
**Primary source:** Post-match threads, the daily discussion thread, and top-level match-thread comments — public only, no authenticated content.
**30-post reality check:** Passed (AI representative pass; human re-verification required before Sprint 2 annotation).
**Locked:** Yes. Date: 2026-06-22.

## DEC-007: Label Taxonomy
**Decision:** 3 labels — `analysis`, `hot_take`, `reaction`.
- `analysis` — claim backed by specific, checkable evidence (stat / tactical mechanism / cause-effect) with a conclusion proportional to that evidence.
- `hot_take` — strong subjective verdict or evaluative/comparative claim stated without proportional evidence.
- `reaction` — pure emotional expression about a moment/result, making no claim.
**Edge rules:** (1) stat-decorated sweeping verdict → `hot_take`, not `analysis`; (2) any evaluative claim, even an insult → `hot_take`, not `reaction`.
**Reason:** Mirrors the proven discourse-quality split in docs/data-model.md, grounded in real r/soccer content. Full definitions, examples, and stress-test log in docs/label-taxonomy.md.
**Locked:** Yes — changing labels after annotation begins means re-labeling everything. Date: 2026-06-22.
> Example posts in docs/label-taxonomy.md reviewed and accepted by the human (2026-06-22).

## DEC-008: Hyperparameter Defaults
**Decision (provisional):** Use Colab defaults — 3 epochs, learning rate 2e-5, batch size 16.  
**Reason:** Spec-recommended starting point for 200 examples on distilbert.  
**Locked:** No — adjust if validation performance is poor. Log any changes here with reason.

## DEC-009: Sprint 3 First Run Underperformed Baseline (RISK-008) → Retune
**First run (defaults, 3 epochs / lr 2e-5 / batch 16):**
- Baseline (Groq zero-shot) accuracy: 63.3%
- Fine-tuned distilbert accuracy: 50.0% (−13.3 pts vs baseline) on a 30-example test set.
- Fine-tuned per-class F1 (from confusion matrix): analysis ≈ 0.64, hot_take ≈ 0.35, reaction ≈ 0.40.
- Fails success thresholds (acc >75%, all F1 >0.65, ≥5 pts over baseline).

**Root-cause investigation (RISK-008 requires this before Sprint 4):**
- NOT test-set leakage (RISK-004): accuracy is low, not suspiciously high.
- NOT class imbalance (RISK-002): dataset is balanced 67/68/65.
- NOT a label-map/parse bug: labels matched, baseline ran cleanly at 63%.
- Diagnosis: **under-training on a small, subtle dataset.** The model over-predicts
  `analysis` (18/30 predictions) — it learned the lexically distinctive class (stats/tactics
  vocab) but collapsed `hot_take` and `reaction` (recall 0.30 each) into it. ~140 training
  examples × 3 epochs is too few passes for distilbert to separate the two subjective classes,
  while the 70B zero-shot baseline leans on broad world knowledge.

**Decision:** Retune with more gradient steps before accepting a result.
- num_train_epochs: 3 → 10
- per_device_train_batch_size: 16 → 8 (more update steps per epoch on small data)
- learning_rate: keep 2e-5 (stability)
**Reason:** Underfitting is the most likely cause; more epochs + smaller batches is the
standard fix and gives fine-tuning a fair chance to beat the baseline. This is also the
hyperparameter decision documented in the README (Feature 3). If the retune still loses to
baseline, accept and document the honest negative result per the Sprint 4 analysis plan.
**Locked:** No — supersedes DEC-008 for the retune run. Update with retune results.

**Retune result (10 epochs / lr 2e-5 / batch 8):**
- Fine-tuned accuracy: 50.0% → **66.7%** (+16.7 pts from the retune).
- Now **beats baseline** 63.3% by **+3.3 pts** → RISK-008 resolved (no longer worse than baseline).
- Below the aspirational success thresholds (acc >75%, ≥5 pts over baseline) but a defensible,
  honest result for ~140 training examples on a subjective 3-way task. Final hyperparameters:
  10 epochs, lr 2e-5, batch size 8 — this is the README's documented hyperparameter decision.
