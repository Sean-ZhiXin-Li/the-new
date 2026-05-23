# Phase0 Day4 — OrbitEnv Observation / Action Flow

## Objective

Understand how a controller or PPO policy interacts with `OrbitEnv` without reading PPO internals, training models, changing reward, or modifying environment physics.

Core transition:

```text
Day3: I can trace one step.
Day4: I can explain how a controller makes decisions inside OrbitEnv rules.
```

---

## Source Boundary

Today only uses:

```text
Local repo: spacecraft-ai-controller
File: envs/orbit_env.py
Sections: __init__(), action_space, observation_space, reset(), _get_obs(), step(), info dict
```

Hard boundary:

```text
No PPO internals.
No training.
No reward tuning.
No OrbitEnv modification.
No Phase 7.6 controller deep dive.
```

---

## Minimal Check Script

```python
from envs.orbit_env import OrbitEnv


def main():
    env = OrbitEnv()

    obs, info = env.reset(seed=0)
    print("Reset obs shape:", obs.shape)
    print("Reset info:", info)

    action = env.action_space.sample()
    next_obs, reward, terminated, truncated, info = env.step(action)

    print("Action:", action)
    print("Action shape:", action.shape)
    print("Next obs shape:", next_obs.shape)
    print("Reward:", reward)
    print("Terminated:", terminated)
    print("Truncated:", truncated)
    print("Info keys:", list(info.keys())[:20])


if __name__ == "__main__":
    main()
```

---

## Actual Output

```text
Reset obs shape: (5,)
Reset info: {'start_mode': 'default', 'seed': 0, 'r0_over_target': 1.05}
Action: [-0.35593343 -0.45882097]
Action shape: (2,)
Next obs shape: (5,)
Reward: 19.2718989327351
Terminated: False
Truncated: False
Info keys: ['reward', 'shaping', 'bonus', 'penalty', 'radius_error', 'speed_error', 'progress', 'reward_radius_term', 'reward_progress_term', 'angle_cos', 'r_term', 'v_term', 'angle_term', 'steps', 'success_counter', 'terminal_bonus', 'success', 'terminated', 'truncated', 'a_cap_ref']
```

---

## API Flow

The basic interaction loop is:

```text
create env
→ reset(seed=0)
→ receive obs and info
→ sample or compute action
→ step(action)
→ receive next_obs, reward, terminated, truncated, info
```

In code form:

```text
obs, info = env.reset(seed=0)
action = controller(obs) or env.action_space.sample()
next_obs, reward, terminated, truncated, info = env.step(action)
```

---

## Observation Flow

The output shows:

```text
Reset obs shape: (5,)
Next obs shape: (5,)
```

Meaning:

```text
OrbitEnv observation dimension = 5
```

So the controller or PPO policy receives a 5-dimensional state representation.

Mental model:

```text
obs ∈ R^5
```

This means the policy interface is approximately:

```text
5-dimensional state → decision logic → action
```

Important interpretation:

```text
The observation is not the whole Python environment.
It is the compressed state vector exposed to the controller / policy.
```

---

## Reset Info

The reset call returned:

```text
{'start_mode': 'default', 'seed': 0, 'r0_over_target': 1.05}
```

Meaning:

```text
start_mode = default initialization mode
seed = reproducibility control
r0_over_target = initial radius / target radius
```

The value:

```text
r0_over_target = 1.05
```

means:

```text
initial radius is 1.05 times the target radius
```

So the spacecraft begins about 5% outside the target radius.

Engineering meaning:

```text
same seed + same config → same initial condition
```

This supports reproducible environment checks.

---

## Action Flow

The output shows:

```text
Action shape: (2,)
```

Meaning:

```text
OrbitEnv action dimension = 2
```

Mental model:

```text
action ∈ R^2
```

So the policy interface is:

```text
obs(5) → action(2)
```

or mathematically:

```text
policy: R^5 → R^2
```

Important distinction:

```text
The controller / PPO policy only produces an action.
OrbitEnv decides how that action affects the physical simulation.
```

---

## Step Flow

The call:

```python
next_obs, reward, terminated, truncated, info = env.step(action)
```

means:

```text
Take the action.
Apply environment rules.
Advance the simulation by one step.
Return the new state and diagnostics.
```

Conceptual sequence:

```text
action
→ action clipping / smoothing / thrust interpretation
→ physics update
→ new observation
→ reward computation
→ termination / truncation check
→ info diagnostics
```

Core rule:

```text
Controller does not own physics.
PPO does not own physics.
OrbitEnv owns the world rules.
```

---

## Reward and Diagnostics

The reward returned:

```text
19.2718989327351
```

This is a scalar evaluation of the current transition.

Today’s goal is not to tune or redesign reward. Today’s goal is to understand that reward is part of the environment feedback loop.

The `info` dictionary shows reward decomposition and diagnostics:

```text
reward
shaping
bonus
penalty
radius_error
speed_error
progress
reward_radius_term
reward_progress_term
angle_cos
r_term
v_term
angle_term
steps
success_counter
terminal_bonus
success
terminated
truncated
a_cap_ref
```

Key interpretation:

```text
radius_error → how far current radius is from target radius
speed_error → how far current speed is from desired speed
progress → whether the state is moving toward the objective
angle_cos → direction / alignment diagnostic
success_counter → persistent success tracking
success → current success flag
terminated / truncated → episode-ending status
```

This means `info` is not the controller decision itself. It is mainly for:

```text
debugging
logging
plotting
analysis
metrics
```

---

## Terminated vs Truncated

The output shows:

```text
Terminated: False
Truncated: False
```

Meaning:

```text
terminated = natural task ending condition was not reached
truncated = time-limit or artificial cutoff was not reached
```

So after this one step:

```text
the episode is still active
```

---

## Full Mental Model

```text
OrbitEnv = physics world + API rules + reward + diagnostics
Controller / PPO = decision maker
```

The loop is:

```text
obs
→ controller / PPO computes action
→ OrbitEnv.step(action)
→ physics update
→ reward + info
→ next_obs
→ repeat
```

The important separation is:

```text
Controller / PPO decides what to try.
OrbitEnv decides what actually happens.
```

---

## Day4 Insight

```text
OrbitEnv is not a model trainer.
OrbitEnv is the rule-defined simulation world.
```

A controller or policy does not directly change the orbit. It only outputs an action. The environment interprets that action under its physical and numerical rules.

---

## Final Summary

```text
obs_dim = 5
action_dim = 2
policy interface = R^5 → R^2
reset() initializes the world
step(action) advances the world
reward evaluates the transition
info explains the transition
```

One-line conclusion:

```text
OrbitEnv owns the physics; controller/PPO only proposes actions.
```

---
