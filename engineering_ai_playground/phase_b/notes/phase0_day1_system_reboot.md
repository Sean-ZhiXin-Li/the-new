# Phase 0 Day 1 — Engineering Playground System Reboot

## Objective

Rebuild operational control over the full engineering pipeline:

```text
config → snapshot → subprocess → stdout/stderr → manifest
```

Today was not about building new functionality.
Today was about restoring system comprehension, reproducibility awareness, and execution discipline.

---

# System Map

```text
phase_b/config/day18.json
        ↓
phase_b/src/call_phase_a_once.py
        ↓
scripts/run_failure_aggregation_v1.sh
        ↓
subprocess.run(...)
        ↓
stdout.txt / stderr.txt / returncode.txt
        ↓
config_snapshot.json
        ↓
run_manifest.json
```

---

# Core Files Read

## Config

`phase_b/config/day18.json`

```json
{ "stdin_value": "0.5" }
```

### Meaning:

This config controls the experiment input value passed into Phase A.

---

## Entry Script

`phase_b/src/call_phase_a_once.py`

### Key Responsibilities:

* Reads config (`day18.json`)
* Extracts `stdin_value`
* Creates timestamped experiment folder
* Copies config into `config_snapshot.json`
* Runs:

```bash
scripts/run_failure_aggregation_v1.sh
```

* Captures:

  * stdout
  * stderr
  * returncode
* Writes:

  * `run_manifest.json`

---

# Latest Verified Run

## Folder

`phase_b/experiments/day17_call_20260418_203446`

---

## `config_snapshot.json`

```json
{ "stdin_value": "0.5" }
```

---

## `run_manifest.json`

```json
{
  "timestamp": "20260418_203446",
  "phase_a_entry": "scripts/run_failure_aggregation_v1.sh",
  "config_snapshot": "config_snapshot.json",
  "returncode": 0
}
```

---

## `returncode.txt`

```text
0
```

### Meaning:

`returncode = 0` confirms successful execution.

---

# What I Understand Now

## 1. Config Controls Input

`stdin_value` is not hardcoded — it is externally configurable.

---

## 2. Snapshot Ensures Reproducibility

`config_snapshot.json` preserves the exact config used during this run.

---

## 3. Manifest Tracks Metadata

`run_manifest.json` records:

* timestamp
* entrypoint
* config source
* returncode

---

## 4. stdout / stderr Separate Success from Failure

This supports:

* debugging
* auditability
* reruns

---

# Commands Used

```bash
pwd
tree phase_b
cat phase_b/src/call_phase_a_once.py
cat phase_b/config/day18.json
ls -lt phase_b/experiments | head
cat phase_b/experiments/day17_call_20260418_203446/run_manifest.json
cat phase_b/experiments/day17_call_20260418_203446/config_snapshot.json
cat phase_b/experiments/day17_call_20260418_203446/returncode.txt
```

---

# Initial Bugs / Recovery

## Bug:

```text
tree: command not found
```

## Fix:

```bash
sudo apt install tree
```

## Lesson:

Engineering work includes environment repair, not just coding.

---

# Key Lesson

```text
This is a config-driven experiment pipeline:
config controls execution,
scripts run subprocesses,
and artifacts are saved for reproducibility.
```

---

# Minimum Viable Completion Standard

```text
✔ Repo root confirmed
✔ `phase_b` structure mapped
✔ Config understood
✔ Entry script understood
✔ Snapshot understood
✔ Manifest understood
✔ Successful run verified
```

---

# Stretch Goal (Next)

Modify:

```json
stdin_value
```

Then rerun and verify:

* new `config_snapshot.json`
* new `run_manifest.json`

---

# Today’s Win Condition

```text
I no longer see this as random scripts.
I understand it as a reproducibl
```
