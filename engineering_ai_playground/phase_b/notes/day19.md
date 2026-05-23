# Day19 (Phase B · Day5) — Run Manifest: Config Snapshot

## Change
- Each Phase B run now automatically writes `config_snapshot.json` into the run directory by copying the active config file (`phase_b/config/day18.json`).

## Proof
- Run 1: `day17_call_20260115_184749`
  - snapshot: `{ "stdin_value": "1.5" }`
- Run 2: `day17_call_20260115_184755`
  - snapshot: `{ "stdin_value": "3.0" }`

## Non-goals
- No CLI arguments
- No multi-config support
- No schema/validation system
- Phase A remains untouched
