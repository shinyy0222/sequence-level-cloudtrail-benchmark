# Dataset Construction

## Representation

Each CloudTrail event is normalized to:

    eventSource:eventName

Events remain in temporal order within each sequence.

Request parameters, actor identity, source IP address, resource identifiers, user-agent information, MFA state, policy documents, and other event-specific fields are not included in the released representation.

## Malicious Base Sequences

Malicious base sequences were derived from executions of AWS attack techniques using Stratus Red Team v2.31.0.

CloudTrail events generated during each execution were collected and organized using Grimoire.

One execution-derived API flow forms one malicious base sequence.

Repeated API calls are preserved.

## Malicious Combination Sequences

Malicious combination sequences connect two or more collected malicious base sequences into longer attack workflows.

Combination follows MITRE ATT&CK-informed tactic progression.

The internal API order of every constituent base sequence is preserved.

No arbitrary individual API event is inserted to create a malicious combination sequence.

## Benign Base Sequences

Benign base sequences correspond to administrative workflows executed in AWS.

Representative workflow categories include:

- IAM user lifecycle
- IAM role lifecycle
- IAM permission review
- access-key management
- Secrets Manager lifecycle
- EC2 inventory
- CloudTrail review
- CloudWatch monitoring
- VPC and network review
- RDS review
- Lambda review
- security assessment and audit workflows

The benign set intentionally includes security-sensitive APIs that can also occur in attacks.

## Benign Combination Sequences

Benign combination sequences connect multiple benign base workflows to represent consecutive administrative activities.

They provide longer normal workflows containing APIs that may appear suspicious when interpreted as isolated events.

## Final Dataset

The released dataset contains:

- 34 malicious base sequences
- 100 malicious combination sequences
- 25 benign base sequences
- 100 benign combination sequences

Total: 259 sequences.
