# Sequence-Level AWS CloudTrail Benchmark

A sequence-level AWS CloudTrail benchmark for studying threat detection under dual-use API behavior.

This repository accompanies the manuscript:

**Sequence-Level AWS CloudTrail Threat Detection with Retrieval-Augmented Large Language Models**

by Yeeun Shin and Seongmin Kim.

## Overview

The benchmark represents each AWS CloudTrail event using the compact representation:

    eventSource:eventName

Each sample is stored as a temporally ordered sequence of normalized AWS API events.

The benchmark contains 259 sequences.

| Category | Count |
| --- | ---: |
| Malicious Base Sequence | 34 |
| Malicious Combination Sequence | 100 |
| Benign Base Sequence | 25 |
| Benign Combination Sequence | 100 |
| Total | 259 |

The benchmark is designed for controlled evaluation of dual-use AWS APIs that can occur in both malicious attack workflows and legitimate administrative operations.

## Dataset Structure

    dataset/
    ├── malicious/
    │   ├── base/
    │   └── combination/
    └── benign/
        ├── base/
        └── combination/

The released dataset contains:

- 34 malicious base sequences
- 100 malicious combination sequences
- 25 benign base sequences
- 100 benign combination sequences

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

Repeated API calls are retained because repetition may reflect discovery, retry, polling, or execution-confirmation behavior.

## Malicious Base Sequences

Malicious base sequences were derived from AWS attack-technique executions using Stratus Red Team v2.31.0.

CloudTrail activity generated during execution was collected and organized using Grimoire.

The temporal order of the observed API calls was preserved.

## Malicious Combination Sequences

Malicious combination sequences connect two or more collected malicious base sequences according to MITRE ATT&CK-informed attack progressions.

The internal temporal order of each constituent base sequence is preserved.

No arbitrary individual API events are synthesized during the combination process.

## Benign Base Sequences

Benign base sequences were collected from administrative workflows executed in AWS.

Representative workflow categories include:

- IAM identity and role lifecycle operations
- access-key management
- AWS Secrets Manager lifecycle operations
- audit and inventory
- monitoring and review
- infrastructure inspection
- security review and cleanup

Security-sensitive dual-use APIs are intentionally included to provide controlled benign workflows that may appear suspicious when interpreted at the individual-event level.

## Benign Combination Sequences

Benign combination sequences connect multiple benign base workflows to represent consecutive administrative activities.

These sequences provide longer benign operational flows containing multiple APIs that may also appear in attack scenarios.

## Release Scope

This repository releases only the compact normalized representation used in the associated experiments.

Raw CloudTrail JSON records are not included.

The released sequence files intentionally exclude event-specific fields such as:

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

See `docs/privacy.md` for details.

## Metadata

Metadata for the released sequences is provided under the `metadata/` directory.

The file `metadata/sequences.csv` contains one row per sequence with information including:

- file name
- relative path
- label
- sequence type
- number of API events

`metadata/malicious_tactic_mapping.csv` provides MITRE ATT&CK tactic assignments for the 34 malicious base sequences.

## Validation

The repository provides a dataset validation script:

    python3 scripts/validate_dataset.py

The script checks:

- expected sequence counts
- eventSource:eventName formatting
- unexpected sensitive-data patterns
- total released sequence count

## Intended Use

This benchmark is intended for research on:

- AWS CloudTrail threat detection
- sequence-level cloud security analysis
- LLM-based log analysis
- dual-use API behavior
- false-positive analysis
- retrieval-augmented security reasoning
- event-level versus sequence-level representations

## Limitations

This is a controlled research benchmark and should not be interpreted as representative of the complete distribution of production AWS activity.

See `docs/limitations.md` for details.

## Documentation

- `DATA_CARD.md`
- `docs/construction.md`
- `docs/privacy.md`
- `docs/limitations.md`

## Citation

Citation information is provided in `CITATION.cff`.

## License

This dataset is released under the Creative Commons Attribution 4.0 International (CC BY 4.0) license. See `LICENSE` for details.
