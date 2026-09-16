from pathlib import Path
from collections import Counter
import csv
import sys

ROOT = Path("external_validation")

single_path = ROOT / "single_event/attack_relevant_events.csv"
seq_path = ROOT / "sequence/attack_workflows_50.csv"
final_path = ROOT / "results/final_metrics.csv"
source_path = ROOT / "results/source_metrics.csv"
obsolete_overall_path = ROOT / "results/overall_metrics.csv"


def read_csv(path):
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def as_metric_tuple(row):
    return (
        row.get("framework", ""),
        row.get("role", ""),
        row.get("method", row.get("experiment", "")),
        row.get("unit", ""),
        int(row["N"]),
        int(row["TP"]),
        int(row["FN"]),
        float(row["Recall"]),
    )


single = read_csv(single_path)
seq = read_csv(seq_path)
final_metrics = read_csv(final_path)
source_metrics = read_csv(source_path)

errors = []

# ------------------------------------------------------------------
# Single-event release: 21 CloudGoat + 43 Atomic Red Team = 64 events
# ------------------------------------------------------------------
if len(single) != 64:
    errors.append(f"Single-event rows: expected 64, found {len(single)}")

single_labels = Counter(r.get("label", "") for r in single)
single_frameworks = Counter(r.get("framework", "") for r in single)
single_roles = Counter(r.get("analysis_role", "") for r in single)

if single_labels != Counter({"Malicious": 64}):
    errors.append(f"Unexpected single-event labels: {single_labels}")

if single_frameworks != Counter({"AtomicRedTeam": 43, "CloudGoat": 21}):
    errors.append(f"Unexpected single-event framework counts: {single_frameworks}")

if single_roles != Counter({"held_out_external": 43, "development_generalization": 21}):
    errors.append(f"Unexpected single-event analysis roles: {single_roles}")

single_ids = [r.get("event_id", "") for r in single]
if len(single_ids) != len(set(single_ids)):
    errors.append("Duplicate event_id values found in single-event release")

single_dedup_keys = [
    (r.get("framework", ""), r.get("api_event", ""), r.get("source_sequence_id", ""))
    for r in single
]
if len(single_dedup_keys) != len(set(single_dedup_keys)):
    errors.append(
        "Duplicate (framework, api_event, source_sequence_id) keys found in single-event release"
    )

if any(not r.get("api_event", "") for r in single):
    errors.append("Missing api_event value in single-event release")

# ------------------------------------------------------------
# Sequence release: 25 CloudGoat + 25 Atomic Red Team = 50
# ------------------------------------------------------------
if len(seq) != 50:
    errors.append(f"Sequence rows: expected 50, found {len(seq)}")

seq_labels = Counter(r.get("label", "") for r in seq)
seq_frameworks = Counter(r.get("framework", "") for r in seq)
seq_roles = Counter(r.get("analysis_role", "") for r in seq)

if seq_labels != Counter({"Malicious": 50}):
    errors.append(f"Unexpected sequence labels: {seq_labels}")

if seq_frameworks != Counter({"CloudGoat": 25, "AtomicRedTeam": 25}):
    errors.append(f"Unexpected sequence framework counts: {seq_frameworks}")

if seq_roles != Counter({"development_generalization": 25, "held_out_external": 25}):
    errors.append(f"Unexpected sequence analysis roles: {seq_roles}")

seq_ids = [r.get("sample_id", "") for r in seq]
if len(seq_ids) != len(set(seq_ids)):
    errors.append("Duplicate sample_id values found in sequence release")

if any(not r.get("api_sequence", "") for r in seq):
    errors.append("Missing api_sequence value in sequence release")

atomic_seq = [r for r in seq if r.get("framework") == "AtomicRedTeam"]
if Counter(r.get("source_type", "") for r in atomic_seq) != Counter({"actual_base_combination": 25}):
    errors.append(
        "Atomic Red Team sequence source_type must be actual_base_combination for all 25 rows"
    )

# ---------------------------------------------
# Final paper-facing source-specific metrics
# ---------------------------------------------
expected_metrics = {
    ("CloudGoat", "development_generalization", "Single-event Prompt-only", "event", 21, 13, 8, 0.619),
    ("CloudGoat", "development_generalization", "Sequence Prompt-only", "sequence", 25, 18, 7, 0.720),
    ("CloudGoat", "development_generalization", "Sequence with RAG", "sequence", 25, 15, 10, 0.600),
    ("AtomicRedTeam", "held_out_external", "Single-event Prompt-only", "event", 43, 35, 8, 0.814),
    ("AtomicRedTeam", "held_out_external", "Sequence Prompt-only", "sequence", 25, 25, 0, 1.000),
    ("AtomicRedTeam", "held_out_external", "Sequence with RAG", "sequence", 25, 19, 6, 0.760),
}

final_set = {as_metric_tuple(r) for r in final_metrics}
source_set = {as_metric_tuple(r) for r in source_metrics}

if final_set != expected_metrics:
    errors.append(f"final_metrics.csv does not match expected final metrics: {final_set}")

if source_set != expected_metrics:
    errors.append(f"source_metrics.csv does not match expected final metrics: {source_set}")

if obsolete_overall_path.exists():
    errors.append(
        "Obsolete results/overall_metrics.csv is present; pooled recall is not used in the final protocol"
    )

print("External Single-event samples:", len(single))
print("  CloudGoat:", single_frameworks["CloudGoat"])
print("  Atomic Red Team:", single_frameworks["AtomicRedTeam"])

print("External sequence workflows:", len(seq))
print("  CloudGoat:", seq_frameworks["CloudGoat"])
print("  Atomic Red Team:", seq_frameworks["AtomicRedTeam"])

print("Final metric rows:", len(final_metrics))
print("Source metric rows:", len(source_metrics))

if errors:
    print("\nFAILED")
    for error in errors:
        print(" -", error)
    sys.exit(1)

print("\nPASS: external validation release is consistent with the final protocol.")
