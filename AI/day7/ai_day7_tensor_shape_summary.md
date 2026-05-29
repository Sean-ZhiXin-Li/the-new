# AI Day7 — Tensor Shape Consolidation

## Core Objective

Today is not about training, optimizer, backprop, or PPO.

Today is about tensor shape.

## Core Sentence

same numbers, different shape, different meaning

## Three Tensor Shapes

### scores

Shape: (3,)

Meaning: one-dimensional tensor with 3 action scores.

### score_column

Shape: (3,1)

Meaning: 2D tensor with 3 rows and 1 column.

### score_row

Shape: (1,3)

Meaning: 2D tensor with 1 row and 3 columns.

## Connection to Day3

Day3 used:

(3,2) @ (2,) -> (3,)

Meaning:

3 samples, 2 features per sample, 3 predictions.

## Connection to Day6

Day6 used:

scores -> argmax -> selected action

argmax returns the index of the largest score.

## Future Connection

Today:

scores
→ argmax
→ action

Future PPO:

observation tensor
→ neural network
→ action logits
→ probability distribution
→ sampled action

Tensor shapes make this entire pipeline possible.

## Final Insight

Tensor shape is not decoration.

Tensor shape defines how the AI system interprets data.