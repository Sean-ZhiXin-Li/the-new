# Day6 Notes

## What sort() Does

sort() rearranges data according to a rule.

By default, the rule is ascending order.

Time complexity:

O(n log n)

sort is important because it makes later analysis easier.

## Comparator

A comparator defines the sorting rule.

The comparator answers this question:

"Should a go before b?"

Examples:

- smaller number first
- larger number first
- lower distance first
- higher score first

## Why pair Is Useful

pair stores two related values together.

Examples:

- time and priority
- score and id
- distance and action_id

Many engineering systems use grouped data instead of single numbers.

## Core Understanding Today

Sorting is not just about numbers.

Sorting is about:

- organization
- ranking
- selection
- system rules

## Comparator Result

Default pair sorting:
first ascending, then second ascending.

Custom comparator:
first ascending, then second descending.

This means:

- smaller time goes first
- if time is the same, higher priority goes first

Comparator defines the system priority rule.
