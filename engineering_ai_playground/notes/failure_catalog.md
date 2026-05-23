# Failure Catalog (Phase A)

## F01: param_le_1
Trigger: Input parameter `param <= 1`.
Observable behavior:
- Console prints "ENTER FAILURE MODE"
- metrics.json records `passed=false` and `failure_reason="param_le_1"`
Reproduction:
- Input: 0.76895

---

## F02: legacy_missing_reason
Trigger: Older records created before `failure_reason` was enforced.
Observable behavior:
- On load, entries missing `failure_reason` are patched:
  - if `passed=false` -> `failure_reason="legacy_missing_reason"`
Reproduction:
- Use existing historical entries in metrics.json that have no failure_reason field
