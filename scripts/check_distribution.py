"""
Sprint 2 distribution check for TakeMeter (data/labeled_posts.csv).

Validates the four things Sprint 2 acceptance cares about:
  1. >= 200 rows
  2. exactly the columns: text, label, notes
  3. every label is exactly one of the 3 defined labels (no typos/variants)
  4. no single label exceeds 70% of the dataset

Usage (from repo root):
    python scripts/check_distribution.py
    python scripts/check_distribution.py path/to/other.csv
"""

import csv
import sys
from collections import Counter

VALID_LABELS = {"analysis", "hot_take", "reaction"}
EXPECTED_COLUMNS = ["text", "label", "notes"]
MIN_ROWS = 200
MAX_SHARE = 0.70


def main(path: str = "data/labeled_posts.csv") -> int:
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        columns = reader.fieldnames or []
        rows = list(reader)

    problems = []

    # 2. columns
    if columns != EXPECTED_COLUMNS:
        problems.append(f"Columns must be exactly {EXPECTED_COLUMNS}, found {columns}")

    labels = [(_r.get("label") or "").strip() for _r in rows]
    counts = Counter(labels)
    total = len(rows)

    print(f"Total rows: {total}")
    for label, count in sorted(counts.items()):
        share = (count / total * 100) if total else 0
        flag = "  <-- INVALID LABEL" if label not in VALID_LABELS else ""
        print(f"  {label or '(blank)'}: {count} ({share:.1f}%){flag}")

    notes_filled = sum(1 for _r in rows if (_r.get("notes") or "").strip())
    print(f"Rows with notes (difficult-case candidates): {notes_filled}")

    # 1. count
    if total < MIN_ROWS:
        problems.append(f"Need >= {MIN_ROWS} rows, have {total}")

    # 3. valid labels
    bad = {lbl: c for lbl, c in counts.items() if lbl not in VALID_LABELS}
    if bad:
        problems.append(f"Invalid label values present: {bad}. Allowed: {sorted(VALID_LABELS)}")

    # 4. distribution
    if total:
        over = {lbl: c for lbl, c in counts.items() if c / total > MAX_SHARE}
        if over:
            problems.append(f"Label(s) over {MAX_SHARE:.0%}: {over} -- collect more of the others")

    print()
    if problems:
        print("DISTRIBUTION CHECK FAILED:")
        for p in problems:
            print(f"  - {p}")
        return 1

    print("Distribution check PASSED")
    return 0


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "data/labeled_posts.csv"
    sys.exit(main(target))
