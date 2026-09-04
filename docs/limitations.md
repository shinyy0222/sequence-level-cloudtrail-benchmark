# Limitations

This dataset is a controlled research benchmark rather than a representative sample of production AWS activity.

## Controlled Environment

Malicious data is based on cloud attack emulation, while benign data is based on designed administrative workflows executed in AWS.

The resulting sequences do not capture the complete diversity of real enterprise environments.

## Compact Representation

Only `eventSource:eventName` is retained.

Potentially informative event attributes are excluded, including:

- request parameters
- actor identity
- source IP
- user agent
- MFA status
- resource identifiers
- policy documents
- error information

Some malicious and benign activities may therefore remain ambiguous.

## Production Distribution

The dataset does not estimate how frequently individual workflows occur in real AWS deployments.

Benign workflows should be interpreted as operationally plausible controlled cases rather than measurements of production prevalence.

## Attack Coverage

The malicious sequences cover only the attack techniques and combinations represented by the underlying executions.

They are not a comprehensive representation of all AWS attack behavior.

## Combination Sequences

Combination sequences are constructed from base workflows.

Although constituent sequence order is preserved, these combinations do not reproduce all sources of noise, concurrency, timing variation, or unrelated background activity that occur in production CloudTrail logs.

## Generalization

Performance measured on this benchmark should not be interpreted as evidence of production-level robustness without additional validation on independently collected malicious and benign CloudTrail activity.
