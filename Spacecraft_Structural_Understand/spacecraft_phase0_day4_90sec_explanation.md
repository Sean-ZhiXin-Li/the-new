# Phase0 Day4 — 90 Second OrbitEnv Explanation

## 90 Second Explanation

`OrbitEnv` is the simulation environment for my spacecraft control project. It is not the controller and it is not PPO itself. It defines the world rules: the spacecraft state, the allowed action format, the physics update, the reward computation, and the diagnostic information.

The basic interaction starts with `reset()`. When I ran `env.reset(seed=0)`, the environment returned an observation with shape `(5,)`, so the controller or PPO policy receives a 5-dimensional state vector. The reset info showed `start_mode='default'`, `seed=0`, and `r0_over_target=1.05`, meaning this run starts in the default mode, is reproducible, and begins at about 1.05 times the target radius.

After reset, a controller or PPO policy would produce an action. In my check script I used `env.action_space.sample()` to generate a random legal action. The action shape was `(2,)`, so the decision interface is basically `R^5 → R^2`: a 5-dimensional observation goes into the decision maker, and a 2-dimensional action comes out.

Then `env.step(action)` sends that action into the environment. The controller does not directly own the physics. PPO also does not directly own the physics. `OrbitEnv` takes the action, applies its internal rules such as clipping, smoothing, thrust interpretation, physics update, reward calculation, and termination checks. It then returns `next_obs`, `reward`, `terminated`, `truncated`, and `info`.

In my run, the next observation still had shape `(5,)`, the reward was a scalar, and both `terminated` and `truncated` were false, meaning the episode continued. The `info` dictionary included diagnostics like `radius_error`, `speed_error`, `progress`, `angle_cos`, `success_counter`, and reward terms. These are not the action itself; they are used for debugging, logging, plotting, and understanding why the environment gave that reward.

The core idea is: `OrbitEnv` is the physics world and evaluation system, while the controller or PPO policy is only the decision maker that proposes actions inside that world.

---

## Ultra-Short Version

```text
OrbitEnv defines the world.
Controller / PPO proposes actions.
step(action) applies physics and returns next_obs, reward, done flags, and diagnostics.
```

---

## Technical Summary

```text
obs_dim = 5
action_dim = 2
reset(seed=0) → obs, info
step(action) → next_obs, reward, terminated, truncated, info
policy interface ≈ R^5 → R^2
```

---

## Key Sentence for Zoom

```text
The controller does not directly change the orbit; it outputs an action, and OrbitEnv decides how that action changes the simulated spacecraft state under the environment physics.
```
