# Phase A System Map

## System Components
- input: floating-point value via standard input
- execution: runtime stage where the success or failure outcome is determined after standard input
- persistence: metrics.json (append-only per run)
- aggregation output: analysis/failure_counts.json
- verification: failure aggregation contract invariants
- entry point: ./scripts/run_failure_aggregation_v1.sh

## Data Flow
standard input → [execution] → metrics.json → [aggregation entry] → analysis/failure_counts.json

## Invariants & Guarantees
- metrics.json is append-only per run
- every failed record in metrics.json must have a failure_reason
- analysis/failure_counts.json must be a dict[str, int]
- sum(analysis/failure_counts.json values) == number of records where passed == false
- no aggregation output is trusted without contract verification
- aggregation entry must verify invariants before writing failure_counts.json
