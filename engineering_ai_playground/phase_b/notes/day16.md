# Day16 — Minimal Read-only Invocation Proof

## Goal

Demonstrate that **Phase B can invoke Phase A exactly once** without modifying
any Phase A files, schemas, or contracts.

This step exists solely to prove that the Phase B → Phase A boundary
is callable, stable, and auditable.

---

## What Was Proven

- A Phase B Python script successfully invokes the existing Phase A entry script:
  `scripts/run_failure_aggregation_v1.sh`
- The invocation is **read-only** with respect to Phase A
- Phase B captures and persists execution evidence:
  - `returncode.txt`
  - `stdout.txt`
  - `stderr.txt`

All artifacts are written under:
  `phase_b/experiments/day16_call_test/`

- The recorded return code is `0`, indicating a    successful Phase A execution.

---

## How the Proof Works (Minimal)

- Phase B resolves the repository root dynamically
- Phase B invokes Phase A via `bash` using `subprocess.run`
- Standard input is provided programmatically
- Execution outputs are persisted as plain files for auditability

No assumptions are made about Phase A internals beyond its documented entry point.

---

## Non-Goals (Explicitly Out of Scope)

- No parameterization
- No artifact copying from Phase A
- No experiment indexing or naming scheme
- No reusable runner abstraction
- No refactor or modification of Phase A
- No schema or contract changes

---

## Why This Step Matters

This confirms that Phase A can be treated as a **frozen, callable unit**
from Phase B, with a verifiable execution trail.

Future Phase B work can safely build on this boundary
without weakening Phase A invariants.
