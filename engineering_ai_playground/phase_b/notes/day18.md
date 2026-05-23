# Day18 — Phase B Day4
## Minimal Single-Value Config (stdin only)

### What changed
- The stdin value is no longer hardcoded in the Phase B runner.
- `STDIN_VALUE` is now loaded from an external config file:
  `phase_b/config/day18.json` (key: `stdin_value`).
- Changing the input value no longer requires modifying Python code.

### Proof
- Phase B was executed twice with identical code and different config values:
  - `day17_call_20260114_184526/config_snapshot.json` → `"stdin_value": "1.5"`
  - `day17_call_20260114_184616/config_snapshot.json` → `"stdin_value": "3.0"`
- The config file was the only thing changed between the two runs.
- Both runs completed successfully (returncode = 0), demonstrating that
  stdin is fully controlled by the config file.

### Non-goals
- No command-line arguments
- No multi-parameter or multi-config system
- No validation or fallback logic
- No changes to Phase A
- Experiment artifacts remain untracked by git
