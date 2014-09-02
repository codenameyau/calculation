calculation
===========

Script that computes number combinations for Calculords

The goal:
> Given a list, L, of non-unique integers, and a number N:
> Find a way to calculate N using the integers in L at most once with the operations: +, -, *.

Actually, this problem is probably in NP. Non-deterministic polynomial time to solve, but polynomial time to verify.

It is related to the [Subset Sum problem](https://en.wikipedia.org/wiki/Subset_sum_problem)
except with an arbitary target number instead of zero, and three operations (+, -, *) instead of one (+).
