# Iteration Methods Assignment

**Name:** 范權榮
**Student ID:** 111210557

This repository contains two primary components for Week 4's algorithm assignment, demonstrating the power and universality of iterative methods in computational mathematics:

1. A custom mathematical problem demonstrating the iterative approach and convergence analysis (`custom_problem.py`).
2. A comprehensive analysis and explanation of the `iter_framework.py` core framework and its classical algorithm implementations.

---

## Part 1: Custom Iteration Problem (Golden Ratio)

Based on the numerical concepts presented in the course materials (`iterative3.py`), I designed a custom problem to solve for the **Golden Ratio**, denoted by the Greek letter $\phi$ (phi).

The Golden Ratio is mathematically defined as the positive root of the quadratic equation:
$$f(x) = x^2 - x - 1 = 0$$

The exact analytical solution is $\phi = \frac{1 + \sqrt{5}}{2} \approx 1.6180339887...$

To solve this using iterative methods, we must algebraically rearrange the base equation $f(x) = 0$ into a fixed-point iteration form: $x = g(x)$. According to the **Banach Fixed-Point Theorem**, an iterative sequence $x_{k+1} = g(x_k)$ will successfully converge to the fixed point $x^*$ if the absolute value of the derivative at that point is strictly less than 1 (i.e., $\vert{}g'(x^*)\vert{} < 1$). The smaller the derivative, the faster the convergence.

I implemented three different transformations of the equation to demonstrate divergence, linear convergence, and quadratic convergence.

### 1. Method 1: The Divergent Form

By isolating the $x$ term, we can write the equation as:
$$x = x^2 - 1 \implies g_1(x) = x^2 - 1$$

- **Derivative Analysis:** $g_1'(x) = 2x$.
- **Convergence Check:** Near the target root $\phi \approx 1.618$, the derivative evaluates to $\vert{}g_1'(\phi)\vert{} \approx 3.236$.
- **Result:** Because $3.236 > 1$, this fixed point is mathematically a "repeller." The sequence rapidly explodes toward infinity, as demonstrated in the script's output where it reaches $1.57 \times 10^7$ by the 5th iteration.

### 2. Method 2: Linear Convergence Form (Continued Fraction)

By dividing the original equation by $x$, we get:
$$x - 1 - \frac{1}{x} = 0 \implies x = 1 + \frac{1}{x} \implies g_2(x) = 1 + \frac{1}{x}$$

- **Derivative Analysis:** $g_2'(x) = -\frac{1}{x^2}$.
- **Convergence Check:** Near the root, $\vert{}g_2'(\phi)\vert{} = \frac{1}{\phi^2} \approx 0.3819$.
- **Result:** Because $0.3819 < 1$, the sequence converges. The negative sign in the derivative indicates that the sequence will oscillate around the root (alternating above and below it) while converging linearly. This exactly models the famous continued fraction expansion of the Golden Ratio.

### 3. Method 3: Quadratic Convergence (Newton-Raphson Method)

Using the Newton-Raphson formula $g(x) = x - \frac{f(x)}{f'(x)}$, with $f(x) = x^2 - x - 1$ and $f'(x) = 2x - 1$:
$$g_3(x) = x - \frac{x^2 - x - 1}{2x - 1} = \frac{x^2 + 1}{2x - 1}$$

- **Derivative Analysis:** By design, Newton's method yields $g_3'(\phi) = 0$ at the root.
- **Result:** Because the first derivative is exactly zero, the method achieves **quadratic convergence**. This means the number of accurate decimal places roughly doubles with every single iteration step. In the script execution, Method 3 achieves full 10-decimal-place double-precision accuracy in just 4 iterations.

---

## Part 2: Explanation of the `iter_framework.py` Software Architecture

The provided `iter_framework.py` file demonstrates a profound abstraction pattern in computer science and numerical analysis: **almost all complex numerical algorithms can be modeled as a single, generic Fixed-Point Iteration.**

### 1. The Core Abstraction (`generic_iterator`)

The `generic_iterator` function acts as a unified scaffold. It completely decouples the _control flow_ of the iteration from the _business logic_ (the specific mathematics) of the algorithm.

```python
def generic_iterator(transition_func, is_converged, initial_state, max_iter=1000):
```

It reduces any iterative algorithm down to three injected behaviors:

- `initial_state`: The starting guess $x_0$. Because Python is dynamically typed, this state is heavily polymorphic. It can be a scalar (Newton's method), a 1D vector (PageRank), a 2D matrix (QR algorithm), or even a custom tuple containing time and state variables (RK4).
- `transition_func`: A callable function representing $x_{k+1} = g(x_k)$. It calculates the next state based solely on the current state.
- `is_converged`: A callable function that inspects the `old_state`, `new_state`, and `iteration_count` to determine if the algorithm should halt.

**Advantages of this Architecture:**

1. **DRY Principle (Don't Repeat Yourself):** Standard boilerplate code like `for` loops, maximum iteration limits, and early-stopping mechanisms are written only once.
2. **Testability:** The mathematical transition logic can be isolated and unit-tested without worrying about loop conditions.
3. **Readability:** When implementing a new algorithm, the developer only needs to define the pure math formulas.

### 2. How the 9 Classical Examples Map to the Framework

The framework successfully handles algorithms across completely different branches of mathematics by mapping them to the `transition_func` and `is_converged` paradigms:

#### A. Root Finding & Optimization

- **Fixed-Point Iteration (2D):** The state is a 2D coordinate vector. The transition is a simple affine transformation matrix. Convergence is checked using the L2 Norm (Euclidean distance) between steps.
- **Newton's Method:** The transition function is $x - f(x)/f'(x)$. State is a 1D scalar.

#### B. Linear Algebra

- **Gauss-Seidel Solver:** Solves $Ax = b$. The transition function updates a vector coordinate-by-coordinate in place.
- **Power Iteration:** Finds the dominant eigenvalue. The transition function simply multiplies a vector by Matrix $A$ and normalizes it.
- **QR Algorithm:** Finds all eigenvalues. The transition function performs a QR decomposition of $A$, then reverses the multiplication $R \times Q$ to form the next state matrix.

#### C. Calculus & Graph Theory

- **Runge-Kutta 4 (RK4):** Used for solving ODEs. The state is a tuple of `(time, y)`. The transition function calculates 4 weighted slopes to step forward in time. Interestingly, the `is_converged` function here does _not_ check for mathematical convergence; it simply checks if `time >= time_end`, demonstrating the flexibility of the framework.
- **PageRank (Web Surfer Model):** The state is a probability distribution of web surfers. The transition function multiplies this state by the Google Matrix (incorporating a damping factor to prevent dead-ends).

#### D. Machine Learning & Statistics

- **K-Means Clustering (Hard EM):** The `transition_func` packages two steps together. First, it calculates the distances of all points to current centroids (E-step). Then, it calculates the mean of those assignments to output new centroids (M-step).
- **EM Algorithm (Two-Coin Problem):** Similar to K-Means but handles probability distributions (Soft EM). The transition updates the latent probability weights and recalculates the maximum likelihood parameters for the coins.

### Conclusion

By studying this framework, we see that whether we are training an Artificial Intelligence model (K-Means/EM), simulating physics (Runge-Kutta), ranking websites (PageRank), or doing pure linear algebra, we are ultimately just looping $x_{k+1} = g(x_k)$ until the system reaches a stable mathematical equilibrium.
