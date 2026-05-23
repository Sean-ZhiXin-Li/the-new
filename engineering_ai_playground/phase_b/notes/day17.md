# Day17 — Phase B

## What changed
- Timestamped experiments: `day17_call_YYYYMMDD_HHMMSS`
- stdin moved to `STDIN_VALUE` (still minimal, no config system)

## How verified
- Ran the script multiple times
- Observed multiple `day17_call_...` directories
- Each directory contains:
  - `returncode.txt`
  - `stdout.txt`
  - `stderr.txt`

## Non-goals
- No runner / framework / class
- No JSON/YAML config (reserved for Day18)
- No Phase A edits
- No copying Phase A artifacts
