# engineering_ai_playground

A **personal engineering training ground** for building solid, long-term capability in:

* Python engineering (from scratch, not templates)
* Linux-based development workflow (WSL)
* Git discipline and reproducibility
* Debugging as a first-class skill
* Gradual transition toward AI / ML engineering

This repository is **not a product** and **not a research project**.
It is intentionally small, controlled, and process-oriented.

---

## Why This Repository Exists

This repo is designed to answer one question clearly:

> **Can I independently build, debug, and iterate on a Python + AI engineering system in a Linux environment?**

The focus is not on advanced models or performance, but on:

* Writing code from a blank file
* Understanding errors instead of avoiding them
* Forming engineering habits that scale to lab work and research projects

This repository also **supports future lab readiness** by strengthening reproducible engineering and debugging skills that are essential for collaborative research environments.

This repository is meant to stay simple so that **thinking, debugging, and structure** are always visible.

---

## What This Repo Does (Current Phase)

At the current stage (Phase A), the repository contains a single executable script:

* `test.py`

The script:

1. Reads **one numeric input** from standard input
2. Executes a clear **success / failure branch**
3. Prints **explicit console signals** for both paths
4. Appends a structured record to `metrics.json`

Every run leaves a **persistent, inspectable trace**.
Nothing is implicit.

---

## Failure Aggregation (Phase A)

### Verified entry point

To generate and verify failure aggregation results:

```bash
./scripts/run_failure_aggregation_v1.sh
```

This entry point:

* generates `analysis/failure_counts.json`
* verifies count invariants against `metrics.json`

Contract details: `notes/failure_aggregation_contract_v1.md`

---

## Behavior Summary

Input parameter `param` determines execution flow:

* **Success path**: `param > 1`
* **Failure path**: `param <= 1`

Both paths:

* Print a visible console message
* Append exactly one record to `metrics.json`

---

## Minimal Reproduction (Day5)

Environment: Python 3.x on Linux / WSL. No extra dependencies.

### Reproduce failure

```bash
python test.py
# input: 0.2
```

Expected:

* Console prints:

  ```
  ENTER FAILURE MODE
  ```
* File `metrics.json` appends a new record with:

  ```json
  "passed": false,
  "failure_reason": "param <= 1"
  ```

---

### Reproduce success

```bash
python test.py
# input: 2
```

Expected:

* Console prints:

  ```
  1.0
  Hello Engineering World!!!
  ```
* File `metrics.json` appends a new record with:

  ```json
  "passed": true,
  "failure_reason": null
  ```

---

### Verify

```bash
tail -n 40 metrics.json
```

You should see a JSON list.
The **last entry corresponds to the most recent run**.

No code inspection is required to validate correctness.

---

## Training Roadmap (High-Level)

The work in this repository follows a fixed, time-bounded plan:

### Phase A — Foundations (12/24 – 1/12)

* Linux / WSL workflow
* Python virtual environments (venv)
* Git fundamentals with small, clean commits
* Writing minimal runnable scripts
* Real debugging (logic, None, NaN, shape issues)

**Deliverables**:

* ≥10 commits
* Minimal config → run → output pipeline
* `metrics.json` output
* `notes/debug_log.md`

---

### Phase B — Engineering Python (1/13 – 2/9)

* Clear project structure
* Config-driven execution (no hard-coded parameters)
* Reproducible experiments
* Metrics and simple plots

**Constraints**:

* Models limited to linear / logistic / very small MLP
* Engineering clarity > model complexity

---

### Phase C — Python AI Engineering (2/10 – 3/23)

* PyTorch basics
* `train` / `eval` separation
* Seed control
* At least one ablation study
* Explicit experiment tracking

**Theory is introduced only through engineering phenomena**, not formulas.

---

### Phase D — Maintenance & Low Frequency (3/24 – 5)

* Reduced cadence due to AP exams
* Refactoring, documentation, and bug fixes only
* No new features or models

---

## Engineering Principles

This repository values:

* Clarity over cleverness
* Correctness over speed
* Reproducibility over convenience
* Debugging over avoidance

Mistakes are expected and preserved as part of the training process.

---

## Status

* Phase: **A — Foundations**
* Scope: **Frozen**
* Focus: **Failure semantics, traceability, reproducibility**

Complexity is added only when explicitly scheduled.

---

## License

Personal educational use.
