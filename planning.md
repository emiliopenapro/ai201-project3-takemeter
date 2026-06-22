# TakeMeter — Planning

**Project:** TakeMeter — Fine-Tuned Discourse Quality Classifier
**Course:** AI201 | Applications of AI Engineering
**Date:** 2026-06-22

> Scope note: This document is the Sprint 1 deliverable. No data has been collected and no
> Colab work has started. Example posts below are realistic representations of r/soccer
> discourse, reviewed and accepted by the human on 2026-06-22.

---

## 1. Community

**Community:** r/soccer (public subreddit).

**Why it's a good fit for classification:** r/soccer generates a continuous, high-volume
stream of public, text-rich football discussion that spans the full quality spectrum — from
rigorous statistical and tactical breakdowns, to confident-but-unsupported opinions, to pure
emotional outbursts during live matches. That natural variance is exactly what a
discourse-quality classifier needs: the labels are not trivially separable, but they are
real and meaningful to members (the "that's analysis vs. that's just a hot take" distinction
is a recurring meta-conversation in the sub). The community is also large, active, and
fully public, so collecting 200+ posts across all three labels is straightforward.

It scored 14/15 on the selection rubric (tied highest), and passed the 30-post reality check
with a 9 / 12 / 9 split across the three labels (no label above 40%, all 30 labelable).

---

## 2. Labels

Three labels, mutually exclusive. Full definitions, examples, and stress-test log live in
`docs/label-taxonomy.md`; DEC-007 in `planning/decisions.md` locks them.

### `analysis`
**Definition:** A post that supports a claim about soccer with specific, checkable evidence —
a statistic, a named tactical mechanism, or an explicit cause-and-effect — where the
conclusion is proportional to the evidence given.
- **Example A:** "Arsenal's xG has outpaced their actual goals by 6.2 over the last 10 games. The finishing dip is real, but the underlying numbers say they're still creating enough — teams doubling Saka are pushing Ødegaard into lower-percentage shots from the half-spaces."
- **Example B:** "Rodri's progressive passes per 90 (8.4) vs his replacement's (4.1) explains why City's midfield control collapsed. Without a pivot who can receive on the half-turn under pressure, they're forced into longer, lower-percentage switches."

### `hot_take`
**Definition:** A strong subjective verdict or evaluative/comparative claim about a player,
team, or manager, stated without proportional supporting evidence.
- **Example A:** "Messi was never tested in a real league — Ligue 1 and MLS are retirement homes. Put him in the Premier League in his prime and he disappears like every other flat-track bully."
- **Example B:** "Pep is overrated and would win nothing without a billion-pound squad. Any decent manager wins the league with that City team."

### `reaction`
**Definition:** A post that expresses emotion about a moment, result, or match without
making any evaluative claim about quality, ability, or cause.
- **Example A:** "OFF THE BAR AND IN. I AM NEVER EMOTIONALLY RECOVERING FROM THIS. LETS GOOOO 🔥🔥🔥"
- **Example B:** "Bro I cannot watch this anymore, my heart can't take stoppage time every single week 😭"

---

## 3. Hard Edge Cases

### Edge Case 1 — `hot_take` vs. `analysis` (the stat-decorated verdict)
**Ambiguous post:** "City's defense is finished, they've conceded in 7 straight games."
**Decision rule:** If the post cites evidence AND the conclusion follows proportionally from
that evidence, label `analysis`. If it cites a stat but uses it only as decoration for a
sweeping, unsupported verdict — "finished" does not follow from a 7-game streak alone —
label `hot_take`. *The test is proportionality, not the mere presence of a number.*

### Edge Case 2 — `reaction` vs. `hot_take` (the emotional insult)
**Ambiguous post:** "Pickford is so trash lmaooo 😭"
**Decision rule:** If the post makes any evaluative or comparative claim about a
player/team/manager — even a one-word insult like "trash" — label `hot_take`. If it is pure
emotion with no claim about quality, ability, or cause, label `reaction`. *Emoji and slang
do not decide the label; the presence of a claim does.*

---

## 4. Data Collection Plan

**Source:** r/soccer public content only — post-match threads, the daily discussion thread,
and top-level comments in live match threads. No authenticated, private, or DM content.

**Target counts:** ~70 examples per label, **210 total** (exceeds the 200 minimum). The CSV
follows the `text, label, notes` schema in `docs/data-model.md`. A single CSV is submitted —
the Colab notebook performs the 70/15/15 split (DEC-002: do **not** pre-split).

**Balance / underrepresentation plan:**
- Aim for roughly 33% per label; hard cap any label at 70% of the dataset (architecture
  constraint). `analysis` is expected to be the scarcest because it requires effort to write,
  so it will be sourced deliberately.
- If any label is under 20% after the first 150 examples, actively seek that type before
  finishing: for `analysis`, mine tactical/stats writeup threads and flaired post-match
  analysis; for `reaction`, sample live match-thread comments during goals; for `hot_take`,
  sample opinion/debate threads.
- Difficult or borderline posts get a `notes` entry recording which edge-case rule was
  applied, so annotation stays consistent and auditable.

---

## 5. Evaluation Metrics

Per `docs/evaluation-plan.md`. Accuracy alone is insufficient because three classes can be
imbalanced and a model can score well on accuracy while ignoring a minority class.

| Metric              | Applied to        | Why it's included                                                        |
|---------------------|-------------------|--------------------------------------------------------------------------|
| Overall accuracy    | Both models       | Headline comparison vs. the ~33% random-guess floor; misleading alone.   |
| Per-class F1        | Both models       | Best single per-class number — balances precision and recall.            |
| Per-class precision | Both models       | "Of posts predicted X, how many were truly X?" Catches over-prediction.  |
| Per-class recall    | Both models       | "Of posts truly X, how many were caught?" Catches a neglected class.     |
| Confusion matrix    | Fine-tuned only   | Shows *which* label pairs are confused and in which direction (expect the `analysis`↔`hot_take` boundary to be the hardest). |

Both the fine-tuned distilbert model and the Groq zero-shot baseline are scored on the same
held-out test set so the comparison is apples-to-apples.

---

## 6. Definition of Success

Specific, numeric, locked as Q-004. **All four must hold:**
1. Fine-tuned model overall accuracy **> 75%**.
2. **Every** per-class F1 (`analysis`, `hot_take`, `reaction`) **> 0.65**.
3. Fine-tuned model beats the Groq baseline by **≥ 5 percentage points** of accuracy.
4. **No class F1 = 0** — the model must demonstrably learn all three distinctions.

If criterion 2 fails for `analysis`↔`hot_take`, the most likely cause is inconsistent
application of the Edge Case 1 proportionality rule during annotation — the fix is a labeling
pass, not more data.

---

## AI Tool Plan

### Label stress-testing
- **Tool:** Claude (Opus).
- **Prompt:** Paste the three label definitions and ask it to generate 5–10 boundary posts
  that are deliberately hard to classify, with its own proposed label and reasoning for each.
- **What I do with results:** Classify each generated post myself using the decision rules,
  compare against Claude's labels, and log every post in the stress-test table in
  `docs/label-taxonomy.md`. If 3+ posts remain hard after applying the rules, I tighten the
  definitions before annotating. (Already run for Sprint 1: 2/6 borderline, both resolved →
  definitions are tight enough to proceed.)

### Annotation assistance
- **Tool:** Groq `llama-3.3-70b-versatile` (same account as the baseline) for optional
  LLM pre-labeling.
- **How:** Pre-label collected posts zero-shot using the exact label definitions, then
  **manually review every pre-label** — the human label is authoritative, never the model's.
  Pre-labels are a draft to speed review, not a source of truth.
- **Tracking:** Any post where I overrode the pre-label gets a `notes` entry. This doubles as
  an early, informal signal of where the baseline will struggle.

### Failure analysis (Sprint 4)
- **Tool:** Claude.
- **What I paste in:** All misclassified test examples from Colab Section 4 (true label,
  predicted label, text) and ask: "What patterns do you see in these misclassifications?"
- **How I verify:** I re-read every example behind each claimed pattern myself — AI pattern
  claims are not trusted blindly (per `docs/evaluation-plan.md`). For each of the 3 required
  wrong predictions in the README I answer: which labels are confused, why the boundary is
  hard (sarcasm / short post / stat-decorated verdict / topic mismatch), whether it's a
  labeling vs. data problem, and what would fix it.

---

## Out of Scope for Sprint 1
- No data collection. `data/labeled_posts.csv` does not exist yet.
- No Colab notebook work, no fine-tuning, no baseline run.
- No README.md, no demo video, no stretch features.

## Sprint 1 Status
Complete. Example posts and the 30-post reality check were reviewed and accepted by the human
(2026-06-22). Remaining before Sprint 2: create the GitHub repo and commit "Sprint 1 complete".
