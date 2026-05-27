# Phase0 Day6 — Spacecraft Planner Ranking Reading Log

## Objective

Understand how spacecraft planners and controller experiments are evaluated.

Today's goal is NOT:

- PPO training
- reward redesign
- physics modification

Today's goal IS:

```text
candidate
→ metrics
→ ranking
→ engineering conclusion
```

---

# Files Read

## Phase20

```text
analysis/phase20_predictive_planner/summary.md
```

## Phase29

```text
analysis/phase29_repo_audit_and_family_selector/repo_audit.md
```

## Phase35

```text
analysis/phase35_crossing_basin_expansion/summary.md
```

---

# Key Realization

Today I realized that spacecraft controller evaluation follows the same abstraction as:

```text
C++ comparator
AI argmax
engineering ranking systems
```

The core structure is:

```text
candidate
→ evaluation metrics
→ ranking
→ selection
```

---

# Phase20 Analysis

## Candidates

```text
baseline_soft_linear_3e4

phase19_minimal_transfer

phase20_predictive_planner
```

## Evaluation Metrics

```text
CAPTURE
Success
Crossing cases
Recoverable crossings
Overspeed
```

## Observation

Phase20 introduced:

```text
predictive planning
future crossing evaluation
recoverability-aware scoring
```

but final benchmark results remained identical to baseline.

## Engineering Conclusion

The planner generated:

```text
82566 replans
743094 candidate simulations
```

but did not improve:

```text
Success
CAPTURE
Recoverable crossings
```

Therefore:

```text
The bottleneck is not solved by this planner design.
```

---

# Phase29 Analysis

## Candidates

Five Burn-A family selectors.

Examples:

```text
phase29_angular_momentum_targeted_burn_a

phase29_energy_angular_momentum_balanced_burn_a

phase29_baseline_phase22_burn_a
```

## Evaluation Metrics

```text
Crossings
Recoverable
CAPTURE
Success
Dead windows
```

## Observation

All major variants produced very similar results.

The selector changed transfer-family logic but did not improve:

```text
Recoverable crossings
Success
```

## Engineering Conclusion

```text
Family selection itself is not the dominant bottleneck.
```

A larger search space is likely required.

---

# Phase35 Analysis

## Candidates

```text
baseline_phase34

radial_energy_push

tangential_corridor_entry

predictive_crossing_bias
```

## Evaluation Metrics

```text
Geometric crossings
Recoverable crossings
Success
Overspeed
Instability
```

## Observation

Best crossing count remained:

```text
8 / 24
```

Both:

```text
baseline_phase34
predictive_crossing_bias
```

produced the same crossing count.

## Failure Modes

Primary failures:

```text
near_crossing

over_conservative_transfer
```

## Engineering Conclusion

The bottleneck is not crossing bias.

The dominant issue is:

```text
crossing basin expansion
```

before the first crossing occurs.

---

# Comparator Thinking

Today I connected spacecraft analysis to C++ comparator logic.

C++ example:

```cpp
if (success differs)
    higher success wins;

if (capture differs)
    higher capture wins;

if (recoverable differs)
    higher recoverable wins;
```

Spacecraft evaluation follows the same idea.

Metrics define priority.

Priority defines ranking.

Ranking defines engineering decisions.

---

# Connection to AI

Today's AI chain:

```text
scores
→ ranking
→ argmax
→ action
```

Spacecraft chain:

```text
controller candidates
→ metrics
→ ranking
→ selected approach
```

The abstraction is identical.

---

# Connection to Engineering

Engineering is not:

```text
write code
→ run
→ finish
```

Engineering is:

```text
candidate
→ measurement
→ comparison
→ diagnosis
→ conclusion
```

The spacecraft project follows this workflow.

---

# Biggest Insight

A spacecraft planner does not succeed because it is called:

```text
planner
AI
predictive
```

It succeeds only if it produces better ranked outcomes under meaningful metrics.

The project is fundamentally:

```text
Structured Data
→ Evaluation
→ Ranking
→ Selection
```

which is the same abstraction behind:

- comparator
- argmax
- planner selection
- engineering decision systems

---

# Day6 Final Summary

The most important realization today is:

```text
Spacecraft controller development is not magic AI.

It is structured engineering selection based on metrics and ranking.
```

Or structurally:

```text
candidate
→ metrics
→ ranking
→ engineering conclusion
```

This connects:

```text
C++ comparator
AI argmax
Engineering evaluation
Spacecraft planners
```

into one unified mental model.


## Metrics Are the Language of Engineering

Engineering decisions should not be based on:

- intuition
- naming
- complexity

Engineering decisions should be based on:

- measurable outcomes
- benchmark metrics
- reproducible comparisons