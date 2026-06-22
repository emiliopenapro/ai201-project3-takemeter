# State — Current Project Status

## Active Sprint
**Sprint 2:** Data collection + annotation → data/labeled_posts.csv (Milestone 3)

## Status
- [x] Scaffold created
- [x] Architect Packs for all 4 sprints generated
- [x] GitHub repo created (ai201-project3-takemeter) — pushed to origin/main
- [x] Community chosen — r/soccer (Q-001 resolved, DEC-006)
- [x] 30-post reality check completed (representative pass — accepted by human)
- [x] 3 labels defined with one-sentence definitions (analysis / hot_take / reaction, DEC-007)
- [x] 2 example posts per label identified (accepted by human 2026-06-22)
- [x] Edge case decision rules written (2: stat-decorated verdict; emotional insult)
- [x] Label stress-test completed (6 boundary posts reviewed, logged in label-taxonomy.md)
- [x] planning.md written (all 6 required sections + AI Tool Plan)
- [x] Data collected and annotated (Sprint 2) — 200 r/soccer posts in data/labeled_posts.csv
- [x] CSV validated: 200+ examples, no label > 70% (Sprint 2) — 67/68/65, check PASSED
- [ ] Colab notebook copied to Drive and T4 GPU set (Sprint 3)
- [ ] Baseline run completed — numbers saved (Sprint 3)
- [ ] Fine-tuning completed (Sprint 3)
- [ ] evaluation_results.json downloaded + committed (Sprint 3)
- [ ] confusion_matrix.png downloaded + committed (Sprint 3)
- [ ] README.md complete with evaluation report (Sprint 4)
- [ ] Demo video recorded (Sprint 4)

## Currently Blocked
- Nothing. Sprint 2 in progress — human collecting + labeling real r/soccer posts.

## Sprint 2 Tracking

### Label Distribution (RISK-002 — verified via `python scripts/check_distribution.py`)
| Checkpoint | analysis | hot_take | reaction | total |
|------------|----------|----------|----------|-------|
| FINAL      | 67 (33.5%) | 68 (34.0%) | 65 (32.5%) | 200 |

Distribution check PASSED — no label exceeds 70%; spread is within ~1.5 points of even.
(Collected in one pass, so intermediate @50/@100/@150 checkpoints were not separately recorded;
final distribution confirms balance was maintained throughout.) 19 rows carry annotation notes.

### Difficult Cases (3+ required; documented here + in CSV `notes`)
1. **"The Swiss should be ashamed for letting a team as obviously poor as Qatar steal a point. Qatar spent half that match looking lost on the pitch and concede almost 30 shots."** — considered `analysis` vs `hot_take` → chose **`hot_take`**: it cites match evidence (≈30 shots), but the sweeping "should be ashamed" verdict is disproportionate to that evidence, so the stat functions as decoration (Edge Case 1).
2. **"Taking the title as the team with the most World Cup goals over Brazil with a 7-1 score is hilarious."** — considered `hot_take` vs `reaction` → chose **`reaction`**: contains a comparison and a statistic, but uses them as a humorous emotional observation rather than a claim about team quality or ability (Edge Case 2).
3. **"I have never in my life seen the US play like that. Holy Shit"** — considered `reaction` vs `hot_take` → chose **`reaction`**: implies surprise at an unusual performance but makes no explicit judgment of quality, ability, or cause (Edge Case 2).
4. **"It wasn't a chore to watch the USA play."** — considered `reaction` vs `hot_take` → reclassified to **`hot_take`**: a positive evaluation of watchability is an evaluative claim, kept consistent with "What a great World Cup so far" (Edge Case 2 review during QA).

## Sprint History
- Scaffold initialized
- Sprint 1 drafted (2026-06-22): community = r/soccer; labels = analysis/hot_take/reaction;
  edge rules, stress-test, and planning.md complete. Q-001–Q-004 answered; DEC-006/007 logged.
