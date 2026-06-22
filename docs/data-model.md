# Data Model

## labeled_posts.csv — Required Schema

| Column  | Type   | Required | Description                                                    |
|---------|--------|----------|----------------------------------------------------------------|
| `text`  | string | Yes      | The raw post or comment text. No truncation — full text.       |
| `label` | string | Yes      | Exactly one label from your taxonomy (e.g., `analysis`)        |
| `notes` | string | No       | Annotation notes for difficult cases. Empty string if easy.    |

### Example rows
```csv
text,label,notes
"LeBron's playoff efficiency drops 8% against top-4 defenses — here's the breakdown by season.",analysis,""
"Dude is cooked, never winning another ring lol",hot_take,""
"LETS GOOO that dunk was INSANE 🔥🔥🔥",reaction,"almost labeled hot_take but no claim made — pure emotion"
```

## Label Distribution Requirements
- Minimum 200 total examples
- No single label > 70% of dataset
- Aim for at least 20% per label (with 3 labels: ~67 examples each is ideal)
- If a label is under 20% after 150 examples, actively seek more of that type before finishing

## Dataset Split (handled automatically by Colab)
| Split      | Proportion | Approx. count (200 examples) |
|------------|------------|-------------------------------|
| Train      | 70%        | ~140 examples                 |
| Validation | 15%        | ~30 examples                  |
| Test       | 15%        | ~30 examples                  |

> Do NOT manually split the CSV. Upload the full labeled file to Colab Section 1.

## evaluation_results.json — Output Schema
Downloaded from Colab Section 6. Contains:
```json
{
  "baseline": {
    "accuracy": float,
    "per_class": { "label_name": { "precision": float, "recall": float, "f1": float } }
  },
  "finetuned": {
    "accuracy": float,
    "per_class": { "label_name": { "precision": float, "recall": float, "f1": float } }
  }
}
```

## confusion_matrix.png — Output
Downloaded from Colab Section 4. Rows = true labels, columns = predicted labels. Also reproduced as a markdown table in README.md.
