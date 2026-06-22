# Evaluation Plan

## Metrics Used and Why

| Metric             | Used For        | Why                                                                 |
|--------------------|-----------------|---------------------------------------------------------------------|
| Overall accuracy   | Both models     | High-level comparison — but misleading if classes are imbalanced    |
| Per-class F1       | Both models     | Best single number per class — balances precision and recall        |
| Per-class precision| Both models     | "Of all posts predicted as X, how many actually were X?"           |
| Per-class recall   | Both models     | "Of all posts that are truly X, how many did the model catch?"     |
| Confusion matrix   | Fine-tuned only | Shows which label pairs are being confused and in which direction   |

## Definition of Success
Locked numeric thresholds (Q-004, 2026-06-22). All four must hold:
- Fine-tuned model overall accuracy **> 75%**
- **Every** per-class F1 score **> 0.65** (`analysis`, `hot_take`, `reaction`)
- Fine-tuned model beats the Groq baseline by **at least 5 percentage points** of accuracy
- **No single class F1 = 0** — the model must learn all three distinctions

Rationale: 75% accuracy is a meaningful lift over a ~33% random-guess floor for 3 balanced
classes; the 0.65 per-class F1 floor guards against the model "winning" on accuracy while
ignoring a minority class; the 5-point margin over baseline confirms fine-tuning added real
signal rather than restating what zero-shot Groq already knows.

## Interpreting Results

| Scenario                                  | What it means                                                         |
|-------------------------------------------|-----------------------------------------------------------------------|
| All per-class F1 ≥ 0.70                   | Model learned all distinctions well                                   |
| One class F1 ≈ 0, others fine             | Model can't learn that boundary — check labels and examples           |
| All classes F1 similar and low            | Task too hard for 200 examples, or labels are inconsistent            |
| Fine-tuned barely beats baseline          | Labels may be too easy or too noisy — fine-tuning added little signal |
| Fine-tuned much worse than baseline       | Check for label leakage, class imbalance, or training bug             |
| Accuracy suspiciously high (>95%)         | Check for test set leakage into training data                         |

## Failure Analysis Protocol (Sprint 4)
1. Collect all wrong predictions from Colab Section 4 output.
2. Paste misclassified examples into Claude and ask: "What patterns do you see in these misclassifications?"
3. **Verify every pattern yourself** by re-reading the examples — do not trust AI pattern claims blindly.
4. For each of the 3 required wrong predictions in README, answer:
   - Which labels are being confused?
   - Why is that boundary hard? (sarcasm, short post, ambiguous framing, topic mismatch?)
   - Is this a labeling problem or a data problem?
   - What would need to change to fix it?

## Baseline Prompt Design Rules
- Include full label definitions from `docs/label-taxonomy.md`
- Instruct the model to output ONLY the label name — no explanation
- Example format: "Classify the following post as exactly one of: [label1, label2, label3]. Output only the label name.\n\nPost: {text}"
- If >10% of responses are unparseable, revise the prompt before proceeding
