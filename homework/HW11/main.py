# AI Usage Declaration: This code was generated with the assistance of AI (Gemini).

import random
import math
import itertools

# ==========================================
# 1. 1D Numerical Derivative and Integral
# ==========================================
def derivative_1d(f, x, h=1e-5):
    """Calculates single-variable derivative using central difference."""
    return (f(x + h) - f(x - h)) / (2 * h)

def integral_1d_numerical(f, low, high, steps=1000):
    """Calculates single-variable integral using Riemann sum (midpoint rule)."""
    dx = (high - low) / steps
    total_area = 0.0
    for i in range(steps):
        midpoint = low + dx * (i + 0.5)
        total_area += f(midpoint) * dx
    return total_area

# ==========================================
# 2. 1D Monte Carlo Integral
# ==========================================
def integral_1d_mc(f, low, high, samples=10000):
    """Calculates single-variable integral using Monte Carlo method."""
    total = 0.0
    for _ in range(samples):
        x = random.uniform(low, high)
        total += f(x)
    volume = high - low
    return (total / samples) * volume

# ==========================================
# 3. n-D Numerical Derivative (Gradient)
# ==========================================
def gradient_nd(f, point, h=1e-5):
    """Calculates n-variable gradient."""
    n = len(point)
    grad = []
    for i in range(n):
        pt_plus = list(point)
        pt_minus = list(point)
        pt_plus[i] += h
        pt_minus[i] -= h
        partial_derivative = (f(pt_plus) - f(pt_minus)) / (2 * h)
        grad.append(partial_derivative)
    return grad

# ==========================================
# 5. n-D Riemann Integral
# ==========================================
def integral_riemann(f, low, high, steps_per_dim=10):
    """Calculates n-variable integral using a Riemann sum grid."""
    n = len(low)
    
    # Anti-crash mechanism for high dimensions
    total_iterations = steps_per_dim ** n
    if total_iterations > 5e6:
        return f"Skipped: Requires {total_iterations} iterations (Curse of Dimensionality)."
        
    ranges = []
    dxs = []
    for l, h in zip(low, high):
        dx = (h - l) / steps_per_dim
        dxs.append(dx)
        ranges.append([l + dx * (i + 0.5) for i in range(steps_per_dim)])
        
    dv = math.prod(dxs)
    total_sum = 0.0
    
    for point in itertools.product(*ranges):
        total_sum += f(point)
        
    return total_sum * dv

# ==========================================
# 4 & 6. n-D Monte Carlo Integral
# ==========================================
def integral_mc(f, low, high, samples=100000):
    """Calculates n-variable integral using Monte Carlo random sampling."""
    n = len(low)
    total_sum = 0.0
    
    for _ in range(samples):
        point = [random.uniform(low[i], high[i]) for i in range(n)]
        total_sum += f(point)
        
    volume = 1.0
    for l, h in zip(low, high):
        volume *= (h - l)
        
    return (total_sum / samples) * volume

# ==========================================
# Test Cases (Tasks 5 & 6)
# ==========================================
def f_test(x):
    """f(x) = x_1^2 + x_2^2 + ... + x_n^2"""
    return sum(xi**2 for xi in x)

if __name__ == "__main__":
    print("--- 1D Basic Tests ---")
    f_1d = lambda x: x**2
    print(f"Derivative of x^2 at x=2: {derivative_1d(f_1d, 2):.4f} (Expected: 4.0)")
    print(f"Integral of x^2 (0 to 1) [Numerical]: {integral_1d_numerical(f_1d, 0, 1):.4f} (Expected: 0.3333)")
    print(f"Integral of x^2 (0 to 1) [Monte Carlo]: {integral_1d_mc(f_1d, 0, 1):.4f}")
    
    print("\n--- n-D Gradient Test ---")
    print(f"Gradient of x^2 + y^2 at (1, 2): {gradient_nd(f_test, [1, 2])} (Expected: ~[2.0, 4.0])")

    print("\n--- Testing n-D Integrals (f(x) = sum(xi^2) from 0 to 1) ---")
    dimensions_to_test = [1, 2, 5, 100]
    
    for dim in dimensions_to_test:
        low = [0] * dim
        high = [1] * dim
        
        print(f"\nDimension n = {dim}")
        
        # 1. Riemann Test
        res_riemann = integral_riemann(f_test, low, high, steps_per_dim=5 if dim > 2 else 100)
        print(f"  Riemann Integral:    {res_riemann}")
        
        # 2. Monte Carlo Test
        res_mc = integral_mc(f_test, low, high, samples=100000)
        print(f"  Monte Carlo Integral:{res_mc:.6f}")
        
        print(f"  Expected Value:      {dim / 3:.6f}")