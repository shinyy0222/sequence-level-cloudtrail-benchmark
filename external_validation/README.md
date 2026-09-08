# External Validation

This directory documents the malicious-only external evaluation used in the manuscript **Sequence-Level AWS CloudTrail Threat Detection with Retrieval-Augmented Large Language Models**.

The external evaluation is separate from the 259-sequence benchmark under `dataset/`.

## External Sources and Roles

Two AWS attack sources are used:

- **CloudGoat**: 25 malicious API sequences, used as a **development/generalization set**.
- **Atomic Red Team**: 25 malicious API sequences, used as a **held-out external evaluation set**.

All samples use the same compact `eventSource:eventName` representation as the internal benchmark.

## Representation-Specific Evaluation

The evaluation unit differs by representation.

### Single-event Prompt-only

Single-event samples are constructed using the same malicious-event selection rule as the internal event-level evaluation:

1. candidate events are restricted to the same predefined set of attack-relevant and security-sensitive API operations used internally;
2. repeated occurrences of the same normalized API within the same source sequence are removed using `(eventSource:eventName, source sequence)` as the deduplication key;
3. sampling uses seed `42` and an internal maximum of 100 malicious events;
4. because the eligible external pools are smaller than 100, all eligible events are retained.

This yields:

- CloudGoat: **21 eligible events**
- Atomic Red Team: **43 eligible events**

Single-event Prompt-only is therefore evaluated using **event-level recall**.

### Sequence Prompt-only and Sequence with RAG

Each complete malicious sequence is classified directly as an ordered API sequence.

- CloudGoat: 25 sequences
- Atomic Red Team: 25 sequences

Both sequence-based methods are evaluated using **sequence-level recall**.

Because Single-event and sequence-based settings use different evaluation units, their results are interpreted descriptively rather than as paired comparisons.

The external sets contain only malicious samples. Accordingly, this evaluation reports recall only; false-positive robustness, precision, F1, and full binary-classification generalization cannot be assessed without external benign samples.

## Final Results

| Source | Role | Single-event Prompt-only | Sequence Prompt-only | Sequence with RAG |
|---|---|---:|---:|---:|
| CloudGoat | development/generalization | 13/21 (0.619) | **18/25 (0.720)** | 15/25 (0.600) |
| Atomic Red Team | held-out external | 35/43 (0.814) | **25/25 (1.000)** | 19/25 (0.760) |

Single-event values are event-level recall; sequence-based values are sequence-level recall.

No pooled `Overall` result is reported because the Single-event and sequence-based settings use different evaluation units and sample counts, and because CloudGoat and Atomic Red Team serve different evaluation roles.

## Interpretation

Sequence Prompt-only shows numerically higher malicious-detection recall than the event-level baseline on both external sources under the representation-specific protocol. These values are descriptive rather than paired event-versus-sequence comparisons.

Sequence with RAG performs below Sequence Prompt-only on both external sources, indicating that the retrieval benefit observed on the controlled internal benchmark does not uniformly transfer under external source shift.

## Data Provenance Note

CloudGoat sequences are execution-derived attack traces used during development/generalization analysis.

The Atomic Red Team sequence set used for the final paper evaluation is the **actual execution-derived base-combination set**, not the earlier synthetic Atomic combination robustness set. The final held-out Atomic sequences preserve the order of their execution-derived constituent base traces.

## Results Files

- `results/source_metrics.csv`: source-specific final recall values under the representation-specific protocol.
- `results/final_metrics.csv`: final paper-facing metric table with source role and evaluation unit.

The previous pooled `overall_metrics.csv` is intentionally removed because an overall pooled recall is not meaningful under the final representation-specific protocol.

## Scope

These external samples are not part of the 259-sequence benchmark count. The external evaluation is malicious-only and is intended to characterize attack-detection generalization rather than external false-positive robustness.
