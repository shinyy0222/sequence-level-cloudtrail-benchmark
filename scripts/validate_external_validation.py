from pathlib import Path
from collections import Counter
import csv
import sys

ROOT = Path("external_validation")

single_path = ROOT / "single_event/attack_relevant_events_50.csv"
seq_path = ROOT / "sequence/attack_workflows_50.csv"
overall_path = ROOT / "results/overall_metrics.csv"
source_path = ROOT / "results/source_metrics.csv"

def read_csv(path):
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

single = read_csv(single_path)
seq = read_csv(seq_path)
overall = read_csv(overall_path)
source = read_csv(source_path)

errors = []

# Single-event
if len(single) != 50:
    errors.append(
        f"Single-event rows: expected 50, found {len(single)}"
    )

single_labels = Counter(r.get("label", "") for r in single)
single_frameworks = Counter(r.get("framework", "") for r in single)
single_categories = Counter(r.get("category", "") for r in single)

if single_labels != {"Malicious": 50}:
    errors.append(f"Unexpected single labels: {single_labels}")

if single_frameworks != {
    "CloudGoat": 25,
    "AtomicRedTeam": 25,
}:
    errors.append(
        f"Unexpected single framework counts: {single_frameworks}"
    )

if single_categories != {
    "malicious_attack_relevant": 50
}:
    errors.append(
        f"Unexpected single categories: {single_categories}"
    )

# Sequence
if len(seq) != 50:
    errors.append(
        f"Sequence rows: expected 50, found {len(seq)}"
    )

seq_labels = Counter(r.get("label", "") for r in seq)
seq_frameworks = Counter(r.get("framework", "") for r in seq)

if seq_labels != {"Malicious": 50}:
    errors.append(f"Unexpected sequence labels: {seq_labels}")

if seq_frameworks != {
    "CloudGoat": 25,
    "AtomicRedTeam": 25,
}:
    errors.append(
        f"Unexpected sequence framework counts: {seq_frameworks}"
    )

# Result sanity checks
expected_overall = {
    "Single-event Prompt-only": (50, 37, 13, 0.74),
    "Sequence Prompt-only": (50, 42, 8, 0.84),
    "Sequence + RAG": (50, 44, 6, 0.88),
}

for r in overall:
    method = r.get("experiment")

    if method not in expected_overall:
        continue

    exp_n, exp_tp, exp_fn, exp_recall = expected_overall[method]

    got = (
        int(r["N"]),
        int(r["TP"]),
        int(r["FN"]),
        float(r["Recall"]),
    )

    expected = (
        exp_n,
        exp_tp,
        exp_fn,
        exp_recall,
    )

    if got != expected:
        errors.append(
            f"{method}: expected {expected}, found {got}"
        )

print("External Single-event samples:", len(single))
print("  CloudGoat:", single_frameworks["CloudGoat"])
print("  Atomic Red Team:", single_frameworks["AtomicRedTeam"])

print("External sequence workflows:", len(seq))
print("  CloudGoat:", seq_frameworks["CloudGoat"])
print("  Atomic Red Team:", seq_frameworks["AtomicRedTeam"])

print()
print("Overall result rows:", len(overall))
print("Source result rows:", len(source))

if errors:
    print("\nFAILED")
    for error in errors:
        print(" -", error)
    sys.exit(1)

print("\nPASS: external validation release is consistent.")
