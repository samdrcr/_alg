# 5th Assignments: Advanced Recursion and Functional Paradigms

This repository contains algorithmic solutions focusing on state management, abstract syntax tree (AST) traversal, and strict functional programming paradigms. The primary objective across these tasks was to manipulate execution flow using recursion and custom data structures, specifically avoiding standard iterative constructs where required.

## 1. Tower of Hanoi: Call Stack Simulation

**Requirement:** Solve the Tower of Hanoi puzzle using both standard recursion and a strictly non-recursive approach.

**Implementation Details:**

- **Recursive Approach:** Utilized standard function call recursion to handle the divide-and-conquer logic of moving $n-1$ disks.
- **Iterative Approach (Non-Recursive):** I bypassed Python's internal call stack by engineering a manual Last-In-First-Out (LIFO) stack. By pushing execution states (tuples containing the action type, disk number, and peg positions) onto the list and popping them within a `while` loop, the algorithm accurately simulates recursive memory allocation. The instructions are appended in reverse order to ensure the LIFO structure executes them chronologically.

## 2. Symbolic Differentiation

**Requirement:** Build a recursive function `sym_diff(expr)` to calculate the mathematical derivative of symbolic expressions.

**Implementation Details:**

- I structured the mathematical expressions as an Abstract Syntax Tree (AST) using nested Python tuples, formatted as `(operator, left_operand, right_operand)`.
- The solution leverages recursion to traverse this tree. By evaluating the operator at the current node, the function dynamically applies the fundamental rules of calculus:
  - Constant and Identity rules for base cases.
  - The Sum/Difference rule for addition and subtraction.
  - The Product Rule `(u'v + uv')` and Quotient Rule `((u'v - uv') / v^2)` for multiplication and division.
- This approach keeps the logic strictly focused on structural traversal rather than string parsing.

## 3. Loop-Free Functional Sort

**Requirement:** Recreate the standard `map`, `filter`, and `reduce` functions entirely without loops, and utilize them to implement a Bubble Sort algorithm without `for` or `while` statements.

**Implementation Details:**

- **Functional Primitives:** I built `my_map`, `my_filter`, and `my_reduce` using structural recursion. Each function isolates the `head` (index 0) of the list, applies the lambda operation, and recursively concatenates the result with the evaluated `tail` (index 1 to end).
- **Algorithmic Integrity:** To implement a true Bubble Sort functionally, I separated the logic into a single-pass function (`bubble_pass`) that performs strictly adjacent comparisons and swaps.
- **Loop Replacement:** Standard Bubble Sort requires $n$ sequential passes to guarantee a sorted array. Instead of a `for` loop, I utilized `my_reduce`, passing the array itself as the iteration counter. This forces the `bubble_pass` function to execute exactly $n$ times, accumulating the sorted state cleanly and efficiently while avoiding the data-loss bugs common in naive functional sorting attempts.

---

_Documentation and logic refinement assisted by Gemini Pro LLM._
