# Sprint 2 — Dataset Summary

Provenance and validation record for `data/labeled_posts.csv`.

## Overview
| Metric | Value |
|--------|-------|
| Total rows | 200 |
| `analysis` | 67 (33.5%) |
| `hot_take` | 68 (34.0%) |
| `reaction` | 65 (32.5%) |
| Rows with annotation notes | 19 |
| Duplicate posts | 0 |
| Invalid labels | 0 |

**Validation:** `python scripts/check_distribution.py` → **Distribution check PASSED**
(200+ rows, exactly `text,label,notes` columns, all labels valid, no label over 70%).

> Note: one row was reclassified during QA — "It wasn't a chore to watch the USA play."
> moved from `reaction` to `hot_take` (positive evaluation = an evaluative claim, per the
> claim-vs-emotion rule). Distribution shifted from 67/67/66 to the 67/68/65 shown above.

## Source
Public r/soccer content only (no authenticated content) — post-match threads, the daily
discussion thread, and top-level match-thread comments from FIFA World Cup 2026 coverage.

Final-batch source threads (representative):
- Post Match Thread: Spain 4 – 0 Saudi Arabia | FIFA World Cup 2026
- Post Match Thread: Tunisia 0 – 4 Japan | FIFA World Cup 2026
- Post Match Thread: England 4 – 2 Croatia | FIFA World Cup 2026
- Post Match Thread: Netherlands 5 – 1 Sweden | FIFA World Cup 2026

## Difficult Annotation Cases
The four canonical cases are recorded in `planning/state.md`; the full set of 19 borderline
calls is flagged inline in the CSV `notes` column. Representative examples:

1. **"The Swiss should be ashamed for letting a team as obviously poor as Qatar steal a point. Qatar spent half that match looking lost on the pitch and concede almost 30 shots."**
   - Considered `analysis` vs `hot_take` → **`hot_take`**
   - Cites match evidence (≈30 shots), but the sweeping "should be ashamed" verdict is disproportionate, so the stat functions as decoration (Edge Case 1).

2. **"Taking the title as the team with the most World Cup goals over Brazil with a 7-1 score is hilarious."**
   - Considered `hot_take` vs `reaction` → **`reaction`**
   - Contains a comparison and a statistic, but uses them as a humorous emotional observation rather than a claim about quality or ability (Edge Case 2).

3. **"I have never in my life seen the US play like that. Holy Shit"**
   - Considered `reaction` vs `hot_take` → **`reaction`**
   - Implies surprise at an unusual performance but makes no explicit judgment of quality, ability, or cause (Edge Case 2).

4. **"It wasn't a chore to watch the USA play."**
   - Considered `reaction` vs `hot_take` → reclassified to **`hot_take`**
   - A positive evaluation of watchability is an evaluative claim; kept consistent with "What a great World Cup so far" (Edge Case 2, QA review).

5. **"Congratulations to Australia on a perfectly executed game plan they fully deserved to win this game."**
   - Considered `analysis` vs `hot_take` → **`analysis`**
   - Includes praise, but "perfectly executed game plan" supplies a causal basis for the result (Edge Case 1).

6. **"Si era penal. He stood on his foot."**
   - Considered `hot_take` vs `analysis` → **`analysis`**
   - Very brief, but the second sentence supplies direct, checkable evidence for the penalty claim.
