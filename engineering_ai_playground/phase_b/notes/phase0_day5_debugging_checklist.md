# Phase0 Day5 — Debugging Checklist

# Current Directory Checks

* Did I verify the current working directory using `pwd`?
* Am I inside the correct repository?
* Am I accidentally running commands from the home directory?
* Am I using relative paths correctly?

---

# tree Checks

* Did I accidentally run `tree` without depth limits?
* Did I use:

```bash
tree phase_b -L 2
```

instead of printing the entire repository?

* Did I verify the actual folder names before using grep or tail?

---

# grep Checks

* Did I spell the target directory correctly?
* Did I use quotation marks around the search keyword?
* Did I accidentally search the wrong directory?
* Did I forget `-R` for recursive search?
* Did I limit output using `head` when necessary?

Common typo example:

```text
experimenrts
```

Correct:

```text
experiments
```

Important lesson:

```text
“No such file or directory” often means path mistakes.
```

---

# tail Checks

* Did I read stdout or stderr intentionally?
* Did I accidentally inspect old experiments?
* Did I use:

```bash
latest=$(ls -1t phase_b/experiments | head -1)
```

before tracing the newest experiment?

* Did I use:

```bash
tail -n 30
```

instead of printing extremely large logs?

---

# stdout / stderr Checks

## stdout

Normal execution information:

```text
verification output
metrics
logging
status messages
```

## stderr

Error information:

```text
warnings
exceptions
tracebacks
runtime failures
```

Important distinction:

```text
stdout != stderr
```

---

# Return Code Checks

* Did I inspect `returncode`?
* Did I verify whether the process exited successfully?
* Did I remember:

| Code     | Meaning |
| -------- | ------- |
| 0        | Success |
| non-zero | Failure |

---

# Reproducibility Checks

* Did the experiment save a config snapshot?
* Is there a run manifest?
* Can I identify the exact entry script?
* Can I reproduce the run later?

---

# Engineering Mindset Checks

Today is NOT:

```text
changing code
changing hyperparameters
random experimentation
```

Today IS:

```text
trace
inspect
understand
```

Important Day5 engineering idea:

```text
Good engineering starts with understanding evidence.
```

Not:

```text
blindly changing systems
```
