# TakeMeter — A Fine-Tuned Discourse-Quality Classifier for r/soccer

TakeMeter classifies r/soccer posts by **discourse quality** into three labels —
`analysis`, `hot_take`, and `reaction` — using a fine-tuned `distilbert-base-uncased`
model, compared against a zero-shot Groq baseline.

- **Dataset:** [`data/labeled_posts.csv`](data/labeled_posts.csv) — 200 hand-labeled r/soccer posts
- **Outputs:** [`evaluation_results.json`](evaluation_results.json), [`confusion_matrix.png`](confusion_matrix.png)
- **Design notes:** [`planning.md`](planning.md), [`docs/label-taxonomy.md`](docs/label-taxonomy.md)
- **Demo video:** A 3–5 minute walkthrough (live classifications with label + confidence, one correct and one incorrect prediction narrated, and an evaluation-report overview) was recorded and submitted via the course portal.

---

## Community and Labels

**Community:** [r/soccer](https://www.reddit.com/r/soccer/) — a large, public football community.

**Why this community:** r/soccer produces a continuous, high-volume stream of public,
text-rich discussion spanning the full quality spectrum — from rigorous tactical/statistical
breakdowns to one-word emotional outbursts during live matches. That natural variance is
exactly what a discourse-quality classifier needs, and the "is this analysis or just a hot
take?" distinction is one members already make. Data was collected during FIFA World Cup 2026
coverage, when match threads are most active.

### Label Taxonomy

**`analysis`** — A post that supports a claim about soccer with specific, checkable evidence
(a statistic, a named tactical mechanism, or an explicit cause-and-effect), where the
conclusion is proportional to the evidence.
- *"Arsenal's xG has outpaced their actual goals by 6.2 over the last 10 games. The finishing dip is real, but the underlying numbers say they're still creating enough — teams doubling Saka are pushing Ødegaard into lower-percentage shots from the half-spaces."*
- *"Rodri's progressive passes per 90 (8.4) vs his replacement's (4.1) explains why City's midfield control collapsed without a pivot who can receive under pressure."*

**`hot_take`** — A strong subjective verdict or evaluative/comparative claim about a player,
team, or manager, stated without proportional supporting evidence.
- *"Messi was never tested in a real league — Ligue 1 and MLS are retirement homes. Put him in the Premier League in his prime and he disappears."*
- *"Pep is overrated and would win nothing without a billion-pound squad. Any decent manager wins the league with that City team."*

**`reaction`** — A post that expresses emotion about a moment, result, or match without
making any evaluative claim about quality, ability, or cause.
- *"OFF THE BAR AND IN. I AM NEVER EMOTIONALLY RECOVERING FROM THIS. LETS GOOOO"*
- *"Bro I cannot watch this anymore, my heart can't take stoppage time every single week"*

**Edge-case decision rules:**
1. If a post cites a stat but uses it only to decorate a sweeping, unsupported verdict, it is `hot_take` (not `analysis`).
2. If a post contains any evaluative or comparative claim — even a short insult — it is `hot_take` (not `reaction`).

---

## Data

**Source:** Public r/soccer content only — post-match threads, the daily discussion thread,
and top-level match-thread comments from FIFA World Cup 2026 coverage. No authenticated or
private content.

**Process:** 200 posts were collected and labeled **manually** (read in full, no skimming).
Borderline calls were resolved with the two edge-case rules above and recorded in the CSV
`notes` column (19 rows carry notes). Distribution was validated with
[`scripts/check_distribution.py`](scripts/check_distribution.py). No LLM pre-labeling was used
— every label is a human judgment (see [AI Usage](#ai-usage)).

**Label distribution (200 examples):**

| Label | Count | Share |
|-------|-------|-------|
| analysis | 67 | 33.5% |
| hot_take | 68 | 34.0% |
| reaction | 65 | 32.5% |

No label exceeds 70%; the set is near-balanced.

**Three genuinely difficult examples:**

1. **"The Swiss should be ashamed for letting a team as obviously poor as Qatar steal a point. Qatar spent half that match looking lost on the pitch and concede almost 30 shots."**
   → `analysis` vs `hot_take` → **`hot_take`**. It cites a stat (≈30 shots), but the sweeping "should be ashamed" verdict is disproportionate to that evidence — the stat is decoration (Edge Case 1).
2. **"Taking the title as the team with the most World Cup goals over Brazil with a 7-1 score is hilarious."**
   → `hot_take` vs `reaction` → **`reaction`**. Contains a comparison and a statistic, but uses them as a humorous emotional observation, not a claim about quality (Edge Case 2).
3. **"I have never in my life seen the US play like that. Holy Shit"**
   → `reaction` vs `hot_take` → **`reaction`**. Implies surprise at an unusual performance but makes no explicit judgment of quality, ability, or cause (Edge Case 2).

---

## Fine-Tuning Approach

- **Base model:** `distilbert-base-uncased` (HuggingFace).
- **Training setup:** 10 epochs, learning rate `2e-5`, batch size `8`, on the auto-split
  train set (70% train / 15% val / 15% test, ~140 / ~30 / ~30 examples). The single labeled
  CSV is uploaded whole; Colab handles the split.

**Hyperparameter decision (epochs 3 → 10):** The first run used the notebook defaults
(3 epochs, lr 2e-5, batch 16) and **underfit badly** — 50.0% accuracy, *losing* to the
baseline by 13 points, with the model collapsing uncertain posts into `analysis`. Diagnosis:
under-training on a small (~140-example), subtle 3-way task — not leakage (accuracy was low,
not suspiciously high) and not imbalance (the data is balanced). Fix: raise epochs to 10 and
drop batch size to 8 (more gradient updates per epoch on small data), keeping lr at 2e-5 for
stability. This lifted the fine-tuned model to 66.7% and above the baseline.

---

## Baseline

Zero-shot classification with Groq `llama-3.3-70b-versatile` — no task-specific training.
Every test-set post was sent with the system prompt below; the user message was `Post: {text}`.
All 30 responses parsed cleanly (0 unparseable). The Groq API key was stored in Colab Secrets,
never committed.

```
You are classifying posts from r/soccer, a football (soccer) discussion community.
Assign each post to exactly one of the following three categories.

analysis: The post supports a claim about soccer with specific, checkable evidence — a statistic, a named tactical mechanism, or an explicit cause-and-effect — and the conclusion is proportional to that evidence.

hot_take: The post makes a strong subjective verdict or evaluative/comparative claim about a player, team, or manager, stated without proportional supporting evidence.

reaction: The post expresses emotion about a moment, result, or match and makes no evaluative claim about quality, ability, or cause.

Decision rules for borderline posts:
- If a post cites a stat but uses it only to decorate a sweeping, unsupported verdict, label it hot_take (not analysis).
- If a post contains any evaluative or comparative claim — even a short insult — label it hot_take (not reaction).

Respond with ONLY the label name. Do not explain your reasoning.
```

---

## Evaluation Report

Both models evaluated on the same locked 30-example test set.

### Overall accuracy

| Model | Accuracy |
|-------|----------|
| Zero-shot baseline (Groq `llama-3.3-70b-versatile`) | 63.3% |
| **Fine-tuned `distilbert-base-uncased`** | **66.7%** |

The fine-tuned model beats the baseline by **+3.3 points**.

### Per-class metrics

| Label | Model | Precision | Recall | F1 |
|-------|-------|-----------|--------|-----|
| analysis | baseline | 1.00 | 0.20 | 0.33 |
| analysis | fine-tuned | 0.75 | 0.90 | **0.82** |
| hot_take | baseline | 0.53 | 0.80 | 0.64 |
| hot_take | fine-tuned | 0.50 | 0.30 | **0.38** |
| reaction | baseline | 0.69 | 0.90 | 0.78 |
| reaction | fine-tuned | 0.67 | 0.80 | **0.73** |

The two models have **complementary strengths**: the baseline barely predicts `analysis`
(recall 0.20) but handles the other two well; the fine-tuned model masters `analysis`
(F1 0.82) but struggles with `hot_take` (F1 0.38). Fine-tuning's entire net gain comes from
learning to recognize `analysis`.

### Confusion matrix (fine-tuned model)

| True \ Predicted | analysis | hot_take | reaction |
|------------------|----------|----------|----------|
| **analysis**     | 9        | 1        | 0        |
| **hot_take**     | 3        | 3        | 4        |
| **reaction**     | 0        | 2        | 8        |

`hot_take` is the unstable class — it accounts for **7 of the 10 errors**, scattered into both
neighbors. (See [`confusion_matrix.png`](confusion_matrix.png) for the rendered version.)

### Wrong predictions analyzed

**1. "The Swiss should be ashamed for letting a team as obviously poor as Qatar steal a point. Qatar spent half that match looking lost on the pitch and concede almost 30 shots."**
True `hot_take` → predicted `analysis` (conf 0.98).
*Which labels confused:* hot_take ↔ analysis. *Why hard:* the post cites a concrete stat
(≈30 shots), and the model treats the presence of a number as evidence — exactly the
"stat decoration" trap Edge Case 1 warns about. *Labeling or data problem:* neither — it's a
model limitation; the model keys on surface stats rather than whether the verdict is
proportionally supported. *Fix:* more `hot_take` examples that contain stats-as-decoration, so
the model learns the proportionality distinction.

**2. "Nmecha MOTM"**
True `hot_take` → predicted `reaction` (conf 0.95).
*Which labels confused:* hot_take ↔ reaction. *Why hard:* it's an evaluative pick
(man of the match) but extremely short with no evidence, so it looks like a bare exclamation.
*Labeling or data problem:* model limitation — short evaluative claims have the same surface
form as emotional outbursts. *Fix:* more short `hot_take` examples to teach that brevity ≠
emotion.

**3. "Water breaks help a lot with this style."**
True `analysis` → predicted `hot_take` (conf 0.87).
*Which labels confused:* analysis ↔ hot_take (reverse direction). *Why hard:* it's a genuine
causal claim but brief and without an explicit stat, so the model reads it as an unsupported
opinion. *Labeling or data problem:* borderline label — this was a tight call in annotation
too (a short causal claim). *Fix:* either more short-but-evidenced `analysis` examples, or
accept it as inherently ambiguous.

**One pattern I checked and discarded:** an AI failure-analysis pass suggested "sarcasm" as a
systematic error driver. Re-reading the errors, only one ("This game could've been an email")
is dry humor — a single case, not a systematic pattern — so it was discarded.

---

## Sample Classifications

Five posts run through the fine-tuned model:

| Post (truncated) | Predicted | Confidence | Correct? |
|------------------|-----------|------------|----------|
| "Rodri's progressive passes per 90 dropping from 8.4 to 4.1 is why City lost midfield control." | analysis | 0.97 | ✅ |
| "Saka being doubled forces Ødegaard into lower-percentage shots from the half-spaces." | analysis | 0.97 | ✅ |
| "LETS GOOOO WHAT A GOAL I'M SHAKING" | reaction | 0.95 | ✅ |
| "Germany are finished, total embarrassment." | hot_take | 0.83 | ✅ |
| "Pep is overrated, any manager wins with that squad." | analysis | 0.72 | ❌ (true `hot_take`) |

**Why the first prediction is reasonable:** "Rodri's progressive passes per 90 dropping from
8.4 to 4.1 is why City lost midfield control" pairs a specific statistic with an explicit
cause-and-effect, and the conclusion is proportional to the evidence — the defining shape of
`analysis`. The model is highly confident (0.97).

**The instructive miss:** "Pep is overrated, any manager wins with that squad" is a textbook
`hot_take` (a sweeping verdict with no evidence), but its causal/comparative sentence structure
mimics reasoning, so the model labeled it `analysis` — and at its lowest confidence of the five
(0.72), reflecting genuine uncertainty.

---

## Reflection: Intended vs. Learned Behavior

**What I intended the model to learn:** to judge *whether a claim is argued* — `analysis` when
a conclusion follows proportionally from evidence, `hot_take` when a verdict is asserted without
it, `reaction` when there's only emotion.

**What it actually learned:** surface proxies for those categories. The model keys on the
*presence of stats or concrete match detail* → `analysis`, and on *brevity plus exclamatory
tone* → `reaction`. `hot_take` — the middle category that has no distinctive surface signature
(it's defined by an *absence*, the lack of proportional evidence) — gets squeezed out, which is
why its recall collapses to 0.30 and it supplies 7 of 10 errors.

- **What it overfit to:** lexical/structural cues. Numbers and match-specific nouns pull a post
  toward `analysis` regardless of whether the verdict is actually supported (the Swiss example;
  the live "Pep is overrated… any manager wins" miss).
- **What it missed:** the semantic core of `hot_take` — an assertion *without* proportional
  evidence. Because that's defined negatively, ~140 training examples weren't enough for the
  model to carve it out from its two neighbors.

The honest summary: TakeMeter learned to recognize the *form* of good analysis better than the
zero-shot baseline did, but not the *reasoning quality* the labels were meant to capture.

---

## Spec Reflection

**One way the spec helped:** it forced `planning.md` and the full label taxonomy — definitions,
2 examples each, and explicit edge-case rules — to be written *before* collecting a single
labeled post. Because the proportionality rule and the claim-vs-emotion rule existed up front,
the 200 examples were annotated consistently, and no re-labeling was needed after the fact. The
"run the baseline before fine-tuning" ordering also guaranteed a clean, untainted comparison.

**One way the implementation diverged:** the spec presents the Colab defaults (3 epochs) as the
starting point, and the first run followed them — but it underfit and lost to the baseline. I
diverged to 10 epochs / batch 8 after diagnosing under-training. The spec explicitly invites a
hyperparameter decision, so this divergence was anticipated rather than a true departure — but
it's the clearest example of the implementation deviating from the literal default.

---

## AI Usage

AI assistance (Claude) was used in the following specific instances:

1. **Baseline prompt drafting.** I directed Claude to write the Groq zero-shot classification
   prompt from the locked label definitions and the evaluation-plan rules ("output only the
   label name"). It produced the system prompt used verbatim in Colab Section 5
   (see [`docs/baseline-prompt.md`](docs/baseline-prompt.md)). I reviewed it and ran a small
   parse-failure check before the full run; no changes were needed.

2. **Label stress-testing (Sprint 1).** I gave Claude the three label definitions and asked it
   to generate boundary posts. It produced 6; I classified each myself and confirmed the
   decision rules resolved the borderline cases. This validated the taxonomy before annotation
   (logged in [`docs/label-taxonomy.md`](docs/label-taxonomy.md)).

3. **Failure-analysis pattern surfacing (Sprint 4).** I pasted the 10 misclassified test posts
   into Claude and asked for systematic error patterns. It proposed several; I verified each by
   re-reading the examples and **discarded** the "sarcasm" pattern as unsupported (a single
   case). The confirmed patterns appear in the evaluation report above.

4. **README drafting.** Claude assembled this README from the project's planning and evaluation
   files; I reviewed the content and numbers against `evaluation_results.json` and the Colab
   output.

**Annotation disclosure:** No LLM pre-labeling was used. All 200 labels are human judgments.

---

## Repository Contents

| Path | Description |
|------|-------------|
| [`planning.md`](planning.md) | Pre-build design: community, labels, metrics, AI tool plan |
| [`data/labeled_posts.csv`](data/labeled_posts.csv) | 200 labeled posts (`text`, `label`, `notes`) |
| [`data/dataset_summary.md`](data/dataset_summary.md) | Dataset provenance and validation record |
| [`scripts/check_distribution.py`](scripts/check_distribution.py) | Distribution / label validation |
| [`docs/`](docs/) | Label taxonomy, evaluation plan, baseline prompt, architecture |
| [`evaluation_results.json`](evaluation_results.json) | Both models' accuracy (from Colab) |
| [`confusion_matrix.png`](confusion_matrix.png) | Fine-tuned model confusion matrix |

## Reproducing

1. Open the Colab notebook, set runtime to T4 GPU, add `GROQ_API_KEY` to Colab Secrets.
2. Section 1: define the label map (`{"analysis": 0, "hot_take": 1, "reaction": 2}`), upload `data/labeled_posts.csv`.
3. Section 2: auto-split + tokenize. Section 5: run the Groq baseline. Section 3: fine-tune (10 epochs, lr 2e-5, batch 8). Section 4: evaluate. Section 6: export.
4. Download `evaluation_results.json` and `confusion_matrix.png` to the repo root.
