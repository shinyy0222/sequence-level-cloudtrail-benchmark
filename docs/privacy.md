# Privacy and Data Release

## Released Data

The public repository contains two representations:

1. The normalized sequence-level benchmark using `eventSource:eventName`.
2. Sanitized raw CloudTrail traces corresponding to the 59 base workflows.

The normalized benchmark contains 34 malicious base sequences, 100 malicious combination sequences, 25 benign base sequences, and 100 benign combination sequences.

The raw release contains 34 malicious and 25 benign base-workflow traces.

## Raw Trace Sanitization

The unsanitized CloudTrail source traces are not included in this repository.

Before publication, environment-specific and potentially sensitive values are pseudonymized or redacted. These include AWS account identifiers, ARNs, access-key identifiers, principal identifiers, usernames, source IP addresses, event/request identifiers, resource-specific identifiers, and secret- or credential-related values.

The sanitization procedure preserves fields required to interpret CloudTrail API behavior, including `eventSource`, `eventName`, `eventCategory`, and `managementEvent`.

The private pseudonymization salt is not distributed.

## Raw and Normalized Representations

The normalized benchmark focuses on ordered `eventSource:eventName` sequences.

Raw scenario traces can contain additional CloudTrail records that are not included in the normalized representation. For example, Data Events can occur in a raw workflow even when the normalized benchmark retains only the relevant Management Events.

Combination sequences do not have separate raw captures because they are constructed from collected base workflows.

## Release Validation

Before release, the public raw artifacts are scanned for common sensitive-data patterns, including:

- 12-digit AWS account identifiers
- AWS access-key patterns
- IPv4 addresses

Release v1.1.0 contains 59 sanitized raw base-workflow JSON files and passes these release-time checks.

## Scope

The sanitized traces provide provenance for the sequence benchmark but are not exact replicas of the private AWS environment logs. Analyses requiring original account identities, IP addresses, credentials, or environment-specific resource names are outside the intended scope of the public raw release.
