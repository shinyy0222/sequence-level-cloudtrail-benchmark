# Dataset Card

## Dataset Name

Sequence-Level AWS CloudTrail Benchmark

## Summary

This dataset contains temporally ordered AWS CloudTrail API sequences represented using only the `eventSource:eventName` pair.

It was constructed for controlled research on threat detection involving dual-use AWS APIs.

## Dataset Size

| Label | Sequence Type | Count |
| --- | --- | ---: |
| Malicious | Base | 34 |
| Malicious | Combination | 100 |
| Benign | Base | 25 |
| Benign | Combination | 100 |
| | **Total** | **259** |

## Representation

Each sample is stored as a plain-text file containing one normalized API event per line.

## Provenance

### Malicious Base Sequences

Malicious base sequences were derived from AWS attack-technique executions using Stratus Red Team v2.31.0.

CloudTrail activity was collected and organized using Grimoire.

### Malicious Combination Sequences

Malicious combination sequences were constructed from the collected malicious base sequences.

Two or more base sequences were connected according to MITRE ATT&CK-informed attack progressions while preserving the internal temporal order of each constituent base sequence.

No arbitrary individual API events were synthesized during this process.

### Benign Base Sequences

Benign base sequences were collected from administrative workflows executed in AWS.

### Benign Combination Sequences

Benign combination sequences connect multiple benign base workflows to represent consecutive administrative activities.

## Collection Environment

- AWS Region: `us-east-1`
- CloudTrail multi-region management events
- Global service events enabled

## Labels

Each complete sequence is labeled `malicious` or `benign`.

The sequence label does not imply that every individual API event in that sequence is independently malicious or benign.

## Intended Uses

Appropriate uses include:

- sequence-level CloudTrail classification
- event-level versus sequence-level comparison
- false-positive analysis
- dual-use API analysis
- LLM-based cloud security analysis
- retrieval-augmented threat detection

## Out-of-Scope Uses

The benchmark should not be treated as:

- a representative sample of production AWS traffic
- a comprehensive catalog of AWS attacks
- a replacement for full-context CloudTrail analysis
- evidence of production deployment robustness

## Privacy

The public release includes normalized API sequences and sanitized raw CloudTrail traces for the 59 base workflows.

Unsanitized CloudTrail logs are not distributed. Account identifiers, ARNs, access-key identifiers, principals, usernames, source IP addresses, resource-specific identifiers, and other sensitive values are pseudonymized or redacted in the raw release.

The sanitized raw artifacts are therefore not intended for analyses that depend on original AWS identities, IP addresses, credentials, or resource names.

## Known Limitations

The benchmark is based on controlled attack emulation and designed administrative workflows.

A separate per-combination constituent-base mapping artifact is not included in this release.

## Raw Trace Artifacts

Release v1.1.0 includes 59 sanitized CloudTrail base-workflow traces: 34 malicious and 25 benign.

These raw artifacts provide execution provenance for the normalized benchmark and are supplemental artifacts rather than additional benchmark samples.

Combination sequences are constructed from base workflows and therefore are not duplicated as independent raw captures.

Environment-specific identifiers and sensitive values are pseudonymized or redacted before publication.

