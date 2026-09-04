# Dataset Construction

## Representation

Each CloudTrail event is normalized to:

    eventSource:eventName

Events remain in temporal order within each sequence.

Event-specific fields such as request parameters, actor identity, source IP address, resource identifiers, user-agent information, MFA state, policy documents, and error information are not included in the released representation.

## Collection Environment

- AWS Region: `us-east-1`
- CloudTrail multi-region management events
- Global service events enabled

## Malicious Base Sequences

Malicious base sequences were derived from executions of AWS attack techniques using Stratus Red Team v2.31.0.

CloudTrail events generated during each execution were collected and organized using Grimoire.

One execution-derived API flow forms one malicious base sequence.

The observed temporal order and repeated API calls are preserved.

The final benchmark contains 34 malicious base sequences.

## Malicious Combination Sequences

Malicious combination sequences were constructed using the 34 malicious base sequences as constituent flows.

Two or more base sequences were connected according to MITRE ATT&CK-informed attack progression.

The construction follows three principles:

1. Only collected malicious base sequences are used as constituent attack flows.
2. The internal temporal order of each constituent base sequence is preserved.
3. No arbitrary individual API event is synthesized or inserted during combination.

The final benchmark contains 100 malicious combination sequences.

## Benign Base Sequences

Benign base sequences correspond to administrative workflows executed in AWS.

Representative workflow categories include:

- IAM lifecycle operations
- access-key management
- Secrets Manager lifecycle management
- infrastructure inspection
- monitoring
- audit
- security review
- cleanup

The benign set intentionally includes security-sensitive APIs that can also occur in attacks.

The final benchmark contains 25 benign base sequences.

## Benign Combination Sequences

Benign combination sequences were constructed by connecting multiple benign base workflows to represent consecutive administrative activities.

They are intended as controlled, operationally plausible workflows rather than measurements of production prevalence.

The final benchmark contains 100 benign combination sequences.

## Combination Mapping Availability

The release documents the construction procedure and distributes all resulting combination sequence files.

A separate per-combination mapping from each combination file to the exact constituent base-sequence filenames is not included as a release artifact.

## Final Dataset

- Malicious Base Sequence: 34
- Malicious Combination Sequence: 100
- Benign Base Sequence: 25
- Benign Combination Sequence: 100
- Total: 259
