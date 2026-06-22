# Architecture

## Pipeline Overview
```
Online Community Posts (Reddit, Discord, etc.)
        │
        ▼
[Sprint 2] Manual Collection + Annotation
        → labeled_posts.csv (text, label, notes)
        │
        ▼
[Sprint 3 — Colab Section 1+2] Upload CSV + Tokenize
        → Auto-split: 70% train / 15% val / 15% test
        │
        ├──────────────────────────────────────────┐
        │                                          │
        ▼                                          ▼
[Sprint 3 — Colab Section 3+4]          [Sprint 3 — Colab Section 5]
Fine-tune distilbert-base-uncased        Zero-shot Groq baseline
on train set, eval on test set           (llama-3.3-70b-versatile)
        │                                          │
        ▼                                          ▼
[Sprint 3 — Colab Section 6] Side-by-side comparison
        → evaluation_results.json
        → confusion_matrix.png
        │
        ▼
[Sprint 4] Evaluation Report + README + Demo Video
```

## Component Responsibilities
| Component                  | Location          | Responsibility                                      |
|----------------------------|-------------------|-----------------------------------------------------|
| Data collection            | Human task        | Collect 200+ posts from chosen community            |
| Annotation                 | Human task        | Label each post using taxonomy from label-taxonomy.md|
| Labeled dataset            | `data/labeled_posts.csv` | Single CSV with text + label + notes columns  |
| Colab notebook             | Google Colab      | Tokenize, split, fine-tune, evaluate, compare       |
| distilbert-base-uncased    | HuggingFace       | Base model for fine-tuning                          |
| Groq baseline              | Colab Section 5   | Zero-shot classification for comparison             |
| evaluation_results.json    | Repo root         | Downloaded from Colab — both models' metrics        |
| confusion_matrix.png       | Repo root         | Downloaded from Colab — fine-tuned model only       |

## Constraints
- Single CSV file — do NOT pre-split. Notebook splits automatically.
- No label may exceed 70% of total examples.
- Colab session resets lose state — re-upload CSV and re-run Sections 1+2 if disconnected.
- Groq API key goes into Colab Secrets, never in code or committed to GitHub.
