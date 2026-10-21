# Algorithm Analysis: Longest Common Subsequence (LCS)

## 1. Project Overview

This project provides an in-depth algorithmic comparison of two different approaches to solving the **Longest Common Subsequence (LCS)** problem. The LCS algorithm is a fundamental computer science concept used as the underlying mathematical engine for UNIX `diff` commands, Git version control file comparisons, and bioinformatics (DNA sequence alignment).

The project consists of two Python scripts that solve the exact same problem using two distinct computational paradigms:

1. **`lcs_non_dp.py`**: A pure Brute-Force / Backtracking approach.
2. **`lcs_dynamic.py`**: A highly optimized Dynamic Programming (DP) approach.

By benchmarking these two scripts, we can empirically prove the critical importance of algorithmic optimization when dealing with overlapping subproblems.

---

## 2. Problem Definition

Given two sequences (strings) $A$ and $B$, the goal is to find the length of the longest subsequence present in both of them.

- A **subsequence** is a sequence that appears in the same relative order, but not necessarily contiguous.
- **Example:** For strings `"ABCBDAB"` and `"BDCAB"`, the LCS is `"BCAB"` (or `"BDAB"`), with a length of $4$.

---

## 3. Approach 1: Non-Dynamic Programming (Brute-Force)

### File: `lcs_non_dp.py`

### 3.1. Theoretical Principle

The brute-force method operates on a pure exhaustive search model. The algorithm systematically generates every single possible subsequence of the shorter string. For each generated subsequence, it scans the longer string using a two-pointer technique to check if it constitutes a valid common subsequence. It keeps track of the maximum length found.

### 3.2. Complexity Analysis

Let $m$ be the length of the shorter string and $n$ be the length of the longer string.

- **Time Complexity: $\mathcal{O}(n \cdot 2^m)$**
  A string of length $m$ has exactly $2^m$ possible subsequences. Generating and verifying each one against a string of length $n$ requires linear time $\mathcal{O}(n)$. This exponential time complexity causes the "combinatorial explosion" phenomenon.
- **Space Complexity: $\mathcal{O}(m)$**
  The space is primarily consumed by the system's Call Stack during recursion. The maximum depth of the recursive tree is exactly $m$.

---

## 4. Approach 2: Dynamic Programming (DP)

### File: `lcs_dynamic.py`

### 4.1. Theoretical Principle

The LCS problem exhibits two crucial properties: **Optimal Substructure** and **Overlapping Subproblems**. Instead of recalculating the same subsequences repeatedly, the Dynamic Programming approach uses memoization/tabulation.

It constructs a 2D matrix (`dp`) of size $(m+1) \times (n+1)$, where the value at `dp[i][j]` represents the length of the LCS for the prefix of string A (up to $i$) and the prefix of string B (up to $j$).

**State Transition Equations:**

1. **Base Case:** `dp[i][0] = 0` and `dp[0][j] = 0` (An empty string yields an LCS of 0).
2. **Match (If $A[i-1] == B[j-1]$):**
   `dp[i][j] = dp[i-1][j-1] + 1`
3. **Mismatch (If $A[i-1] \neq B[j-1]$):**
   `dp[i][j] = \max(dp[i-1][j], dp[i][j-1])`

### 4.2. Complexity Analysis

- **Time Complexity: $\mathcal{O}(m \cdot n)$**
  The algorithm utilizes two nested loops to traverse the matrix. The calculation inside the inner loop is a simple state check and assignment, which takes $\mathcal{O}(1)$ constant time.
- **Space Complexity: $\mathcal{O}(m \cdot n)$**
  The algorithm requires allocating memory for the 2D matrix. (Note: This can be further optimized to $\mathcal{O}(\min(m, n))$ using a 1D array if only the length is required, but the 2D matrix is standard for tracing back the actual string).

---

## 5. Performance Benchmark & Empirical Results

Both scripts have been equipped with Python's `time.perf_counter()` to provide high-precision profiling.

### Benchmark Parameters

- **Input String A:** `"ABCBDABQWERTYUIOP"` (Length: 17)
- **Input String B:** `"BDCABQWERTYUIOP"` (Length: 15)

### Expected Execution Results

| Metric             | Brute-Force (Non-DP)  | Dynamic Programming (DP)     |
| :----------------- | :-------------------- | :--------------------------- |
| **LCS Length**     | 12                    | 12                           |
| **Execution Time** | ~1.5 to 3.0 seconds   | ~0.0001 seconds              |
| **Calculations**   | Hundreds of thousands | Exactly $17 \times 15 = 255$ |

_Note: Actual execution time varies based on CPU architecture, but the relative scale remains the same._

### Conclusion

As demonstrated by the benchmarking data, the Non-DP approach becomes computationally paralyzing even with extremely small inputs (around length 15-20). The Dynamic Programming approach reduces an exponential-time problem into a polynomial-time problem, showcasing why DP is the absolute industry standard for file diffing algorithms and sequence alignment systems.
