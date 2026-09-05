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

- Version: 1.1.0
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

Malicious base sequences were derived from AWS attack-technique executions using [Stratus Red Team v2.31.0](https://github.com/DataDog/stratus-red-team).

CloudTrail activity generated during execution was collected and organized using [Grimoire](https://github.com/DataDog/grimoire).

The temporal order of observed API calls was preserved.

### Benign Data

Benign base sequences were collected from administrative workflows executed in AWS.

The workflows include IAM lifecycle management, access-key management, Secrets Manager lifecycle operations, monitoring, audit, infrastructure review, security review, and cleanup.

### Normalization

Raw CloudTrail events were normalized to:

    eventSource:eventName

The primary benchmark representation is the normalized `eventSource:eventName` sequence. Release v1.1.0 additionally provides sanitized raw CloudTrail traces for all 59 base workflows.

## Dataset Structure

<pre>
dataset/
├── malicious/
│   ├── base/
│   └── combination/
└── benign/
    ├── base/
    └── combination/

raw/
├── malicious/
│   └── base/          # 34 sanitized raw traces
├── benign/
│   └── base/          # 25 sanitized raw traces
└── raw_manifest.json
</pre>

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

Two or more collected base sequences were connected according to attack progressions informed by the [MITRE ATT&CK Enterprise Cloud Matrix](https://attack.mitre.org/matrices/enterprise/cloud/).

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

The repository releases the 259 normalized sequence samples used by the benchmark together with sanitized CloudTrail provenance for all 59 base workflows.

The raw release contains:

- 34 malicious base-workflow traces
- 25 benign base-workflow traces

Combination sequences do not have separate raw traces because they are constructed from the collected base workflows.

Environment-specific identifiers and potentially sensitive values in the raw traces are pseudonymized or redacted before publication. The unsanitized source logs are not included.

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

This release contains normalized API sequences together with sanitized raw CloudTrail provenance for the base workflows. The sanitized traces are not exact copies of the private AWS logs because environment-specific identifiers have been pseudonymized or redacted.

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

## Sanitized Raw CloudTrail Traces

Release v1.1.0 provides sanitized raw CloudTrail traces for all 59 base workflows used to construct the benchmark.

The traces are stored under `raw/malicious/base/` and `raw/benign/base/`.

The raw artifacts preserve CloudTrail API semantics while pseudonymizing or redacting environment-specific values such as AWS account identifiers, ARNs, access-key identifiers, principals, usernames, source IP addresses, event/request identifiers, and resource-specific identifiers.

The normalized benchmark continues to use ordered `eventSource:eventName` sequences. Raw scenario traces may contain additional CloudTrail events that are not retained in the normalized benchmark representation. For example, an S3 scenario can contain Data Events in addition to the Management Events used by the benchmark.

Combination sequences are constructed from base workflows and therefore do not have separate raw captures.

