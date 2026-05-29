# Spacecraft Phase0 Week1 Summary

## Objective

This week was not about PPO training, reward tuning, controller optimization, or changing environment physics.

The goal was to understand the structural foundation of the spacecraft control system:

* OrbitEnv
* observation
* action
* reward
* info
* closed-loop rollout
* controller boundaries
* metrics
* ranking
* engineering evaluation

The primary objective was to understand how the system works before attempting to improve it.

---

# 1. What OrbitEnv Is

OrbitEnv is the physical world and Gym-style interface for the spacecraft control project.

It is not the controller.

It is not PPO.

OrbitEnv defines:

* spacecraft state representation
* action interface
* physics updates
* reward computation
* success conditions
* failure conditions
* diagnostic information

Core mental model:

```text
OrbitEnv = physics world + API rules

Controller / PPO = decision maker
```

OrbitEnv owns the simulation.

Controllers and PPO policies only propose actions inside the environment.

The environment decides what actually happens according to physics and system rules.

---

# 2. What Observation Means

Observation is the state information exposed to the controller.

The observation dimension is:

```text
obs_dim = 5
```

Current observation structure:

```text
[x, y, vx, vy, v_r]
```

Meaning:

```text
x     = spacecraft x position
y     = spacecraft y position

vx    = x velocity
vy    = y velocity

v_r   = radial velocity
```

The observation is a compressed description of the current spacecraft state.

Controllers and PPO policies do not see the entire environment implementation.

They only receive the observation vector.

Conceptually:

```text
observation
→ controller / policy
→ action
```

The observation serves as the input of the decision system.

---

# 3. What Action Means

Action is the output produced by a controller or PPO policy.

The action dimension is:

```text
action_dim = 2
```

Conceptually:

```text
action = [ax_command, ay_command]
```

The action is a normalized control command.

The action does not directly move the spacecraft.

Instead:

```text
action
→ thrust
→ acceleration
→ velocity update
→ position update
```

The environment interprets the action and converts it into physical motion.

Important principle:

```text
Controller proposes actions.

OrbitEnv applies physics.
```

---

# 4. What Reward Means

Reward is an evaluation signal.

Reward is not physics.

Reward does not directly control the spacecraft.

Reward evaluates whether a state transition is desirable according to the task objective.

Conceptually:

```text
good behavior
→ higher reward

bad behavior
→ lower reward
```

Reward exists to evaluate performance.

It does not define gravity.

It does not define thrust.

It does not define orbital dynamics.

The environment computes reward after physics updates have already occurred.

---

# 5. What Metrics Mean

Metrics are engineering measurements.

Metrics are more important than naming, intuition, or complexity.

Examples used throughout the project:

```text
Crossings

Recoverable Crossings

CAPTURE

Success

Overspeed

Instability
```

Metrics answer questions such as:

```text
Did the spacecraft cross the target orbit?

Did it recover after crossing?

Did it achieve capture?

Was the behavior stable?

Did the controller improve performance?
```

Metrics transform simulation behavior into measurable evidence.

Engineering decisions should be based on metrics.

Not assumptions.

---

# 6. What Candidate Ranking Means

The project follows a ranking workflow.

Core engineering chain:

```text
candidate
→ metrics
→ ranking
→ conclusion
```

Examples of candidates:

```text
baseline controller

predictive planner

crossing bias planner

burn selector variants
```

Each candidate is evaluated using the same benchmark metrics.

Then candidates are compared.

Example abstraction:

```text
higher success
→ better rank

higher capture
→ better rank

higher recoverability
→ better rank
```

This is structurally similar to:

```text
C++ comparator

AI argmax

engineering ranking systems
```

Metrics define priorities.

Priorities define rankings.

Rankings support engineering conclusions.

---

# 7. What I Must Not Change Yet

At the current phase, I should not modify:

```text
reward functions

environment physics

PPO implementation

termination logic

capture definitions

evaluation metrics
```

Reason:

```text
I am still learning system structure.
```

Changing the system before understanding the system creates confusion.

The current goal is:

```text
trace
inspect
understand
```

Not:

```text
optimize
modify
improve
```

Understanding must come before optimization.

---

# 8. Why PPO Is Not Today's Focus

PPO is only one possible decision maker.

PPO does not define:

```text
environment

physics

metrics

ranking

evaluation
```

Therefore PPO is not the starting point.

Current learning order:

```text
environment

observation

action

reward

closed-loop interaction

metrics

ranking

controller comparison

PPO
```

If the structure is not understood first, PPO becomes a black box.

The goal is to understand the system before understanding the learning algorithm.

---

# 9. Closed-Loop Interaction Understanding

The spacecraft project is not a one-step calculation.

It is a repeated state transition system.

Core interaction chain:

```text
obs
→ action
→ next_obs
→ next_action
→ next_next_obs
→ ...
```

This creates:

```text
closed-loop behavior
```

Each new observation becomes the input for the next decision.

This structure is the foundation of:

```text
feedback control

reinforcement learning

PPO

spacecraft autonomy
```

---

# 10. Biggest Week 1 Insights

## Insight 1

```text
OrbitEnv owns the world.

Controllers only make decisions.
```

---

## Insight 2

```text
Reward is evaluation.

Reward is not physics.
```

---

## Insight 3

```text
Metrics are the language of engineering.
```

---

## Insight 4

```text
Candidate
→ Metrics
→ Ranking
→ Conclusion
```

is the core engineering workflow.

---

## Insight 5

```text
Spacecraft control is not magic AI.

It is structured engineering evaluation.
```

---

# 11. 90-Second Explanation

This project is not just about training PPO.

At the current stage, I am learning how the environment, controller, metrics, and benchmark structure work.

OrbitEnv defines the physical simulation and the Gym-style interface.

The spacecraft state is represented through observations, while controllers or PPO policies generate actions.

OrbitEnv applies physics updates, computes rewards, checks success and failure conditions, and returns diagnostic information.

The project evaluates controller candidates using metrics such as crossings, recoverability, CAPTURE, and success.

Controllers are compared using benchmark results rather than intuition.

The key engineering workflow is:

```text
candidate
→ metrics
→ ranking
→ conclusion
```

The most important lesson from Week 1 is that spacecraft autonomy is not primarily about AI algorithms.

It is about understanding the environment, measuring outcomes, and making engineering decisions based on evidence.

---

# One-Sentence Summary

```text
Week 1 taught me that spacecraft autonomy begins with understanding the environment, measurements, and evaluation structure before attempting controller or PPO optimization.
```
