# Sprint 1 — Requirements

## What Is Being Built
No code. No data collection. This sprint produces two things: a locked label taxonomy and a fully written `planning.md`.

## Business Justification
The spec requires planning.md to be written before collecting a single labeled example. Labels designed without reading real posts are vague and produce inconsistent annotations. The label taxonomy is the most important design decision in the entire project.

## Scope
| In Scope                                              | Out of Scope                          |
|-------------------------------------------------------|---------------------------------------|
| Choose community using docs/community-selection.md    | Any data collection                   |
| Complete 30-post reality check                        | Any Colab notebook work               |
| Define 3 labels with one-sentence definitions         | Fine-tuning or baseline               |
| Write 2 example posts per label                       | README.md                             |
| Write edge case decision rules (minimum 2)            | Stretch features                      |
| Run AI label stress-test, review results              |                                       |
| Fill docs/label-taxonomy.md completely                |                                       |
| Write planning.md — all 6 required sections + AI Tool Plan |                              |
| Log community + labels in planning/decisions.md       |                                       |

## Deliverables
1. `docs/label-taxonomy.md` — fully filled, stress-test logged
2. `planning.md` — all 6 sections + AI Tool Plan, no placeholders
3. `planning/decisions.md` — DEC-006 and DEC-007 filled in
4. `planning/questions.md` — Q-001 and Q-002 marked answered

## Success Definition
You can state your 3 labels with one-sentence definitions from memory. You can name the hardest edge case and recite the decision rule. Two people reading your planning.md label definitions would agree on 90%+ of real posts.

---

# Sprint 1 — Blueprint

## Step 1: Choose Community (Human task)
- Open `docs/community-selection.md`
- Score at least 3 candidate communities against the 5 criteria
- Use the AI exploration prompt with your top 2 candidates
- Complete the 30-post reality check for your chosen community
- Log decision in planning/decisions.md (DEC-006)

## Step 2: Define Labels (Human task with AI assistance)
- Read 30–40 real posts from the community before writing any definitions
- Draft 3 label names and one-sentence definitions
- For each label: find 2 clear example posts, find 1 borderline post
- Write decision rules for the 2 hardest boundary cases
- Run the AI stress-test prompt (see docs/label-taxonomy.md Step 3)
- Review every AI-generated boundary post yourself
- If 3+ posts are hard to classify → tighten definitions before proceeding
- Fill docs/label-taxonomy.md completely
- Log labels in planning/decisions.md (DEC-007)

## Step 3: Write planning.md (Human task with AI assistance)
planning.md must address all 6 required questions substantively:

1. **Community** — what community, why it's a good fit for classification
2. **Labels** — 3 label definitions + 2 example posts each
3. **Hard edge cases** — at least 2 ambiguous post types + decision rules
4. **Data collection plan** — source, target count per label, what to do if underrepresented
5. **Evaluation metrics** — which metrics, why each one (accuracy alone is not enough)
6. **Definition of success** — specific numeric thresholds (fill Q-004 first)

Plus the **AI Tool Plan** section covering:
- Label stress-testing: which AI tool, what prompt, what you'll do with results
- Annotation assistance: whether you'll use LLM pre-labeling, which tool, how you'll track it
- Failure analysis: which AI tool, what you'll paste in, how you'll verify patterns

---

# Sprint 1 — Acceptance Criteria

## Definition of Done

### AC-1: Community + Labels
- [ ] Community chosen, 30-post reality check passed
- [ ] 3 labels defined — each has a one-sentence definition with an explicit decision boundary
- [ ] 2 clear example posts per label identified from real community content
- [ ] Minimum 2 edge case decision rules written
- [ ] AI stress-test completed — results logged in docs/label-taxonomy.md
- [ ] DEC-006 and DEC-007 logged in planning/decisions.md

### AC-2: planning.md
- [ ] All 6 required sections filled — zero placeholders or "TBD"s
- [ ] Label definitions precise enough that two people would agree on 90%+ of posts
- [ ] Success criteria include specific numeric thresholds (not "good accuracy")
- [ ] AI Tool Plan covers all 3 uses: stress-testing, annotation assistance, failure analysis
- [ ] Data collection plan specifies source and target count per label

### AC-3: No Data Collected Yet
- [ ] labeled_posts.csv does not exist yet
- [ ] No Colab notebook work started

## Git Commit Required
- [ ] Commit: "Sprint 1 complete — labels defined and planning.md written"

---

# Sprint 1 — Handoff Prompt

**HANDOFF PROMPT — SPRINT 1 (planning.md drafting)**

You are the Builder for the TakeMeter fine-tuning project. Before producing anything, read these files in order:

1. `agents.md`
2. `docs/architecture.md`
3. `docs/label-taxonomy.md` (already filled in by the human)
4. `docs/evaluation-plan.md`
5. `planning/decisions.md`
6. `planning/risks.md`
7. `sprints/sprint-1/requirements.md` (this file)

After reading all files, produce a **Dry Run Summary**:
- The exact content you will draft for each of the 6 planning.md sections
- The exact content you will write for the AI Tool Plan section
- What is OUT OF SCOPE (no data, no code, no Colab)
- Any ambiguities or missing information that would prevent you from drafting a complete planning.md

**DO NOT write planning.md yet. Wait for Architect approval of the Dry Run Summary.**

> Note: The human must complete Steps 1 and 2 of the blueprint (community choice + label design) BEFORE issuing this handoff prompt. The Builder needs docs/label-taxonomy.md to be filled in before it can draft planning.md.
