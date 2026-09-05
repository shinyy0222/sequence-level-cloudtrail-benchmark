from pathlib import Path
import re
import sys

ROOT = Path("raw")

ACCOUNT = re.compile(r"(?<!\d)\d{12}(?!\d)")
ACCESS = re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")
IPV4 = re.compile(
    r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])"
)

mal = sorted((ROOT / "malicious/base").glob("*.json"))
ben = sorted((ROOT / "benign/base").glob("*.json"))

print("Malicious raw:", len(mal))
print("Benign raw:", len(ben))
print("Total raw:", len(mal) + len(ben))

if len(mal) != 34 or len(ben) != 25:
    print("FAILED: unexpected raw file count")
    sys.exit(1)

problems = []

for p in mal + ben:
    text = p.read_text(encoding="utf-8")

    for name, pattern in [
        ("12-digit account ID", ACCOUNT),
        ("AWS access key", ACCESS),
        ("IPv4 address", IPV4),
    ]:
        if pattern.search(text):
            problems.append((p, name))

if problems:
    print("\nFAILED: possible sensitive values remain")
    for p, kind in problems:
        print(p, "|", kind)
    sys.exit(1)

print("PASS: raw release validation succeeded")
