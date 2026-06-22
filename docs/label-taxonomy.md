# Label Taxonomy

> STATUS: FILLED & ACCEPTED — community chosen (r/soccer, Q-001 resolved).
> Example posts are realistic representations of r/soccer discourse, reviewed and accepted
> by the human on 2026-06-22.

## Community
**Chosen community:** r/soccer
**Why this community:** r/soccer produces a continuous, high-volume stream of public,
text-rich football discussion that spans the full quality spectrum — from rigorous
statistical/tactical breakdowns to one-word emotional outbursts during live matches. That
natural variance is exactly what a discourse-quality classifier needs, and the three labels
below map onto distinctions that real members already feel (the difference between "good
analysis" and "just a hot take" is a recurring meta-conversation in the sub).

---

## Label Definitions

### Label 1: `analysis`
**Definition:** A post that supports a claim about soccer with specific, checkable evidence — a statistic, a named tactical mechanism, or an explicit cause-and-effect — where the conclusion is proportional to the evidence given.
**Example A:** "Arsenal's xG has outpaced their actual goals by 6.2 over the last 10 games. The finishing dip is real, but the underlying numbers say they're still creating enough — teams doubling Saka are pushing Ødegaard into lower-percentage shots from the half-spaces."
**Example B:** "Rodri's progressive passes per 90 (8.4) vs his replacement's (4.1) explains why City's midfield control collapsed. Without a pivot who can receive on the half-turn under pressure, they're forced into longer, lower-percentage switches."
**Does NOT include:** Posts that cite a stat only as decoration for a sweeping verdict the stat doesn't actually support (that is `hot_take`).

---

### Label 2: `hot_take`
**Definition:** A strong subjective verdict or evaluative/comparative claim about a player, team, or manager, stated without proportional supporting evidence.
**Example A:** "Messi was never tested in a real league — Ligue 1 and MLS are retirement homes. Put him in the Premier League in his prime and he disappears like every other flat-track bully."
**Example B:** "Pep is overrated and would win nothing without a billion-pound squad. Any decent manager wins the league with that City team."
**Does NOT include:** Posts that back the verdict with proportional evidence (that is `analysis`), or posts that express only emotion and make no claim at all (that is `reaction`).

---

### Label 3: `reaction`
**Definition:** A post that expresses emotion about a moment, result, or match without making any evaluative claim about quality, ability, or cause.
**Example A:** "OFF THE BAR AND IN. I AM NEVER EMOTIONALLY RECOVERING FROM THIS. LETS GOOOO 🔥🔥🔥"
**Example B:** "Bro I cannot watch this anymore, my heart can't take stoppage time every single week 😭"
**Does NOT include:** Posts that contain any judgment or comparison — even an insulting one like "he's trash" — which carry a claim and belong in `hot_take`.

---

## Edge Case Decision Rules

### Edge Case 1: `hot_take` vs. `analysis`
**Ambiguous post example:** "City's defense is finished, they've conceded in 7 straight games."
**Decision rule:** If the post cites evidence AND the conclusion follows proportionally from that evidence, label `analysis`. If it cites a stat but uses it only as decoration for a sweeping, unsupported verdict (here, "finished" does not follow from a 7-game streak alone), label `hot_take`.

### Edge Case 2: `reaction` vs. `hot_take`
**Ambiguous post example:** "Pickford is so trash lmaooo 😭"
**Decision rule:** If the post makes any evaluative or comparative claim about a player/team/manager — even a short insult — label `hot_take`. If it is pure emotion with no claim about quality or ability, label `reaction`.

---

## Mutual Exclusivity Check
Before annotating, answer these:
- [x] Can I assign exactly one label to 90%+ of posts without ambiguity? **Yes — the two
  decision rules resolve the only systematic overlaps (stat-decorated verdicts; insults).**
- [x] Is any label likely to exceed 70% of the dataset? **No — representative pass was
  40% max (`hot_take`); collection plan caps any label at 70% and targets ~33% each.**
- [x] Do my edge case rules resolve the hardest cases without a catch-all "other" label?
  **Yes — every boundary collapses to evidence-proportionality or claim-vs-emotion.**

---

## Label Stress-Test Log (AI-Assisted)
Definitions pasted into Claude with the request to generate boundary posts. Results:

| Generated Post | My Label | Confident? | Notes |
|----------------|----------|------------|-------|
| "Haaland's underlying numbers are fine, 0.9 npxG/90, the goals will come" | analysis | Yes | Stat + proportional conclusion ("goals will come" follows from npxG). |
| "Haaland is washed, hasn't scored in 4, City wasted their money" | hot_take | Yes | "Washed/wasted money" is a sweeping verdict; 4-game streak doesn't support it. |
| "5 shots, 1 on target, 0 goals — same story every week with this striker" | hot_take | Borderline→Yes | Cites stats but uses them to decorate a verdict ("same story"); Edge Case 1 → hot_take. |
| "I have not blinked since the 80th minute send help" | reaction | Yes | Pure emotion, no claim. |
| "Best defensive performance I've seen from him all season honestly" | hot_take | Borderline→Yes | Evaluative claim with no specific evidence → hot_take, not reaction. |
| "GOAL DISALLOWED ARE YOU KIDDING ME VAR HAS RUINED THIS SPORT" | hot_take | Borderline→Yes | Emotional, but "VAR has ruined this sport" is a claim → hot_take, not reaction. |

**Result:** 2 of 6 were borderline at first read; both resolved cleanly via the two
decision rules. Fewer than 3 remained hard → definitions are tight enough to proceed.
