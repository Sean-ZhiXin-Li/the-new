## Debug #001 — JSON serialization failure (set)

- Trigger: Added a Python `set` into `metrics` (e.g. `{"bad": {1,2,3}}`).
- Symptom: Program crashed at `json.dump(...)` and `metrics.json` was not written/updated.
- Error: `TypeError: Object of type set is not JSON serializable`
- Fix: Converted the `set` to a JSON-serializable type (`list`, e.g. `[1,2,3]`).
- Lesson: Only store JSON-serializable types in `metrics` (dict/list/str/int/float/bool/null).

## Debug #002 — Metrics history structure mismatch
- Trigger: Manually edited `metrics.json` to `{}` (JSON root became an object, not a list).
- Symptom: No crash, but previous history was discarded and a new history list was created.
- Error: None (schema check prevented `append` on a non-list type).
- Fix: After `json.load`, validate `history` with `isinstance(history, list)`. If not a list, reset `history = []` before appending.
- Lesson: Never assume persisted JSON schema is correct. Always validate root type (list vs dict) before mutating metrics history.

## Debug #003 — Failure without semantic explanation

- Trigger:
  Ran `test.py` with input values `param <= 1`, resulting in failed runs.

- Symptom:
  Metrics only recorded `passed = false` without explaining why the failure occurred.

- Error:
  No exception was raised; the problem was missing semantic information about the failure.

- Fix:
  Added a `failure_reason` field to each metrics record, and backfilled legacy records with `legacy_missing_reason`.

- Lesson:
  A boolean flag is not enough in engineering logs; failures must be explicitly and semantically labeled.

## Debug #004 — Failure state ignored by control flow
- Trigger: param=0.2 (passed=False)

- Symptom: failure path printed same as success (no behavior        difference)

- Error: control flow did not branch on passed

- Fix: if passed: ... else: ... (failure mode message)

- Lesson: failure must affect decisions, not just logs

## Debug #005 — Phase A audit under failure and success paths

- Injected condition: <a valid float that triggers failure mode> and <a valid float that triggers success path> (two separate runs).
- Observed behavior: failure path entered; success path entered; metrics.json appended on each run; aggregation verified via ./scripts/run_failure_aggregation_v1.sh (VERIFY OK).
- Invariant check result: metrics.json append-only preserved; every failed record has failure_reason (none missing / none None); sum(failure_counts) == number of failed records; verification passed.
