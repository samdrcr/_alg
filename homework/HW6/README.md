# LambdaCalc.py: A Pure Python Untyped Lambda Calculus Interpreter

> A minimalist, zero-dependency engine for exploring the foundations of computation.

Lambda calculus is a universal model of computation introduced by Alonzo Church in the 1930s. It has no primitive data types—no integers, no booleans, no arrays, and no built-in control structures. Everything is built entirely out of anonymous functions.

`LambdaCalc.py` is a strict, mathematical interpreter that parses standard lambda calculus notation and evaluates it step-by-step. The codebase itself has been intentionally stripped of all comments and docstrings, serving as a pristine, code-only artifact. This document acts as its official companion and architectural guide.

---

## ⚙️ How the Engine Works

This is a true interpreter, not a trick that leverages Python's internal `lambda` keyword. It processes lambda expressions through a complete compilation and evaluation pipeline:

1. **Tokenization & Parsing:** Converts strings like `\x y. x` into a formal Abstract Syntax Tree (AST).
2. **Immutable AST Nodes:** The entire state of the program is modeled using three `namedtuple` definitions:
   - `Var` (Variables, e.g., $x$)
   - `Abs` (Abstractions/Functions, e.g., $λx. M$)
   - `App` (Applications/Function Calls, e.g., $M N$)
3. **Normal-Order Reduction:** The engine finds the leftmost-outermost reducible expression (redex) and reduces it first. This strategy guarantees that if a program _can_ finish, it _will_ finish.
4. **Alpha-Conversion & Substitution:** The hardest problem in lambda calculus is variable capture (accidentally overwriting a variable of the same name). This engine automatically detects free variables and dynamically generates fresh names (e.g., $y'$) to preserve mathematical purity during substitution.

---

## 🔤 Syntax Guide

The parser accepts a clean, mathematician-friendly syntax:

| Element          | Notation         | Equivalent AST        |
| :--------------- | :--------------- | :-------------------- |
| **Variables**    | `x`, `y`, `z`    | `Var('x')`            |
| **Abstractions** | `\x.x` or `λx.x` | `Abs('x', Var('x'))`  |
| **Applications** | `M N`            | `App(M, N)`           |
| **Grouping**     | `(M N)`          | Explicit precedence   |
| **Sugar**        | `\x y. x`        | Desugars to `\x.\y.x` |

---

## 📚 The "Standard Library" (Church Encodings)

Because the language has no built-in data types, we must construct them from scratch. The interpreter injects a dictionary of macros at runtime. These macros use **Church Encodings** to represent logic and math purely through function application.

### Boolean Logic

Booleans are defined by how they choose between two arguments:

- `TRUE` = `\x y. x` _(returns the first argument)_
- `FALSE` = `\x y. y` _(returns the second argument)_
- `AND` = `\p q. p q p` _(if p is true, return q; if p is false, return p)_

### Church Numerals & Arithmetic

Numbers are defined by how many times they apply a function `f` to an argument `x`:

- `ZERO` = `\f x. x`
- `ONE` = `\f x. f x`
- `TWO` = `\f x. f (f x)`
- `SUCC` = `\n f x. f (n f x)` _(Successor: n + 1)_
- `PLUS` = `\m n f x. m f (n f x)` _(Addition: m + n)_

### Divergence

- `OMEGA` = `(\x. x x) (\x. x x)`
  _If you evaluate OMEGA, it returns OMEGA. It is an infinite loop._

---

## 💻 Running the Interpreter

To run the engine and execute the built-in examples, simply execute the file using Python 3:

```bash
python3 lambda_calculus.py
```

### Trace Output

Unlike standard interpreters that only spit out a final result, `LambdaCalc.py` prints the entire reduction trace. You can literally watch the functions expand, substitute, and collapse.

Example trace for calculating `1 + 1` (`SUCC ONE`):

```text
--- Example: Church numeral successor (1 -> 2) ---
Source: SUCC ONE
Step  0: (λn.λf.λx.f (n f x)) (λf.λx.f x)
Step  1: λf.λx.f ((λf.λx.f x) f x)
Step  2: λf.λx.f ((λx.f x) x)
Step  3: λf.λx.f (f x)
Result: λf.λx.f (f x)
```

### Automated Safety Checks

The script finishes by running a self-test suite. Most notably, it evaluates `(λy. x)[x := y]`. A flawed engine would produce `λy. y` (destroying the original meaning). The output will prove that this engine correctly alpha-renames the bound variable to produce `λy'. y`.

---

## 🛡️ Failsafes

To prevent the Python recursion limit from blowing up or the program from hanging forever on terms like `OMEGA`, the `reduce_steps()` function implements a hard cap of 200 beta-reductions. If a normal form is not reached by step 200, the evaluation is safely aborted.
