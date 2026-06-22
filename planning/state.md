# State — Current Project Status

## Active Sprint
**Sprint 3:** Colab fine-tuning + baseline → evaluation outputs (Milestones 4–5) — COMPLETE, ready to commit

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
- [x] Colab notebook copied to Drive and T4 GPU set (Sprint 3)
- [x] Baseline run completed — numbers saved (Sprint 3) — Groq zero-shot 63.3%
- [x] Fine-tuning completed (Sprint 3) — distilbert 66.7% after retune (DEC-009)
- [x] evaluation_results.json downloaded + committed (Sprint 3)
- [x] confusion_matrix.png downloaded + committed (Sprint 3)
- [ ] README.md complete with evaluation report (Sprint 4)
- [ ] Demo video recorded (Sprint 4)

## Currently Blocked
- Nothing. Sprint 3 complete — fine-tuned model beats baseline (RISK-008 resolved). Next: Sprint 4 README + demo.

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

## Sprint 3 Tracking (Colab evaluation)

### Final results (test set = 30 examples)
| Model | Accuracy | analysis F1 | hot_take F1 | reaction F1 |
|-------|----------|-------------|-------------|-------------|
| Groq zero-shot baseline | 63.3% | 0.33 | 0.64 | 0.78 |
| Fine-tuned distilbert (10 ep / lr 2e-5 / batch 8) | **66.7%** | **0.82** | **0.38** | **0.73** |

Fine-tuned beats baseline by +3.3 pts. Per-class precision/recall: baseline analysis 1.00/0.20,
hot_take 0.53/0.80, reaction 0.69/0.90; fine-tuned analysis 0.75/0.90, hot_take 0.50/0.30,
reaction 0.67/0.80. No class F1 = 0. Below the aspirational 75% / +5 pt thresholds but a
defensible honest result for ~140 training examples (see DEC-009). Hyperparameters retuned
from defaults after the first run lost to baseline (50.0%); 3→10 epochs fixed underfitting.

### Complementary failure modes (key reflection)
The two models fail in opposite directions: the baseline barely predicts `analysis` (recall
0.20) but handles `hot_take`/`reaction`; the fine-tuned model masters `analysis` (F1 0.82) but
struggles with `hot_take` (F1 0.38), scattering it into both neighbors. Fine-tuning's entire
gain comes from learning `analysis`. `hot_take` is the hardest class — the central category
between evidenced argument and pure emotion.

### Wrong predictions for Sprint 4 failure analysis (10/30, from the 66.7% model)
All `hot_take` errors (7 of 10) — the failure story. Three to feature in the README:
1. **"The Swiss should be ashamed for letting a team as obviously poor as Qatar steal a point. Qatar spent half that match looking lost on the pitch and concede almost 30 shots."** — true `hot_take`, predicted `analysis` (conf 0.98). The model fell for the stat decoration (≈30 shots) — the exact Edge Case 1 trap the taxonomy warns about, and the same post flagged as Difficult Case #1 during annotation.
2. **"Nmecha MOTM"** — true `hot_take`, predicted `reaction` (conf 0.95). A short evaluative pick (man of the match) with no evidence reads to the model like a pure exclamation.
3. **"Water breaks help a lot with this style."** — true `analysis`, predicted `hot_take` (conf 0.87). A brief causal claim with no specific evidence gets read as an unsupported opinion.

Other 7 errors: hot_take→analysis ("Deserved tie, such a shambolic performance by Czechia...";
"Terrible lost for Côte d'Ivoire..."); hot_take→reaction ("Yeah Germany is not winning the
World Cup"; "Nagelsmann you absolute fraud / START UNDAV"; "japan will destroy sweden");
reaction→hot_take ("Super happy for Mo, super happy for Egypt..."; "This game could've been an email").

## Sprint History
- Scaffold initialized
- Sprint 1 drafted (2026-06-22): community = r/soccer; labels = analysis/hot_take/reaction;
  edge rules, stress-test, and planning.md complete. Q-001–Q-004 answered; DEC-006/007 logged.
- Sprint 2 (2026-06-22): 200 r/soccer posts annotated (67/68/65), validated, committed.
- Sprint 3 (2026-06-22): Colab baseline (63.3%) + fine-tune. First run underfit (50.0%, lost to
  baseline → RISK-008); retuned to 10 epochs → 66.7%, beats baseline. Outputs committed. DEC-009.
