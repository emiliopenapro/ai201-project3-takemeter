# Open Questions

## Q-001: Community Choice [ANSWERED — 2026-06-22]
**Question:** Which online community will TakeMeter classify?  
**Why it matters:** Determines data source, label taxonomy, annotation effort, and evaluation framing. Everything downstream depends on this.  
**How to decide:** Use `docs/community-selection.md` — score options, run the AI exploration prompt, complete the 30-post reality check.  
**Answer:** **r/soccer** (public subreddit). Highest-scoring candidate (14/15), full discourse-quality spectrum, easy 200+ public-post collection. Logged as DEC-006. 30-post check passed (AI representative pass; human re-verification required before Sprint 2).

## Q-002: Final Label Names and Definitions [ANSWERED — 2026-06-22]
**Question:** What are the exact 3 label names and one-sentence definitions?  
**Why it matters:** These go into planning.md, the Groq baseline prompt, and the Colab label map. Changing them after annotation starts means re-labeling everything.  
**Answer:** **`analysis`** — claim backed by specific, checkable evidence with a proportional conclusion. **`hot_take`** — strong subjective verdict/comparison without proportional evidence. **`reaction`** — pure emotional expression making no claim. Full definitions + edge rules in docs/label-taxonomy.md; logged as DEC-007.

## Q-003: Data Collection Source [ANSWERED — 2026-06-22]
**Question:** Exactly where will you collect posts? (e.g., specific subreddit, public Discord, fan forum?)  
**Why it matters:** Must be public-only. No content behind authentication. Documented in README.  
**Answer:** r/soccer public content only — post-match threads, the daily discussion thread, and top-level match-thread comments. No authenticated or private content.

## Q-004: Definition of Success — Numeric Thresholds [ANSWERED — 2026-06-22]
**Question:** What specific accuracy and F1 thresholds will you use as your success criteria in planning.md?  
**Why it matters:** Spec requires success criteria to be specific enough to objectively determine if you hit them.  
**Answer:** Fine-tuned overall accuracy > 75%; every per-class F1 > 0.65; fine-tuned beats Groq baseline by ≥ 5 percentage points accuracy; no class F1 = 0. Logged in docs/evaluation-plan.md and planning.md §6.

## Q-005: Stretch Features [OPEN]
**Question:** Will you implement any stretch features (inter-annotator reliability, confidence calibration, error pattern analysis, deployed interface)?  
**Why it matters:** Each stretch feature requires updating planning.md BEFORE implementation.  
**Answer:** _(decide after Sprint 3 is complete)_
