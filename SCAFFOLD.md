# TakeMeter — Scaffold Navigation

> This file is internal Builder navigation. The graded deliverable is `README.md` — fill that out separately.

## What This Is
TakeMeter is a fine-tuned text classifier that measures discourse quality (e.g., hot take vs. analysis vs. reaction) in an online community. The model is trained on hand-annotated real posts and compared against a zero-shot Groq baseline.

## Stack
| Component        | Tool                                      |
|------------------|-------------------------------------------|
| Base model       | `distilbert-base-uncased` (HuggingFace)   |
| Fine-tuning env  | Google Colab (free T4 GPU)               |
| Baseline LLM     | Groq `llama-3.3-70b-versatile`            |
| Training libs    | `transformers`, `datasets`, `scikit-learn`|
| Repo             | GitHub (fresh repo — no fork)             |

## Scaffold Structure
```
/
├── agents.md                  ← Builder reads this first
├── SCAFFOLD.md                ← You are here (internal navigation)
├── docs/                      ← Durable technical blueprints
│   ├── architecture.md
│   ├── data-model.md
│   ├── label-taxonomy.md
│   ├── evaluation-plan.md
│   └── community-selection.md
├── planning/                  ← Operational state and decisions
│   ├── state.md
│   ├── decisions.md
│   ├── risks.md
│   └── questions.md
├── sprints/                   ← Architect Packs
│   ├── sprint-1/              ← Community + labels + planning.md
│   ├── sprint-2/              ← Data collection + annotation
│   ├── sprint-3/              ← Colab baseline + fine-tuning
│   └── sprint-4/              ← Evaluation report + README + demo
├── data/                      ← Your labeled CSV goes here
│   └── labeled_posts.csv
├── planning.md                ← GRADED DELIVERABLE (write this yourself)
├── README.md                  ← GRADED DELIVERABLE (write this yourself)
├── evaluation_results.json    ← Downloaded from Colab (Milestone 5)
└── confusion_matrix.png       ← Downloaded from Colab (Milestone 5)
```

## Colab Notebook
- Make a copy: File → Save a copy in Drive
- Set runtime: Runtime → Change runtime type → T4 GPU
- Add Groq key: 🔑 icon → Add secret named `GROQ_API_KEY`
- Never commit your Groq key to GitHub
