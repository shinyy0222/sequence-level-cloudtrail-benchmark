# Sequence-Level AWS CloudTrail Benchmark

A sequence-level AWS CloudTrail benchmark for studying threat detection under dual-use API behavior.

This repository accompanies the manuscript:

**Sequence-Level AWS CloudTrail Threat Detection with Retrieval-Augmented Large Language Models**

by Yeeun Shin and Seongmin Kim.

## Overview

Each AWS CloudTrail event is represented using the compact format:

    eventSource:eventName

Each sample is a temporally ordered sequence of normalized API events.

| Category | Count |
| --- | ---: |
| Malicious Base Sequence | 34 |
| Malicious Combination Sequence | 100 |
| Benign Base Sequence | 25 |
| Benign Combination Sequence | 100 |
| **Total** | **259** |

The benchmark is intended for controlled analysis of dual-use AWS APIs that can occur in both malicious attack workflows and legitimate administrative operations.

## Dataset Version

- Version: 1.0.0
- Initial release: September 2026
- Total sequences: 259

## Data Provenance and Collection Environment

The benchmark was constructed from AWS CloudTrail activity collected in a controlled AWS environment.

### Collection Environment

- AWS Region: `us-east-1`
- CloudTrail multi-region management events
- Global service events enabled
- Released representation: `eventSource:eventName`

### Malicious Data

Malicious base sequences were derived from AWS attack-technique executions using Stratus Red Team v2.31.0.

CloudTrail activity generated during execution was collected and organized using Grimoire.

The temporal order of observed API calls was preserved.

### Benign Data

Benign base sequences were collected from administrative workflows executed in AWS.

The workflows include IAM lifecycle management, access-key management, Secrets Manager lifecycle operations, monitoring, audit, infrastructure review, security review, and cleanup.

### Normalization

Raw CloudTrail events were normalized to:

    eventSource:eventName

Only this normalized representation is released. Raw CloudTrail JSON records are not distributed.

## Dataset Structure

    dataset/
    ├── malicious/
    │   ├── base/
    │   └── combination/
    └── benign/
        ├── base/
        └── combination/

## Sequence Format

Each `.txt` file contains one normalized API event per line.

Example:

    sts.amazonaws.com:GetCallerIdentity
    iam.amazonaws.com:ListUsers
    iam.amazonaws.com:CreateUser
    iam.amazonaws.com:AttachUserPolicy
    iam.amazonaws.com:ListAttachedUserPolicies
    iam.amazonaws.com:DetachUserPolicy
    iam.amazonaws.com:DeleteUser

Repeated API calls are retained.

## Malicious Base Sequences

The benchmark contains 34 malicious base sequences.

Each base sequence is an execution-derived API flow collected from an individual attack-technique execution.

## Malicious Combination Sequences

The 100 malicious combination sequences were constructed from the 34 malicious base sequences.

Two or more collected base sequences were connected according to MITRE ATT&CK-informed attack progressions.

The internal temporal order of every constituent base sequence was preserved.

No arbitrary individual API events were synthesized or inserted during combination.

The resulting samples therefore represent longer attack progressions assembled from execution-derived base flows.

## Benign Base Sequences

The benchmark contains 25 benign base sequences collected from administrative workflows executed in AWS.

Security-sensitive dual-use APIs are intentionally included.

## Benign Combination Sequences

The 100 benign combination sequences were constructed by connecting multiple benign base workflows to represent consecutive administrative activities.

They are intended as controlled, operationally plausible workflows rather than estimates of production workflow prevalence.

## Release Scope

This repository releases only the compact normalized representation used in the associated study.

Raw CloudTrail JSON records are not included.

The released files intentionally exclude event-specific fields such as:

- AWS account identifiers
- IAM user identities
- ARNs
- access keys
- source IP addresses
- request parameters
- resource identifiers
- user agents
- MFA information
- policy documents

See [docs/privacy.md](docs/privacy.md) for details.

## Metadata

The repository provides:

- `metadata/sequences.csv`: one row per sequence with file name, path, label, sequence type, and number of API events.
- `metadata/malicious_tactic_mapping.csv`: MITRE ATT&CK tactic assignments for the 34 malicious base sequences.
- `metadata/dataset.yaml`: dataset composition, provenance, collection settings, and construction rules.

A separate per-combination mapping to exact constituent base-sequence filenames is not included as a release artifact.

## Usage

Example in Python:

    from pathlib import Path

    path = Path(
        "dataset/malicious/base/"
        "aws_defense-evasion_cloudtrail-delete_sequence.txt"
    )

    sequence = [
        line.strip()
        for line in path.read_text().splitlines()
        if line.strip()
    ]

    print(sequence)

This release contains normalized API sequences rather than native CloudTrail JSON and is not intended for direct replay as raw CloudTrail logs.

## Validation

Run:

    python3 scripts/validate_dataset.py

The validation script checks dataset counts, `eventSource:eventName` formatting, common sensitive-data patterns, and dataset consistency.

## Intended Use

This benchmark is intended for research on:

- AWS CloudTrail threat detection
- sequence-level cloud security analysis
- LLM-based log analysis
- false-positive analysis
- dual-use API behavior
- retrieval-augmented security reasoning

## Limitations

This is a controlled research benchmark and should not be interpreted as representative of the complete distribution of production AWS activity.

See [docs/limitations.md](docs/limitations.md).

## Documentation

- [Dataset Card](DATA_CARD.md)
- [Dataset Construction](docs/construction.md)
- [Privacy and Data Release](docs/privacy.md)
- [Limitations](docs/limitations.md)

## Citation

Citation information is provided in [`CITATION.cff`](CITATION.cff).

## License

This dataset is released under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

See [`LICENSE`](LICENSE) for details.
