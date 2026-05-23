# Spacecraft Phase 0 Day 2 — OrbitEnv Structural Trace

## Objective

Understand `OrbitEnv` as the physical world and Gym-style interface that controllers and PPO policies operate inside.

This phase is not about PPO training, reward tuning, or changing physics.

This phase is:

```text
Read environment structure → understand state/action → trace one simulation step
```

---

# Core Mental Model

```text
OrbitEnv = physics world + API rules
Controller / PPO = decision maker inside that world
```

`OrbitEnv` itself does not decide intelligently. It defines the environment, dynamics, observations, rewards, termination conditions, and diagnostic information.

---

# Reading Order

```text
1. envs/orbit_env.py top docstring
2. action_space
3. observation_space
4. _get_obs()
5. step(action)
```

---

# 1. Top Docstring

The docstring defines the environment as:

```text
2D Newtonian orbital environment with thrust control
```

Meaning:

```text
A spacecraft moves in a 2D orbital world.
Gravity pulls it toward the central body.
The controller outputs thrust commands.
The environment updates motion using physics.
```

The key physics chain is:

```text
action → thrust vector → thrust acceleration → velocity update → position update
```

Important equations from the environment design:

```text
thrust_vec = thrust_scale * action
a_thrust = thrust_vec / mass
```

So action does not directly move the spacecraft. Action creates thrust. Thrust creates acceleration. Acceleration changes velocity. Velocity changes position.

---

# 2. action_space

Code meaning:

```python
self.action_space = spaces.Box(low=-1.0, high=1.0, shape=(2,), dtype=np.float32)
```

Interpretation:

```text
action is a 2D vector
each component is between -1 and 1
```

Conceptually:

```text
action = [x_direction_command, y_direction_command]
```

It is a normalized control command, not direct physical acceleration.

Inside `step(action)`, the action is clipped and scaled:

```text
action [-1, 1] → thrust vector → thrust acceleration
```

This means the controller chooses a 2D thrust direction and magnitude pattern, while the environment converts that command into physics.

---

# 3. observation_space

Code meaning:

```python
self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(5,), dtype=np.float32)
```

Interpretation:

```text
observation is a 5-dimensional vector
```

The actual observation is returned by `_get_obs()`:

```text
[x, y, vx, vy, v_r]
```

Meaning:

```text
x   = current x position
y   = current y position
vx  = current x velocity
vy  = current y velocity
v_r = radial velocity
```

AI / control connection:

```text
observation = feature vector
state = [x, y, vx, vy, v_r]
action = f(state)
```

This connects directly to the AI Day 2 model:

```text
features → model/controller → output
```

---

# 4. `_get_obs()`

Core code idea:

```python
r = np.linalg.norm(self.pos)
v_r = dot(self.pos, self.vel) / r
return [x, y, vx, vy, v_r]
```

## `r`

```text
r = distance from central body
```

Mathematically:

```text
r = sqrt(x^2 + y^2)
```

## `v_r`

```text
v_r = radial velocity
```

It measures how much of the velocity points toward or away from the central body.

Interpretation:

```text
v_r > 0  → spacecraft is moving outward
v_r < 0  → spacecraft is moving inward
v_r ≈ 0  → spacecraft is mostly moving tangentially
```

Why this matters:

```text
Stable orbit requires radial velocity to stay controlled.
If v_r is too positive, the spacecraft escapes outward.
If v_r is too negative, the spacecraft falls inward.
If v_r is near zero with correct tangential speed, the orbit is more stable.
```

---

# 5. `step(action)` Structural Trace

`step(action)` advances the simulation by one time step.

The Gym-style return format is:

```text
observation, reward, terminated, truncated, info
```

---

## Stage 1 — Step Counter and Previous Position

```python
self.steps += 1
prev_pos = self.pos.copy()
```

Meaning:

```text
Move to the next simulation frame.
Save previous position for reward/progress calculations.
```

---

## Stage 2 — Action Clipping and Smoothing

The raw action is clipped:

```text
action = clip(action, -1, 1)
```

Meaning:

```text
The environment prevents invalid control commands.
```

If action smoothing is enabled, the action cannot change too suddenly:

```text
action_delta = clipped change from previous action
action_executed = previous action + limited delta
```

Engineering meaning:

```text
Control commands should not jump violently between steps.
Smoothing makes the simulation more stable and more realistic.
```

---

## Stage 3 — Action to Thrust to Acceleration

```text
thrust = thrust_scale * action_executed
acc_thrust = thrust / mass
```

Physics meaning:

```text
F = ma
therefore a = F / m
```

Control meaning:

```text
The controller does not directly set velocity or position.
It only provides thrust commands.
```

---

## Stage 4 — Gravity Acceleration

The environment computes gravity from a central point mass:

```text
acc_gravity = -mu * r_vec / r^3
```

Meaning:

```text
Gravity always pulls the spacecraft toward the origin.
```

Why `r^3` appears:

```text
gravity magnitude follows 1/r^2
direction uses r_vec / r
combined form becomes r_vec / r^3
```

---

## Stage 5 — Euler Integration

Core update:

```text
new velocity = old velocity + total acceleration * dt
new position = old position + new velocity * dt
```

In code form:

```text
vel = vel + (acc_gravity + acc_thrust) * dt
pos = pos + vel * dt
```

This is the central simulation loop.

Full causal chain:

```text
action → thrust → acceleration → velocity → position → new observation
```

---

## Stage 6 — Orbit Capture Assist

The environment has an optional assist mechanism.

If the spacecraft is already close to the target circular orbit:

```text
small radius error
small speed error
```

then the velocity is softly blended toward ideal tangential circular velocity.

Meaning:

```text
close to orbit → softly stabilize tangential velocity
```

Important boundary:

```text
This is an environment assist mechanism, not PPO intelligence.
```

For Day 2, only understand that it exists. Do not tune it yet.

---

## Stage 7 — Success and Termination Logic

The environment checks whether the spacecraft is inside a success tolerance window.

```text
if inside tolerance:
    success_counter += 1
else:
    success_counter = 0
```

Meaning:

```text
One good moment is not enough.
The spacecraft must remain stable for multiple steps.
```

Termination conditions include:

```text
success
out_range
overspeed
too_close
radial_stall_fail
time_up
```

Important distinction:

```text
terminated = natural success/failure ending
truncated = time limit reached
```

This matters for experiment analysis because timeout is different from physical failure.

---

## Stage 8 — Reward and Info

The environment calls:

```python
compute_reward(...)
```

This produces diagnostic reward components such as:

```text
reward
shaping
bonus
penalty
radius_error
speed_error
progress
```

The `info` dictionary stores detailed diagnostics, including:

```text
radius_error
speed_error
success
terminated
truncated
thrust_vec
acc_thrust
acc_gravity
acc_total
radial_stall
orbit_lock_counter
```

Meaning:

```text
reward tells whether the current step was good or bad
info explains why
```

For research/debugging, `info` is extremely important because it turns black-box simulation into measurable evidence.

---

# Component Table

| Component     | Meaning                       | Why Important                      |
| ------------- | ----------------------------- | ---------------------------------- |
| `pos`         | `[x, y]` position             | Defines spacecraft location        |
| `vel`         | `[vx, vy]` velocity           | Defines motion direction and speed |
| `action`      | 2D normalized thrust command  | Controller output                  |
| `thrust`      | Scaled physical force         | Connects control to physics        |
| `acc_gravity` | Gravity acceleration          | Core orbital dynamics              |
| `acc_thrust`  | Thrust acceleration           | Propulsion control effect          |
| `_get_obs()`  | Returns `[x, y, vx, vy, v_r]` | Controller / AI input              |
| `reward`      | Task performance score        | Learning and evaluation signal     |
| `terminated`  | Success/failure ending        | Experiment boundary                |
| `truncated`   | Time-limit ending             | Separates timeout from failure     |
| `info`        | Diagnostics dictionary        | Debugging and analysis evidence    |

---

# Core Engineering Understanding

Before this read:

```text
I knew OrbitEnv was the environment file.
```

After this read:

```text
I understand that OrbitEnv defines the physical world, the control interface, the state representation, the simulation update, reward signals, and termination boundaries.
```

---

# Connection to Math Day 2

Math concept:

```text
vector = state / direction / quantity
```

OrbitEnv application:

```text
position vector = [x, y]
velocity vector = [vx, vy]
action vector = [ax_command, ay_command]
observation vector = [x, y, vx, vy, v_r]
```

Linear combination intuition appears in physics updates:

```text
total acceleration = gravity acceleration + thrust acceleration
```

---

# Connection to AI Day 2

AI Day 2 model:

```text
prediction = dot(features, weights) + bias
```

OrbitEnv connection:

```text
features = observation = [x, y, vx, vy, v_r]
controller / policy = function of state
action = output of controller / policy
```

A simple future controller could score a state using:

```text
score = dot(state, weights) + bias
```

This is not the final spacecraft controller, but it shows why vectorized AI models connect naturally to environment states.

---

# 90-Second Explanation

```text
OrbitEnv is a 2D Newtonian orbital simulation environment. The spacecraft state is represented by position, velocity, and radial velocity: [x, y, vx, vy, v_r]. The controller outputs a 2D normalized action in [-1, 1], which is scaled into a thrust vector. The environment computes thrust acceleration using F = ma, adds gravity from the central body, and updates velocity and position with Euler integration. After each step, it checks whether the spacecraft is close enough to the target circular orbit, whether it has failed by escaping, overspeeding, getting too close, or stalling radially, and then returns observation, reward, termination flags, and diagnostic info.
```

---

# Hard Boundary

Do not do these today:

```text
Do not train PPO.
Do not tune rewards.
Do not change physics parameters.
Do not modify OrbitEnv.
Do not analyze PPO clipping.
Do not jump into controller phase logic yet.
```

---

# Day 2 Win Condition

```text
✔ Can explain action_space
✔ Can explain observation_space
✔ Can explain _get_obs()
✔ Can explain action → thrust → acceleration → velocity → position
✔ Can explain terminated vs truncated
✔ Can explain why info is useful for debugging
✔ Can explain OrbitEnv as the world, not the decision maker
```

---

# One-Sentence Summary

```text
OrbitEnv defines the spacecraft's physical world and Gym interface: it receives thrust actions, updates orbital motion using gravity and thrust, returns state observations, and records reward/termination diagnostics for controllers and learning algorithms.
```
