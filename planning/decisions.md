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
