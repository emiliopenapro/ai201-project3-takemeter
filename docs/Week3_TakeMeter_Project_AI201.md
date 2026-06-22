# Week 3 — Model Fine-Tuning
**Course:** AI201 | Applications of AI Engineering  
**Section:** Summer 2026 @ Section 2B | Thursday 5PM – 7PM PT  
**Project Due:** Monday, June 22nd at 2:59AM EDT  
**Estimated Time:** ~9–11 hours total

---

## Overview

> Pre-trained models are generalists. Sometimes you need a specialist.

Fine-tuning is how you take a model trained on the entire internet and make it good at one specific thing: detecting tone in product reviews, classifying support tickets, identifying the quality of a claim. The model doesn't start from zero — it starts from a foundation of general language understanding and learns the specific distinctions you care about from your labeled data.

For this project, you're building **TakeMeter**: a fine-tuned classifier that measures discourse quality in an online community of your choice. NBA takes versus analysis. Music theory insights versus hot takes. TV recap reactions versus actual critique. You define the labels, collect and annotate real posts, run the fine-tuning pipeline, and then honestly compare your model to a zero-shot baseline.

> **Why this matters:** Fine-tuning is what makes AI tools actually useful in specialized domains — legal document analysis, medical coding, financial sentiment, content moderation. The skill that matters most here isn't running the training pipeline — it's **data quality**. The teams building the most effective models in industry spend far more time on label design, annotation consistency, and failure analysis than they do on model architecture.

---

## Learning Objectives

By the end of this week, you will be able to:

- Design a label taxonomy for a classification task, including edge case handling
- Curate and annotate a dataset that is balanced, consistent, and grounded in real text
- Run a fine-tuning pipeline and produce a model that can be evaluated on held-out data
- Compare a fine-tuned model to a zero-shot baseline and interpret what the difference reveals
- Analyze failure modes in model predictions and connect them to specific properties of the labels or data

**What you're building:** A fine-tuned text classifier with a designed label taxonomy, a hand-annotated dataset, a baseline comparison, and an evaluation report that analyzes where the model fails and why.

---

## Session Info

- 🗓️ Thursday, June 18th at 8:00PM EDT
- 📊 Link to Slides *(see course portal)*

---

## Show What You Know: TakeMeter

Online communities run on opinions — NBA subreddits, music theory Discord servers, reality TV recap forums, anime discussion boards. Some posts are insightful. Some are hyperbole. Some are just noise. But what makes a good take is genuinely hard to define — it's specific to the community, the context, and the moment.

In this project, you'll build **TakeMeter**: a fine-tuned text classifier that evaluates discourse quality in an online community of your choosing. You'll define the labels, collect and annotate the data, fine-tune a model, and then honestly assess where it works and where it falls apart.

The hardest part of this project isn't the training pipeline. It's the **label design** — deciding what you're measuring, what counts as an example, and what to do with the cases that don't fit cleanly.

---

## Goals

By completing this project, you will be able to:

- Design a label taxonomy for a classification task, including edge case handling
- Curate and annotate a training dataset from real-world text
- Run a fine-tuning pipeline and produce a usable model
- Evaluate model performance with appropriate metrics and interpret failure modes
- Articulate the gap between what a model learns and what you intended it to learn

---

## Features

### Required Features

**1. Label taxonomy (2–4 labels)**

Define 2–4 labels that capture meaningful distinctions in your chosen community's discourse. Labels must be:
- **Mutually exclusive:** a post should belong to exactly one label
- **Exhaustive enough:** you should be able to label at least 90% of posts without creating a catch-all "other" bucket
- **Grounded in community norms:** the distinction should matter to people who actually participate in that community

Document your labels, definitions, and examples in your `planning.md` and README.

**2. Annotated dataset (at least 200 examples)**

Collect and label at least 200 examples (posts or comments) from your chosen community. Split into train, validation, and test sets. In your README, document:
- Where you collected the data
- Your labeling process
- Your label distribution (count per label)
- At least 3 examples you found genuinely difficult to label and what you decided

**3. Fine-tuning pipeline**

Fine-tune `distilbert-base-uncased` (or another pre-trained model of your choice) on your labeled dataset. Your README must describe:
- The model you started from
- The training approach
- At least one key hyperparameter decision you made (e.g., learning rate, number of epochs, batch size)

**4. Baseline comparison**

Compare your fine-tuned model to a zero-shot baseline: prompt Groq's `llama-3.3-70b-versatile` to classify each test example with no task-specific training. Your evaluation report must show both models' performance on the same test set.

**5. Evaluation report**

Report performance metrics on your test set for both models. Include at minimum:
- Overall accuracy for both models
- At least one per-class metric (precision, recall, or F1)
- A confusion matrix or equivalent table
- At least 3 specific examples the model got wrong with your analysis of why
- A reflection on what the model learned vs. what you intended it to learn

---

### Stretch Features

Complete any of these for extra credit. Update your `planning.md` before starting each one.

- **Inter-annotator reliability:** Have at least one other person label 30+ of your examples independently, and report your agreement rate (Cohen's kappa or simple percentage agreement). Analyze where you disagreed.
- **Confidence calibration:** Report whether your model's confidence scores are meaningful — does a 90% confident prediction actually get it right more often than a 60% confident one?
- **Error pattern analysis:** Go beyond listing individual wrong predictions — identify a systematic pattern in the errors (e.g., "the model consistently misclassifies sarcastic posts").
- **Deployed interface:** Build a simple interface that accepts a new post, runs it through the classifier, and displays the label and confidence. Commit the interface code to your repo and document how to run it in your README.

---

## Hints

- Your labels are the most important design decision in this project. If your labels are vague, your model will learn something vague. Spend more time on label design than you think you need to.
- Label distribution matters. If 80% of your examples carry one label, your model will learn to predict that label constantly. Aim for at least 20% per label.
- The baseline comparison is not a formality — it tells you whether fine-tuning actually helped and by how much. Run it honestly.
- Wrong predictions are your most valuable data. The model's mistakes reveal what it actually captured, which is often not exactly what you intended.
- If your model is performing suspiciously well (>95% accuracy on a hard subjective task), check whether your test set leaked into training, or whether your labels are too easy.
- Collect your data before you start labeling. Read 30–40 examples first to check that your labels actually apply cleanly to real posts — you may need to revise them before committing to annotating 200.

---

## Strong vs. Weak Label Taxonomies

The single most important design decision in this project is your labels.

**❌ Weak taxonomy (too vague):**
- `good` — a quality post
- `bad` — a low-quality post

This fails because "quality" is entirely in the eye of the beholder. Two annotators will apply it differently, and the model will learn an inconsistent signal.

**✅ Strong taxonomy (precise and grounded):**
- `analysis` — the post makes a structured argument backed by statistics, historical comparison, or tactical observation. Evidence is specific and verifiable.
- `hot_take` — a bold, confident opinion stated without supporting evidence. The claim might be true, but the post asserts rather than argues.
- `reaction` — an immediate emotional response to a specific event. Little to no argument — the post is expressing a feeling in the moment.

These work because: (1) you can state the decision boundary in a sentence, (2) two people reading the definitions would agree on most examples, and (3) the distinctions reflect how people in the community actually talk about discourse quality.

**What makes labels too vague:**
- Relying on subjective words without definition: "insightful," "toxic," "engaging"
- Labels that overlap: if a post can reasonably belong to two labels, the boundary isn't precise enough
- Labels too broad to apply: if one label captures 80% of posts, it's not distinguishing anything

### Handling Ambiguous Posts

Some posts genuinely sit at the boundary between two labels. That's not a flaw — it's a signal that your taxonomy needs an explicit decision rule for that case.

**Example ambiguous post (NBA community):**
> "LeBron is overrated — his playoff win rate against top-seeded opponents is below .500."

Is this `hot_take` (bold claim, accusatory framing) or `analysis` (cites a specific stat)?

**Decision rule:** If the post provides specific, verifiable evidence that would support the claim even if you removed the opinion framing, label it `analysis`. If the evidence is vague, cherry-picked, or decorative — just enough to sound credible but not genuinely reasoning — label it `hot_take`. The one-stat post above is borderline; the framing is accusatory and the stat is selected for effect → `hot_take`.

Before committing to your labels, find one post like this in your community. Write down which labels it could belong to, and write the decision rule you'll use.

---

## Tools and Setup

This project uses a free tool stack — no paid subscriptions or API credits required beyond your existing Groq account.

### Recommended Stack

| Component | Tool | Notes |
|---|---|---|
| Base model | `distilbert-base-uncased` | HuggingFace — free to download, no account needed |
| Fine-tuning | Google Colab (free GPU) | Free T4 GPU; fine-tuning DistilBERT on 200 examples takes ~5–15 min |
| Training libraries | `transformers` + `datasets` + `scikit-learn` | Pre-installed on Colab — no setup needed |
| Baseline LLM | Groq (`llama-3.3-70b-versatile`) | Free tier — same account as Projects 1–2 |

### Getting Started

1. Make a copy of the starter Colab notebook. Go to the TakeMeter starter notebook and click **File → Save a copy in Drive**. This gives you your own editable copy.

2. Set your runtime to T4 GPU. In your copy, go to **Runtime → Change runtime type**, select **T4 GPU**, and click Save. Do this before running any cells.

3. Add your Groq API key using Colab Secrets (recommended over pasting it directly):
   - Click the 🔑 icon in the left sidebar
   - Add a secret named `GROQ_API_KEY` with your key as the value
   - Enable notebook access for the secret

4. Create a GitHub repository for everything that lives outside the notebook: your `planning.md`, labeled dataset CSV, README, and the output files you'll download from Colab (`evaluation_results.json`, `confusion_matrix.png`). Name it something like `ai201-project3-takemeter`.

---

## Milestones

### Milestone 1: Choose Your Community and Define Your Labels
⏰ ~45 min

Before touching any code or data, make two decisions: what community you'll study, and what you'll measure. These decisions constrain everything downstream — your data sources, your annotation effort, your model's learning task, and what your evaluation actually tells you.

**Tasks:**

- Choose one online community where discourse is active, text-heavy, and varied in quality. Strong options include:
  - Sports subreddits (`r/nba`, `r/soccer`, `r/fantasyfootball`) where "hot take vs. analysis" is a real distinction
  - Music communities (`r/LetsTalkMusic`, `r/indieheads`) where "opinion vs. argument" matters
  - TV and film fan spaces (`r/television`, `r/TrueFilm`) where discourse ranges from reaction to critique
  - Gaming communities (`r/smashbros`, `r/leagueoflegends`) where you can distinguish tips/strategy from hype

- Read 30–40 posts from your chosen community **before** committing to labels. Don't design labels from memory — read the actual text and see what patterns emerge.

- Define 2–4 labels. For each label, write:
  - A one-sentence definition
  - 2 example posts that clearly belong to it
  - 1 post you're not sure about (this is the most important — it forces you to sharpen the boundary)

- Check your labels for mutual exclusivity: can you pick a random post and assign it to exactly one label without ambiguity most of the time?

- Write a 2–3 sentence description of your community, your labels, and why these distinctions matter to people in that community. You'll use this in your `planning.md`.

**Checkpoint:** You can state your 2–4 labels with one-sentence definitions and 2 concrete examples each. You can name the hardest anticipated edge case and explain how you'll handle it. If you can't name a hard case, you haven't thought hard enough about your label boundaries yet.

---

### Milestone 2: Write Your Spec Before Any Code
⏰ ~45 min

Write your `planning.md` before you collect a single labeled example. There is no template for this document — you design the structure yourself.

**Tasks:**

- Create `planning.md` in your repo root. At minimum, your document must substantively address these six questions:
  1. **Community:** What community did you choose and why? Why is it a good fit for a classification task?
  2. **Labels:** What are your 2–4 labels? Define each in a complete sentence. Include 2 example posts per label.
  3. **Hard edge cases:** What type of post will be genuinely ambiguous between two labels? How will you handle it during annotation?
  4. **Data collection plan:** Where will you collect examples? How many per label? What will you do if a label is underrepresented after 200 examples?
  5. **Evaluation metrics:** Which metrics will you use and why? (Accuracy alone is not enough — explain what else you need and why.)
  6. **Definition of success:** What performance would make this classifier genuinely useful? What would you accept as "good enough" for deployment?

- Review your evaluation plan: are your success criteria specific enough that you could objectively determine at the end whether you hit them?

- Add an **AI Tool Plan** section to your `planning.md`. Cover the three places where AI tools actually help in this project:
  - **Label stress-testing:** Give the AI your label definitions and edge case description, and ask it to generate 5–10 posts that sit at the boundary between two labels. If it produces posts you can't classify cleanly, your definitions need tightening.
  - **Annotation assistance:** Decide whether you'll use an LLM to pre-label a batch of examples before reviewing them yourself. If yes, note which tool you'll use and how you'll track which examples were pre-labeled.
  - **Failure analysis:** Plan to give your list of wrong predictions to an AI tool and ask it to identify patterns. Note what you'll look for and how you'll verify the patterns yourself.

- Update `planning.md` before starting any stretch features later.

**Checkpoint:** `planning.md` contains all six required questions with substantive, specific answers. Your label definitions are precise enough that two people reading them would agree on most examples. Your success criteria define a specific performance threshold. Your AI Tool Plan covers label stress-testing, annotation assistance, and failure analysis.

---

### Milestone 3: Collect and Annotate Your Dataset
⏰ ~3–4 hours

Data collection and annotation is the most time-consuming part of this project — and the most important. The model can only learn what your labels actually capture.

**Tasks:**

- Collect at least 200 posts or comments from your chosen community. Use **public posts only** — no private channels or content behind authentication. Reddit, public Discord servers, fan wikis, and sports comment sections are all valid sources.

- Save your collected examples in a CSV file with at minimum two columns: `text` (the post or comment) and `label` (your string label). Include a third column for notes about difficult cases.
  > The notebook expects a single labeled CSV — it handles the train/validation/test split automatically (70% / 15% / 15%). Do not submit multiple pre-split files.

- Optionally, use an LLM to pre-label a batch of examples before reviewing them yourself — provide it your label definitions from `planning.md` and a set of unlabeled posts and ask it to assign one label per post. **You must review and correct every pre-assigned label.** If you use this workflow, disclose it in your AI usage section.

- Label each example using your definitions from `planning.md`. **Do not label in bulk by skimming** — read each post. Keep a running list of cases that gave you genuine pause: what the post was, which labels it could belong to, and what you decided.

- After labeling, count your examples per label. If any label accounts for more than 70% of your dataset, collect more examples from the underrepresented labels before moving on.

**Checkpoint:** You have at least 200 labeled examples saved in a single CSV file. Your label distribution shows no single label above 70% of the dataset. You have documented at least 3 specific examples that were difficult to label and what you decided — these go in your `planning.md`.

---

### Milestone 4: Run Your Baseline
⏰ ~1 hour

Before fine-tuning, establish a baseline so you know what you're trying to beat. Run this on your **locked test set now**, before you touch your training data.

> ⚙️ **Notebook setup:** Section 5 (the baseline) depends on variables created in earlier sections. You need to run Sections 1 and 2 first, even though you're not fine-tuning yet.

**Tasks:**

- Open your copy of the starter Colab notebook. Confirm the runtime is set to T4 GPU before running any cells.

- **Run Section 1:** Define your label map and upload your labeled CSV. The notebook will prompt you to upload a file — no manual placement in Colab or Google Drive is required. The notebook handles the train/validation/test split automatically.
  > If your Colab session disconnects or resets, you'll need to re-upload the file and re-run Sections 1 and 2.

- **Run Section 2:** The notebook splits your dataset (70% / 15% / 15%) and tokenizes all splits. Review the split sizes and label distribution to confirm they look reasonable.

- **Open Section 5** of the notebook. Add your Groq API key (via Colab Secrets or directly in the cell — never commit it to GitHub) and write your classification prompt. Your prompt should:
  - Include your label definitions as written in `planning.md`
  - Instruct the model to output only the label name (the notebook's parsing logic depends on a clean, consistent response)

- Run the baseline cells. The notebook will classify every example in your test set, print overall accuracy and per-class metrics, and flag any responses it couldn't parse. If more than ~10% of responses are unparseable, revise your prompt to make the expected output format clearer.

- Reflect briefly: where did the baseline struggle? Are there specific labels it consistently confuses? Write down your hypothesis — you'll test it after fine-tuning.

**Checkpoint:** You have baseline performance numbers on your test set (overall accuracy and per-class breakdown). You have **not** yet looked at the fine-tuned model's performance. The baseline results are saved somewhere you can reference them in the evaluation report.

---

### Milestone 5: Fine-Tune Your Model
⏰ ~1.5–2 hours

Fine-tune `distilbert-base-uncased` on your training data using Google Colab's free T4 GPU. Training takes 5–15 minutes for 200 examples.

> ⚙️ **Before you start:** Sections 1, 2, and 5 are already done from Milestone 4. Do **not** re-run them unless your Colab runtime has reset. If it has: re-upload your CSV, re-run Sections 1 and 2, and re-run Section 5 (re-add your Groq key + prompt) before proceeding — Section 6's comparison and export need your baseline numbers from Section 5.

**Tasks:**

- **Run Section 3:** The notebook loads `distilbert-base-uncased` and fine-tunes it on your training data. The default settings are 3 epochs, learning rate `2e-5`, batch size `16`. If you adjust any hyperparameters, note what you changed and why — this goes in your README.

- **Run Section 4:** The notebook evaluates the fine-tuned model on your test set, prints per-class metrics, and generates a confusion matrix image (`confusion_matrix.png`). Review the wrong predictions — pick 3 to analyze in depth for your README.

- **Run Section 6:** The notebook prints the side-by-side baseline-vs-fine-tuned comparison and writes `evaluation_results.json`.

- Download `evaluation_results.json` and `confusion_matrix.png` from Colab (**Files panel → right-click → Download**) and commit them to your GitHub repo.
  > In Milestone 6 you'll also write the confusion matrix out as a markdown table in your README — that text version is the one that needs to read cleanly in your report, with the committed `confusion_matrix.png` kept as a supplementary copy.

### Reading Evaluation Output

| Scenario | What it means |
|---|---|
| All per-class F1 ≥ 0.70 | Model is learning all distinctions well |
| One class F1 ≈ 0, others fine | Model can't learn that boundary — check labels and examples |
| All classes F1 similar and low | Task may be too hard for 200 examples, or labels are inconsistent |
| Fine-tuned barely beats baseline | Fine-tuning added little — labels may be too easy or too noisy |

- **Precision** for a label = "of all examples the model predicted as this label, what fraction actually were?" High precision, low recall = the model is conservative.
- **Recall** for a label = "of all examples that truly are this label, what fraction did the model catch?" High recall, low precision = the model over-predicts this label.
- **F1** = harmonic mean of precision and recall. Most useful single number per class.
- **Confusion matrix:** rows are true labels, columns are predicted labels. The diagonal is correct predictions. Off-diagonal cells show which labels the model confuses and in which direction.

**Checkpoint:** Fine-tuning completed without error. You have evaluation results on your test set for the fine-tuned model. You can compare these directly to your baseline results from Milestone 4. If the fine-tuned model performs worse than the baseline across the board, investigate before writing your report — check for label leakage, class imbalance, or a training bug.

---

### Milestone 6: Evaluate, Document, and Record
⏰ ~1–2 hours

Write your evaluation report, complete your README, and record your demo. The hardest intellectual work here is the **analysis**: honestly explaining where your model fails and what that reveals about your labels, your data, or the task itself.

> 📂 **Which file does what:**
> - `planning.md` = your design thinking before and during the project — label definitions, edge case rules, data collection plan, evaluation metrics reasoning, AI tool plan, and hard annotation decisions.
> - `README.md` = your final polished documentation for a reader — a summary of what you built, your evaluation results, and your analysis. Think of `planning.md` as your working notes and `README.md` as your final report.

**Tasks:**

- Before writing your analysis, use an AI tool to help surface patterns in your wrong predictions. Paste your misclassified examples into Claude or another LLM and ask it to identify common themes — similar post length, use of sarcasm, a specific label pair that keeps getting confused, short or low-information posts. Then **verify those patterns yourself** by re-reading the examples. Include whatever you find — and whatever you had to correct or discard — in your evaluation report.

- Write your **evaluation report** directly in the README. Include:
  - Overall accuracy for both models
  - Per-class metrics for both models
  - A confusion matrix for your fine-tuned model **written out as a markdown table directly in the README** (not only the `confusion_matrix.png` you committed)
  - At least 3 specific examples the fine-tuned model got wrong, with your analysis of why each failed. Use these guiding questions:
    - Which labels are being confused? Is there one pair that accounts for most of the errors?
    - Why is that boundary hard? Ambiguous language, sarcasm, short posts, topic vs. structure mismatch?
    - Is this a labeling problem or a data problem? Did you label similar posts differently?
    - What would need to change to fix it? More examples? A tighter label definition?

- Include a **Sample Classifications** subsection: a markdown table or list of 3–5 example posts run through your fine-tuned model, each shown with the predicted label and its confidence score. For at least one correctly-predicted example, include a sentence explaining why the prediction is reasonable. Write these out as text (not a screenshot).

- Write a **reflection** on what your model captured vs. what you intended it to capture. This is a higher-level observation about the gap between your label definitions and the model's actual decision boundary. What did the model overfit to? What did it miss?

- Write your **spec reflection** in the README: describe one way the spec helped guide your implementation and one way your implementation diverged from it and why.

- Add the **AI usage section** to your README. Describe at least 2 specific instances: what you directed the AI tool to do, what it produced, and what you changed or overrode. If you used AI assistance during annotation, disclose it here.

- Record a **3–5 minute demo video** showing:
  - 3–5 posts being classified by your fine-tuned model with label and confidence visible
  - One correct prediction with narration of why it's reasonable
  - One incorrect prediction with narration of what went wrong
  - A brief walkthrough of your evaluation report

**Checkpoint:** Evaluation report documents both models with per-class metrics, a confusion matrix, and 3 analyzed failures. Reflection addresses the gap between intended and learned behavior specifically. README covers all required sections. Demo video is recorded and shows all required moments.

---

## Submission Requirements

Submit all of the following through the Course Portal:

1. **Link to your GitHub repository**

2. **`planning.md`** in your repo root (written before data collection, updated before stretch features)

3. **Your labeled dataset** (CSV or JSON) included in the repo or linked from the README

4. **`README.md`** including:
   - Community choice and reasoning
   - Label taxonomy: definitions and 2 examples per label
   - Data collection source, labeling process, label distribution, and 3 difficult-to-label examples with your decisions
   - Fine-tuning approach: base model, training setup, and at least one hyperparameter decision
   - Baseline description: prompt used and how results were collected
   - Full evaluation report: metrics for both models (accuracy + per-class), confusion matrix as a markdown table, 3 specific wrong predictions with analysis, and a sample-classifications table (3–5 posts with predicted label and confidence, one correct example explained)
   - Reflection: what the model learned vs. what you intended
   - Spec reflection: one way the spec helped you, one way implementation diverged from it and why
   - AI usage section: at least 2 specific instances describing what you directed the AI to do and what you revised or overrode; disclose any annotation assistance

5. **Demo video (3–5 minutes)** showing:
   - 3–5 posts being classified by your fine-tuned model with label and confidence visible
   - One correct prediction narrated with explanation
   - One incorrect prediction narrated with explanation of why it went wrong
   - Brief walkthrough of your evaluation report

---

*A detailed breakdown of graded features and points can be found on the course grading page.*
