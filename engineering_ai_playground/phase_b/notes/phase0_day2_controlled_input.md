# Phase 0 Day 2 — Controlled Input

## Objective

Understand and verify the full engineering chain:

```text
config → execution → experiment artifact → reproducibility
```

This phase is not about building new features.

This phase is:

```text
Safe system control + trace verification
```

---

# Current Config

## Modified Input

```json
{ "stdin_value": "0.75" }
```

---

# Core Commands Used

## Inspect Current Config

```bash
cat phase_b/config/day18.json
```

### Purpose

```text
Check current system state before modification.
```

---

## Backup Config

```bash
cp phase_b/config/day18.json phase_b/config/day18_backup_day2.json
```

### Purpose

```text
Preserve original config for rollback and reproducibility.
```

---

## Validate JSON

```bash
python -m json.tool phase_b/config/day18.json
```

### Purpose

```text
Ensure config syntax correctness before execution.
```

---

# Execution Command

```bash
python phase_b/src/call_phase_a_once.py
```

---

# Run Status

```text
returncode: 0
```

## Meaning

```text
Execution successful
No crash
No syntax/runtime failure
```

---

# New Experiment Folders

## Run 1

```text
day17_call_20260509_211530
```

## Run 2

```text
day17_call_20260509_211536
```

---

# Config Snapshot Verification

## Run 1

```json
{ "stdin_value": "0.75" }
```

## Run 2

```json
{ "stdin_value": "0.75" }
```

## Result

```text
Both runs correctly preserved intended config.
```

---

# Run Manifest Verification

## Run 1

```json
{
  "timestamp": "20260509_211530",
  "phase_a_entry": "scripts/run_failure_aggregation_v1.sh",
  "config_snapshot": "config_snapshot.json",
  "returncode": 0
}
```

## Run 2

```json
{
  "timestamp": "20260509_211536",
  "phase_a_entry": "scripts/run_failure_aggregation_v1.sh",
  "config_snapshot": "config_snapshot.json",
  "returncode": 0
}
```

---

# Key Lessons

## Lesson 1 — Config Controls Execution

```text
Changing stdin_value changes experiment input.
```

---

## Lesson 2 — Snapshot Preserves Ground Truth

```text
config_snapshot.json records actual run configuration.
```

---

## Lesson 3 — Manifest Preserves Metadata

```text
timestamp + entry script + returncode = reproducibility trace
```

---

## Lesson 4 — Same Config Should Produce Consistent Trace Structure

```text
same config → same snapshot → successful repeated runs
```

---

# Engineering System Model

```text
Inspect → Backup → Validate → Modify → Run → Verify
```

---

# Common Bugs Prevented

```text
✔ Blind config edits
✔ No backup before modification
✔ Broken JSON syntax
✔ Running unknown config
✔ Missing artifact verification
```

---

# Current Understanding

## Before Day 2

```text
I can run the script.
```

## After Day 2

```text
I can control input, validate config, execute safely, and verify reproducible experiment artifacts.
```

---

# Lab / Research Relevance

This exact workflow later applies to:

```text
reward_config.json
controller_config.json
mission_profile.json
hyperparameter sweeps
experiment reproducibility
```

---

# Win Condition

```text
✔ Understand cat
✔ Understand cp
✔ Understand json.tool
✔ Understand config_snapshot
✔ Understand run_manifest
✔ Understand reproducibility chain
```

---

# One-Sentence Summary

```text
Today I learned how to safely modify system input, validate configuration correctness, execute experiments, and verify reproducible engineering artifacts.
```

---

# Next Upgrade (Day R3 Preview)

```text
Consistency Testing:
same config → compare stdout / artifacts across runs
```

Goal:

```text
Move from “it runs” → “it runs consistently.”

```
