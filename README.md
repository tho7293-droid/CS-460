# Gale-Shapley Study Room Assignment

## Overview

This project implements the Gale-Shapley Stable Matching Algorithm to assign study groups to study rooms. Each study group ranks rooms by preference, and each room ranks study groups. The algorithm produces a stable assignment where no unmatched group-room pair would both prefer each other over their assigned match.

This project was completed for **CS 460 Algorithms Final Project**.

## Files

- `CS460.py` – Python implementation of the Gale-Shapley algorithm.
- `test_problem1.py` – Automated unit test (optional but recommended).
- `Trinh_Ho_final.pdf` – Final project report.

## Requirements

- Python 3.x

No additional libraries are required.

## Running the Program

Open a terminal in the project folder and run:

```bash
python CS460.py
```

Example output:

```
Final Matches:
GroupA -> Room1
GroupB -> Room2
GroupC -> Room3
```

## Running Tests

If `test_problem1.py` is included:

```bash
python -m unittest test_problem1.py
```

## Algorithm

The program uses the Gale-Shapley Stable Matching Algorithm.

1. Every unmatched group proposes to its highest-ranked room that has not yet rejected it.
2. A free room accepts the proposal.
3. A matched room keeps whichever group it prefers and rejects the other.
4. The process repeats until every group has been assigned a room.

The algorithm guarantees a stable matching.

## Time Complexity

- **Time:** O(n²)
- **Space:** O(n²)

where **n** is the number of study groups (and rooms).

## Repository

Final submission tag:

**v1.0-final**

## Author

Trinh Ho

CS 460 – Algorithms Final Project
