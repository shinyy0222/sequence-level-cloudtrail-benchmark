from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "dataset"

EXPECTED_COUNTS = {
    ("malicious", "base"): 34,
    ("malicious", "combination"): 100,
    ("benign", "base"): 25,
    ("benign", "combination"): 100,
}

EVENT_RE = re.compile(
    r"^[A-Za-z0-9._-]+\.amazonaws\.com:[A-Za-z0-9._-]+$"
)

SENSITIVE_PATTERNS = {
    "AWS access key": re.compile(r"(AKIA|ASIA)[A-Z0-9]{16}"),
    "AWS ARN": re.compile(r"arn:aws:"),
    "IPv4 address": re.compile(r"(?:\d{1,3}\.){3}\d{1,3}"),
    "12-digit account-like identifier": re.compile(r"\b\d{12}\b"),
}

errors = []
total = 0

for (label, sequence_type), expected in EXPECTED_COUNTS.items():
    directory = DATASET / label / sequence_type
    files = sorted(directory.glob("*.txt"))

    actual = len(files)
    total += actual

    print(
        f"{label}/{sequence_type}: "
        f"{actual} files (expected {expected})"
    )

    if actual != expected:
        errors.append(
            f"{label}/{sequence_type}: expected {expected}, found {actual}"
        )

    for path in files:
        lines = path.read_text(encoding="utf-8").splitlines()

        if not lines:
            errors.append(f"Empty file: {path.relative_to(ROOT)}")
            continue

        for lineno, line in enumerate(lines, 1):
            event = line.strip()

            if not event:
                errors.append(
                    f"Blank line: {path.relative_to(ROOT)}:{lineno}"
                )
                continue

            if not EVENT_RE.fullmatch(event):
                errors.append(
                    f"Invalid API format: "
                    f"{path.relative_to(ROOT)}:{lineno}: {event}"
                )

            for name, pattern in SENSITIVE_PATTERNS.items():
                if pattern.search(event):
                    errors.append(
                        f"Possible {name}: "
                        f"{path.relative_to(ROOT)}:{lineno}: {event}"
                    )

print(f"Total sequences: {total} (expected 259)")

if total != 259:
    errors.append(f"Expected 259 total sequences, found {total}")

if errors:
    print("\nValidation FAILED:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("\nValidation PASSED.")
