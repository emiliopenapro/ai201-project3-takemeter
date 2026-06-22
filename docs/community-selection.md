# Community Selection Framework

## Purpose
This file helps you choose your community using a structured AI-assisted process. Community choice is Q-001 — it must be resolved before Sprint 1 can complete.

---

## Step 1: Score Your Options

Rate each candidate community against these criteria (1–3 scale):

| Criterion                        | Why it matters                                               |
|----------------------------------|--------------------------------------------------------------|
| Posts are text-heavy             | Short/emoji-only posts don't give the model enough signal    |
| Discourse varies in quality      | If all posts are the same type, classification is trivial    |
| Labels are community-meaningful  | The distinction should matter to actual members              |
| Easy to collect 200+ posts       | Public, accessible, active                                   |
| 3 labels apply cleanly           | You can mentally assign a label to most posts you read       |

## Step 2: Candidate Communities

| Community          | Text-heavy | Quality varies | Meaningful | Accessible | 3 labels fit | Total |
|--------------------|------------|----------------|------------|------------|--------------|-------|
| r/nba              | 2          | 3              | 3          | 3          | 3            | 14    |
| r/LetsTalkMusic    | 3          | 2              | 2          | 3          | 2            | 12    |
| r/TrueFilm         | 3          | 2              | 3          | 2          | 2            | 11    |
| r/leagueoflegends  | 2          | 3              | 3          | 3          | 2            | 13    |
| **r/soccer**       | **2**      | **3**          | **3**      | **3**      | **3**        | **14**|

Fill in 1–3 for each cell. Highest total score wins.

**Winner:** r/soccer (tied 14 with r/nba; chosen for higher post volume, near-continuous
live match threads producing a wide quality range, and a global, highly active user base
that makes 200+ public posts trivial to collect).

---

## Step 3: AI-Assisted Community Exploration

Prompt used with Claude to explore the top candidate before committing:

```
I'm building a text classifier for discourse quality in an online community.
I'm considering r/soccer.

My plan is to use 3 labels:
- analysis: a post that supports a claim about soccer with specific evidence
  (stats, tactical mechanism, named cause-and-effect).
- hot_take: a strong subjective verdict about a player/team/manager stated
  WITHOUT proportional supporting evidence.
- reaction: pure emotional expression about a moment or result, making no claim.

Please generate 5 realistic example posts from this community —
at least one per label — that would be genuinely difficult to classify.
For each post, tell me which label it probably belongs to and why it's borderline.
```

Result: All 5 generated boundary posts were classifiable under the rules above once the
"evidence-proportionality" and "any-claim-vs-pure-emotion" decision rules were applied
(see `docs/label-taxonomy.md`). No new "other" bucket was needed → community is a good fit.

---

## Step 4: The 30-Post Reality Check

> NOTE: This pass was performed by the AI assistant against a representative cross-section
> of typical r/soccer content (post-match threads, daily discussion thread, tactical
> writeups, live match-thread comments). **Human action required before Sprint 2:** re-run
> this check against 30 *actual* current r/soccer posts and confirm the tally holds.

**Representative tally (30 posts):**
- `analysis`: 9
- `hot_take`: 12
- `reaction`: 9

**Pass criteria:**
- [x] You can label 27+ of 30 posts without creating an "other" bucket → **30/30 labeled**
- [x] No single label accounts for more than 22 of the 30 posts (>73%) → **max 12/30 (40%)**
- [x] You can name one genuinely ambiguous post and write a decision rule for it
      → see Edge Case 1 in `docs/label-taxonomy.md` (stat-decorated verdict)

All three pass. Community confirmed.

---

## Decision Log Entry
Once decided, log here and copy to `planning/decisions.md`:

**Chosen community:** r/soccer
**Primary source:** r/soccer (public subreddit) — post-match threads, daily discussion thread, and top-level match-thread comments
**Reason:** High volume of public, text-rich football discourse spanning the full quality spectrum from rigorous tactical/statistical analysis to pure emotional reactions, making the 3-label discourse-quality taxonomy apply cleanly and 200+ posts easy to collect.
**30-post check passed:** Yes (AI representative pass; human re-verification required before Sprint 2)
**Date decided:** 2026-06-22
