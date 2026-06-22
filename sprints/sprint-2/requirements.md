# Sprint 2 — Requirements

## What Is Being Built
A labeled dataset of 200+ posts in a single CSV file, with balanced label distribution and documented difficult cases.

## Scope
| In Scope                                              | Out of Scope                          |
|-------------------------------------------------------|---------------------------------------|
| Collect 200+ posts from chosen community              | Any Colab work                        |
| Label each post using taxonomy from Sprint 1          | Fine-tuning or baseline               |
| Save as single CSV: text, label, notes columns        | Changing label definitions*           |
| Verify label distribution (no label > 70%)            | README.md                             |
| Document 3+ genuinely difficult cases                 | Stretch features                      |

*If labels need changes after annotation starts, STOP and log the change in decisions.md before continuing.

## Deliverables
1. `data/labeled_posts.csv` — 200+ rows, 3 columns (text, label, notes)
2. Label distribution count logged in planning/state.md
3. 3+ difficult cases documented (text of post, which labels considered, decision made)

## Success Definition
CSV has 200+ examples. No label exceeds 70% of total. You can describe 3 genuinely hard annotation decisions.

---

# Sprint 2 — Blueprint

## Collection Strategy
- Target: ~67–70 examples per label (for 3 labels, 200 total)
- Source: public Reddit posts/comments (no authentication required)
- Method: browse community, copy post text and paste into CSV with label
- Do NOT scrape programmatically unless you know how — manual copy/paste is fine for 200 examples

## Annotation Rules
- Read each post fully before assigning a label — no skimming
- Use decision rules from docs/label-taxonomy.md for borderline cases
- When genuinely unsure: write a note in the `notes` column, pick the closest label, move on
- After every 50 examples, count distribution — if any label >70%, seek more of the underrepresented ones

## CSV Format
```csv
text,label,notes
"actual post text here",analysis,""
"another post text",hot_take,"almost labeled reaction — no emotional language though"
```

## Optional: LLM Pre-Labeling Workflow
If using LLM to pre-label before reviewing:
1. Paste your label definitions + 10–20 unlabeled posts into Claude
2. Ask it to assign one label per post
3. **Review and correct every single pre-assigned label yourself**
4. Track which examples were pre-labeled (add "pre-labeled" to notes column)
5. Disclose this in README AI usage section

## Distribution Check Script
After collecting 200 examples, run this to verify distribution:
```python
import csv
from collections import Counter

with open('data/labeled_posts.csv') as f:
    reader = csv.DictReader(f)
    labels = [row['label'] for row in reader]

counts = Counter(labels)
total = sum(counts.values())
print(f"Total: {total}")
for label, count in counts.items():
    print(f"  {label}: {count} ({count/total*100:.1f}%)")

assert total >= 200, f"Need at least 200 examples, have {total}"
assert all(count/total <= 0.70 for count in counts.values()), "A label exceeds 70% — collect more of underrepresented labels"
print("Distribution check PASSED")
```

---

# Sprint 2 — Acceptance Criteria

- [ ] `data/labeled_posts.csv` exists with 200+ rows
- [ ] CSV has exactly 3 columns: `text`, `label`, `notes`
- [ ] All label values match exactly one of the 3 defined label names (no typos, no variants)
- [ ] Distribution check: no label > 70% of total
- [ ] 3+ difficult cases documented (in notes column + logged in planning/state.md)
- [ ] Git commit: "Sprint 2 complete — 200 examples annotated"

---

# Sprint 2 — Handoff Prompt

> Sprint 2 is primarily a human annotation task. The Builder's role is optional here — it can assist with LLM pre-labeling if the human chooses that workflow.

**HANDOFF PROMPT — SPRINT 2 (optional LLM pre-labeling assistance)**

You are helping pre-label posts for the TakeMeter project. Read these files first:
1. `agents.md`
2. `docs/label-taxonomy.md` (your label definitions and decision rules)

I will paste unlabeled posts below. For each post, assign exactly one label from: [LABEL1, LABEL2, LABEL3].
Output format: one label per line, in the same order as the posts.
Output ONLY the label names — no explanations.

**The human will review and correct every label you assign before it goes into the CSV.**
