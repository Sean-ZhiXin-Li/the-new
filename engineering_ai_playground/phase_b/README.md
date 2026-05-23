# Phase B — Engineering Scaffold (Read-only Inheritance)

## Purpose
Phase B adds an engineering shell on top of Phase A so future work can grow without touching the Phase A core.
The focus is structure, boundaries, and reproducibility — not new functionality.

## Inheritance from Phase A (Read-only Contract)
Phase A is treated as a read-only execution unit.

Phase B is allowed to:
- invoke Phase A as-is (no edits)
- consume Phase A outputs (e.g., metrics.json) as read-only inputs
- build additional Phase B artifacts around those outputs (configs, experiment folders, comparisons)

Phase B is NOT allowed to:
- modify any Phase A files (README / scripts / notes / contracts / code)
- change the Phase A metrics schema
- redefine Phase A failure semantics

## What Phase B Will Add (Capabilities only)
- Config-driven execution (all variable knobs live in `phase_b/config/`)
- Experiment isolation (each run leaves traces under `phase_b/experiments/`)
- Run-to-run comparison (Phase B can compare metrics across runs without altering Phase A)
