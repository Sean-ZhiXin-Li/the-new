# Phase0 Day5 — Closed Loop Rollout

## Core Objective

From Day4:

```text
obs_dim = 5
action_dim = 2
policy: R^5 → R^2
```

To Day5:

```text
Understanding how obs/action/reward/info drive repeated state transitions.
```

Core Day5 idea:

```text
OrbitEnv is not a one-step calculator.
OrbitEnv is a repeated state transition system.
```

---

# Rollout Script

File:

```text
scripts/day5_closed_loop_rollout.py
```

Code:

```python
from envs.orbit_env import OrbitEnv


def main():
    env = OrbitEnv()

    obs, info = env.reset(seed=0)
    print("Initial obs:", obs)
    print("Reset info:", info)

    for step_index in range(5):
        action = env.action_space.sample()
        next_obs, reward, terminated, truncated, info = env.step(action)

        print("Step:", step_index)
        print("Action:", action)
        print("Next obs:", next_obs)
        print("Reward:", reward)
        print("Radius error:", info.get("radius_error"))
        print("Speed error:", info.get("speed_error"))
        print("Terminated:", terminated)
        print("Truncated:", truncated)
        print("-" * 40)

        obs = next_obs

        if terminated or truncated:
            break


if __name__ == "__main__":
    main()
```

---

# Observed Rollout Output

## Initial Observation

```text
Initial obs:
[ 0.0000000e+00  7.8749997e+12 -4.0433975e+03
  7.1296008e+02  7.1296008e+02]
```

Meaning:

```text
The environment provides the initial spacecraft state representation.
```

This observation belongs to:

```text
obs ∈ R^5
```

The observation vector represents:

```text
state representation
```

Examples:

```text
radius
velocity
angular velocity
angle
fuel
```

---

# Step-by-Step Closed Loop Interpretation

## Step 0

Action:

```text
[0.529367   0.94377923]
```

Environment transition:

```text
obs
→ action
→ env.step(action)
→ next_obs
```

Returned next observation:

```text
[-8.0848003e+03  7.8749997e+12 -4.0424001e+03
  7.1395728e+02  7.1395728e+02]
```

Reward:

```text
19.267724632783
```

Diagnostics:

```text
radius_error = 0.05000000019038867
speed_error = 0.024292158789168246
```

Termination state:

```text
terminated = False
truncated = False
```

Meaning:

```text
The environment did not stop.
The simulation continues.
```

---

## Important Day5 Chain

The most important system chain is:

```text
obs
→ action
→ next_obs
→ next_action
→ next_next_obs
→ ...
```

Meaning:

```text
Each new state becomes the basis for the next decision.
```

This is:

```text
closed-loop interaction
```

not:

```text
single-step calculation
```

---

# Meaning of reward

Important distinction:

```text
reward is NOT physics
```

Reward is:

```text
evaluation signal
```

The reward tells the controller/policy:

```text
how good the current behavior is
```

The reward does NOT:

```text
update physics
control gravity
change orbital equations
```

Physics is handled by:

```text
env.step(action)
```

---

# Meaning of info

Important distinction:

```text
info is NOT control
```

info is:

```text
diagnostics metadata
```

Examples:

```text
radius_error
speed_error
```

Purpose:

```text
monitoring
analysis
logging
debugging
```

The info dictionary helps engineers:

```text
understand system behavior
```

---

# Meaning of terminated / truncated

Observed output:

```text
terminated = False
truncated = False
```

Meaning:

```text
The rollout continued normally.
```

Important distinction:

```text
terminated
```

usually means:

```text
terminal condition reached
```

Examples:

```text
crash
success
invalid orbit
```

While:

```text
truncated
```

usually means:

```text
time limit reached
```

---

# Important Day5 Engineering Insight

Today was NOT:

```text
training PPO
modifying reward
changing OrbitEnv
```

Today WAS:

```text
understanding environment operational flow
```

The goal was:

```text
trace
inspect
interpret
```

not:

```text
optimize performance
```

---

# Connection to AI / PPO

A future PPO policy will eventually perform:

```text
policy(obs)
→ action
```

Meaning:

```text
R^5 → R^2
```

But today:

```text
random actions were used
```

This is important.

Today is only:

```text
environment operational interpretation
```

not:

```text
intelligent control
```

---

# Connection to Control Systems

The Day5 rollout already contains the minimal structure of:

```text
feedback control
```

Because:

```text
next decisions depend on next state
```

This creates:

```text
closed-loop behavior
```

---

# Day5 Final Summary

The most important sentence today is:

```text
OrbitEnv is a repeated state transition system.
```

Not:

```text
single-step computation
```

The most important chain is:

```text
obs
→ action
→ next_obs
→ next_action
```

This is the minimal foundation for:

```text
control systems
reinforcement learning
PPO
spacecraft autonomy
```

Today established:

```text
environment interaction intuition
```

before:

```text
policy optimization
```
