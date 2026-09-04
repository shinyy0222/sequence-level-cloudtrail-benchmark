# Privacy and Data Release

## Released Data

The public dataset contains only normalized AWS API identifiers in the form:

    eventSource:eventName

## Raw Logs

Raw CloudTrail JSON records are not included in this repository.

Raw records may contain environment-specific information that is unnecessary for reproducing the compact sequence representation used in the study.

## Excluded Information

The released sequence files intentionally exclude fields such as:

- AWS account IDs
- IAM user identities
- role ARNs
- resource ARNs
- access keys
- source IP addresses
- user agents
- request parameters
- policy documents
- resource identifiers
- authentication metadata

## Release Validation

Before release, the normalized files are checked for common patterns corresponding to:

- AWS access keys
- ARNs
- IPv4 addresses
- 12-digit AWS account identifiers

The repository validation script performs these checks automatically.

## Scope

The absence of raw event attributes is a deliberate property of this benchmark and matches the compact representation evaluated in the associated study.
