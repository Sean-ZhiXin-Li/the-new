# Day20 (Phase B · Day6) — Run Manifest

## Added
- Auto-generate `run_manifest.json` for each run under `phase_b/experiments/<run_dir>/`.

## Proof
- run_dir:day17_call_20260122_183027
- run_manifest.json:
  - timestamp: <...>
  - phase_a_entry: scripts/run_failure_aggregation_v1.sh
  - config_snapshot: config_snapshot.json
  - returncode: 0

## Non-goals
- no CLI
- no multi-config
- no result interpretation
- Phase A untouched
