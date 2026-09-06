# External Validation

This directory contains the external malicious-only evaluation set used to assess generalization beyond the internally constructed sequence-level CloudTrail benchmark.

The external data are derived from independently executed AWS attack workflows using:

- CloudGoat: 25 workflows
- Atomic Red Team: 25 workflows

These samples are **not part of the 259-sequence benchmark** under `dataset/`.

## Evaluation Sets

### Single-event

`single_event/attack_relevant_events_50.csv`

The Single-event evaluation contains 50 attack-relevant API events:

- 25 CloudGoat events
- 25 Atomic Red Team events

Each event is represented as an `eventSource:eventName` pair and is classified independently.

This follows the same evaluation principle used for the internal Single-event malicious subset, where attack-relevant API events are evaluated individually.

### Sequence

`sequence/attack_workflows_50.csv`

The sequence-level evaluation contains the corresponding 50 complete malicious attack workflows:

- 25 CloudGoat workflows
- 25 Atomic Red Team workflows

Each workflow is represented as an ordered sequence of `eventSource:eventName` pairs.

## Evaluation Units

The evaluation units differ by representation:

- Single-event Prompt-only: event-level malicious recall
- Sequence Prompt-only: workflow-level malicious recall
- Sequence + RAG: workflow-level malicious recall

Accordingly, the results are interpreted as a descriptive comparison rather than a paired comparison between Single-event and sequence-level methods.

Because the external evaluation contains only malicious samples, false-positive behavior, precision, and full binary-classification performance cannot be assessed from this set.

## Results

| Source | Single-event | Sequence Prompt-only | Sequence + RAG |
|---|---:|---:|---:|
| CloudGoat | 13/25 (0.52) | 17/25 (0.68) | 20/25 (0.80) |
| Atomic Red Team | 24/25 (0.96) | 25/25 (1.00) | 24/25 (0.96) |
| Overall | 37/50 (0.74) | 42/50 (0.84) | 44/50 (0.88) |

Single-event values report event-level recall on attack-relevant API events, whereas the sequence-based values report workflow-level recall on complete attack workflows.

## Files

- `single_event/attack_relevant_events_50.csv`: 50 attack-relevant Single-event samples
- `sequence/attack_workflows_50.csv`: 50 complete attack workflows
- `results/overall_metrics.csv`: pooled malicious-only recall
- `results/source_metrics.csv`: CloudGoat and Atomic Red Team results separately

## Scope

The external validation set is released separately from the primary benchmark to preserve the distinction between internally constructed benchmark data and independently generated external attack workflows.
