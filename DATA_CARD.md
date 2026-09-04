# Dataset Card

## Dataset Name

Sequence-Level AWS CloudTrail Benchmark

## Summary

This dataset contains temporally ordered AWS CloudTrail API sequences represented using only the `eventSource:eventName` pair.

It was constructed to support controlled research on threat detection involving dual-use AWS APIs that may occur in both malicious attack workflows and legitimate administrative activity.

## Dataset Size

The benchmark contains 259 sequence samples.

| Label | Sequence Type | Count |
| --- | --- | ---: |
| Malicious | Base | 34 |
| Malicious | Combination | 100 |
| Benign | Base | 25 |
| Benign | Combination | 100 |
| | Total | 259 |

## Data Representation

Each sample is stored as a plain-text file with one API event per line.

Example:

    ec2.amazonaws.com:DescribeInstances
    ssm.amazonaws.com:SendCommand
    ssm.amazonaws.com:GetCommandInvocation

Only the AWS service and operation identity are retained.

## Malicious Data

Malicious base sequences were derived from AWS attack-technique executions using Stratus Red Team v2.31.0, with corresponding CloudTrail activity collected using Grimoire.

Malicious combination sequences were constructed by connecting collected base sequences according to MITRE ATT&CK-informed multi-stage attack progressions while preserving the internal order of each constituent base sequence.

## Benign Data

Benign base sequences were derived from administrative workflows executed in AWS.

They include identity management, access-key management, Secrets Manager lifecycle management, infrastructure review, audit, monitoring, and cleanup operations.

Benign combination sequences connect multiple benign base workflows into longer consecutive administrative sequences.

## Labels

Each complete sequence is assigned one of two labels:

- malicious
- benign

The label applies to the complete sequence and does not imply that every individual API event in the sequence is independently malicious or benign.

## Intended Uses

Appropriate research uses include:

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

Raw CloudTrail JSON records are not distributed.

The released sequences contain only normalized API identifiers and intentionally exclude account-specific and user-specific event attributes.

## Known Limitations

The benchmark is based on controlled attack emulation and designed administrative workflows.

It does not capture the full variability of production AWS environments, including organization-specific automation, long-term user behavior, background activity, adaptive attackers, and complete event-specific telemetry.

See `docs/limitations.md` for additional information.
