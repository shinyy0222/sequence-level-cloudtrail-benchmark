# Limitations

This dataset is a controlled research benchmark rather than a representative sample of production AWS activity.

## Controlled Environment

Malicious data is based on cloud attack emulation, while benign data is based on designed administrative workflows executed in AWS.

The resulting sequences do not capture the complete diversity of real enterprise environments.

## Compact Representation

Only `eventSource:eventName` is retained.

Potentially informative fields such as request parameters, actor identity, source IP, user agent, MFA status, resource identifiers, policy documents, and error information are excluded.

## Production Distribution

The dataset does not estimate how frequently individual workflows occur in real AWS deployments.

Benign workflows should be interpreted as operationally plausible controlled cases rather than measurements of production prevalence.

## Attack Coverage

The malicious sequences cover only the attack techniques and combinations represented by the underlying executions.

They are not a comprehensive representation of all AWS attack behavior.

## Combination Sequences

For malicious data, combination sequences are assembled from collected malicious base sequences according to MITRE ATT&CK-informed attack progressions while preserving the internal order of each constituent base sequence.

No arbitrary individual API event is synthesized during combination.

For benign data, multiple benign base workflows are connected to form longer consecutive administrative activities.

The public release provides the resulting combination sequences and construction rules but does not provide a separate per-combination constituent-base mapping artifact.

Combination sequences do not reproduce all sources of noise, concurrency, timing variation, or unrelated background activity found in production CloudTrail logs.

## Generalization

Performance measured on this benchmark should not be interpreted as evidence of production-level robustness without additional validation on independently collected malicious and benign CloudTrail activity.
