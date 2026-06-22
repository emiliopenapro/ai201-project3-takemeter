# Risks — Known Traps

## RISK-001: Vague labels (CRITICAL)
**Risk:** Labels defined by subjective words ("good post," "quality take") without a precise decision boundary. The model will learn an inconsistent signal and perform poorly.  
**Mitigation:** Every label must have a one-sentence definition that states the decision boundary explicitly. Run the AI stress-test in docs/label-taxonomy.md before annotating.  
**Status:** Active warning — enforce at Sprint 1 checkpoint.

## RISK-002: Class imbalance (CRITICAL)
**Risk:** One label accounts for >70% of examples. The model learns to predict that label constantly and achieves misleadingly high accuracy.  
**Mitigation:** Count label distribution after every 50 examples. If any label is trending above 70%, actively seek examples of the underrepresented labels before continuing.  
**Status:** Open — monitor during Sprint 2.

## RISK-003: Colab session reset mid-run
**Risk:** Colab disconnects after inactivity, wiping all variables. Re-running only later sections without re-running Sections 1+2 first causes errors or uses stale data.  
**Mitigation:** If session resets: re-upload CSV, re-run Sections 1 and 2, re-run Section 5 (baseline), THEN continue. Document this in SCAFFOLD.md.  
**Status:** Open — enforce at Sprint 3.

## RISK-004: Test set leakage
**Risk:** The same posts appear in both training and test data, causing suspiciously high accuracy (>95%) that doesn't reflect real performance.  
**Mitigation:** Do not manually split the CSV — let Colab handle it. If accuracy is >90% on a subjective task, investigate before writing the report.  
**Status:** Open — validate at Sprint 3 checkpoint.

## RISK-005: Groq key committed to GitHub
**Risk:** API key pasted directly into a Colab code cell, saved, and pushed to a public GitHub repo.  
**Mitigation:** Use Colab Secrets (🔑 icon). Never paste the key into a code cell. This is DEC-005 — locked.  
**Status:** Active warning — enforce at every Colab step in Sprint 3.

## RISK-006: Baseline prompt produces unparseable responses
**Risk:** Groq LLM returns explanations, qualifications, or reformatted label names that the notebook's parser can't match. >10% unparseable = invalid baseline.  
**Mitigation:** Prompt must say "Output only the label name." Test with 3–5 examples manually before running the full baseline. Revise prompt if needed.  
**Status:** Open — validate at Sprint 3, Milestone 4.

## RISK-007: Annotating by skimming
**Risk:** Labeling 200 posts quickly by skimming leads to inconsistent annotations. The model learns noise, not signal.  
**Mitigation:** Read each post fully before assigning a label. Keep a running notes column for cases that gave genuine pause. Budget 3–4 hours for annotation.  
**Status:** Active warning — enforce at Sprint 2.

## RISK-008: Fine-tuned model worse than baseline
**Risk:** The fine-tuned model underperforms the zero-shot baseline across the board.  
**Mitigation:** If this happens, investigate before writing the report. Check for: label leakage (RISK-004), severe class imbalance (RISK-002), inconsistent annotation (RISK-007), or a training bug. Do not submit without understanding why.  
**Status:** Open — validate at Sprint 3, Milestone 5.
