# Groq Baseline Prompt (Sprint 3, Colab Section 5)

Zero-shot classification prompt for the baseline model (Groq `llama-3.3-70b-versatile`,
DEC-004). Built from the locked label definitions in [label-taxonomy.md](label-taxonomy.md)
and the baseline prompt rules in [evaluation-plan.md](evaluation-plan.md).

**Run this baseline (Section 5) on the test set BEFORE fine-tuning (Section 3).**

## Label map (Section 1 — case-sensitive, must match the CSV exactly)
```python
label_map = {"analysis": 0, "hot_take": 1, "reaction": 2}
```

## System message
```
You are a text classifier for r/soccer posts. Classify each post as exactly one of three labels based on these definitions:

analysis: The post supports a claim about soccer with specific, checkable evidence — a statistic, a named tactical mechanism, or an explicit cause-and-effect — and the conclusion is proportional to that evidence.

hot_take: The post makes a strong subjective verdict or evaluative/comparative claim about a player, team, or manager, stated WITHOUT proportional supporting evidence.

reaction: The post expresses emotion about a moment, result, or match and makes NO evaluative claim about quality, ability, or cause.

Decision rules for borderline posts:
- If a post cites a stat but uses it only to decorate a sweeping, unsupported verdict, label it hot_take (not analysis).
- If a post contains any evaluative or comparative claim — even a short insult — label it hot_take (not reaction).

Output ONLY the label name: analysis, hot_take, or reaction. No explanation, no punctuation, no extra words.
```

## User message
```
Post: {text}
```

## Dry run (taxonomy example posts)
| Input post (`{text}`) | Expected output |
|---|---|
| "Rodri's progressive passes per 90 (8.4) vs his replacement's (4.1) explains why City's midfield control collapsed. Without a pivot who can receive on the half-turn under pressure, they're forced into longer, lower-percentage switches." | `analysis` |
| "Pep is overrated and would win nothing without a billion-pound squad. Any decent manager wins the league with that City team." | `hot_take` |

Output is a single lowercase label matching the label map exactly, so the notebook parser
reads it cleanly.

## Parse-failure guard (RISK-006)
- Test with 3–5 examples manually before running the full test set.
- If >10% of responses are unparseable (explanations, punctuation, reformatted names),
  reinforce the "Output ONLY the label name" instruction and re-test before proceeding.

## AI usage disclosure
This prompt was drafted with Claude (Builder role) and is reproduced here for the README
AI-usage section. The Groq API key lives only in Colab Secrets — never in code or committed
to GitHub (DEC-005).
