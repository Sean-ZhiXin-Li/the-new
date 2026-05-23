# Failure Aggregation Contract v1 (Phase A)

Inputs (read-only):
- metrics.json
- analysis/failure_counts.json

Contract:
- failure_counts.json must be a dict[str, int]
- sum(counts.values()) == number of records where passed == false

Entry point:
- ./scripts/run_failure_aggregation_v1.sh

