# Numerical and Monte Carlo Calculus Project

**AI Usage Declaration:** Both this `README.md` file and the source code in `main.py` were written with the assistance of an AI (Gemini).

## Overview

This project implements numerical methods and Monte Carlo simulations for calculating derivatives and integrals in both 1-dimensional and n-dimensional spaces.

## Features

1. **Single-Variable Calculus:**
   - Grid-based midpoint Riemann sum for integrals.
   - Central difference method for derivatives.
   - Monte Carlo randomized sampling for integrals.
2. **Multi-Variable (n-D) Calculus:**
   - Partial derivative gradient computation.
   - n-Dimensional hypervolume integration via recursive grid (Riemann).
   - n-Dimensional hypervolume integration via Monte Carlo.

## Observation: The Curse of Dimensionality

As tested in this project with dimensions $n=1, 2, 5, 100$ integrating $f(x) = \sum x_i^2$:

- The **Riemann Sum** fails at higher dimensions (like $n=100$) because the number of grid points grows exponentially ($grid\_size^n$). A grid of just 2 points per dimension in 100D would require $2^{100}$ evaluations, rendering it computationally impossible.
- The **Monte Carlo Method** scales brilliantly. It successfully approximates the integral for $n=100$ in a fraction of a second, proving its necessity for high-dimensional mathematics (such as machine learning and thermodynamics).

## How to Run

Run the test script via the terminal:
`python3 main.py`
