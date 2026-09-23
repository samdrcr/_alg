# DPLL Boolean Satisfiability Solver

## Project Overview and Theoretical Background

The Boolean Satisfiability Problem (SAT) is the canonical NP-complete computational problem. It requires determining whether a given boolean formula can evaluate to true under a specific assignment of boolean variables. Because it is NP-complete, no known algorithm can solve all SAT instances in polynomial time. However, practical applications in hardware verification, automated theorem proving, and software dependency resolution necessitate efficient solving mechanisms.

This repository implements a dependency-free Boolean Satisfiability solver in Python, utilizing the Davis-Putnam-Logemann-Loveland (DPLL) algorithm.

### Transitioning from Brute Force to Heuristic Search

Naive SAT solving relies on full truth-table enumeration, requiring $\mathcal{O}(2^n)$ operations for $n$ variables. This exponential scaling restricts pure brute-force approaches to trivial datasets.

The DPLL algorithm optimizes this process by treating SAT as a constraint satisfaction problem. Rather than generating arbitrary combinations, DPLL utilizes local constraint data to infer global variable assignments, pruning the search tree and preempting dead branches before computation is wasted.

### Algorithm Mechanics

The solver processes boolean formulas strictly in Conjunctive Normal Form (CNF), where a formula is a conjunction (AND) of disjunctive clauses (OR). The implementation relies on three core operations:

1.  **Unit Propagation (Boolean Constraint Propagation):**
    If a clause is reduced to a single unassigned literal, that literal is strictly constrained and must be evaluated as True. The algorithm identifies these unit clauses, enforces the required assignment, and recursively simplifies the formula. This process cascades, frequently resolving significant portions of the problem space without branching.

2.  **State Simplification:**
    Upon assigning a variable, the logical state of the formula is updated immediately:
    - Clauses containing a satisfied literal are discarded entirely.
    - Falsified literals are removed from unresolved clauses, reducing their length and potentially generating new unit clauses.

3.  **Chronological Backtracking:**
    When deterministic constraint propagation halts, the algorithm selects an unassigned variable and branches the search space. If a subsequent assignment sequence results in an empty clause (a logical contradiction), the algorithm backtracks, reverses the assignment, and explores the alternate branch. The solver defaults to a minimal-length clause heuristic to select branching variables.

---

## Technical Documentation

### Prerequisites

The software is implemented in pure Python to maximize cross-platform compatibility. It requires no external libraries.

- Python 3.6 or higher.

### Execution

The application functions as a command-line utility. It executes built-in diagnostic formulas by default and accepts external files following the DIMACS CNF specification.

**Execute diagnostic tests:**

```bash
python3 dpll_solver.py
```

**Evaluate a target CNF file:**

```bash
python3 dpll_solver.py path/to/problem.cnf
```

**Access standard output documentation:**

```bash
python3 dpll_solver.py --help
```

### DIMACS CNF Specification Support

The system ingests constraint logic via the DIMACS CNF format, the standard encoding protocol for industrial SAT applications.

**Parsing Rules:**

- Variables are strictly mapped to positive integers (1, 2, 3).
- Logical negations are mapped to negative integers (-1, -2, -3).
- Lines prefixed with `c` operate as comments and bypass the tokenization phase.
- The metadata header must strictly follow the format: `p cnf [variable_count] [clause_count]`.
- Clauses are represented as space-delimited integer arrays, terminated by `0`.

**Sample Encoding (`target.cnf`):**

```text
c Sample constraint definitions
c Mathematical representation: (x1 v ~x2) ^ (~x1 v x2 v x3) ^ (~x3)
p cnf 3 3
1 -2 0
-1 2 3 0
-3 0
```

### Execution Output

Upon successful parsing and evaluation, the solver standardizes the output to display the system metadata, the reconstructed mathematical CNF, and the final logic state. Satisfiable results include a validating boolean model.

```text
Variables: 3   Clauses: 3
Formula (CNF): (x1 v ~x2) ^ (~x1 v x2 v x3) ^ (~x3)

[DPLL Execution Started...]

Result: SATISFIABLE
  A satisfying assignment: x1=F x2=F x3=F
```

If the internal constraints yield an unavoidable logical contradiction, the system outputs `UNSATISFIABLE`.

### Internal Architecture

- `parse_dimacs(text)`: A lexical parser that processes variable-length DIMACS inputs into standardized integer arrays.
- `simplify_clauses(clauses, literal)`: The mutation layer responsible for pruning the constraint arrays based on active assignments.
- `dpll(clauses, assignment)`: The recursive core managing the unit propagation, conflict detection, and decision tree traversal.
- `solve(num_vars, clauses)`: The high-level abstraction layer that manages data formatting and terminal output.

---

## Acknowledgments and Agent Integration

The conceptualization, architecture design, and technical documentation of this project were developed utilizing programmatic assistance from large language model agents. Specifically, the base DPLL logical translation and code structuration were executed in collaboration with Google Gemini, utilized as an integrated engineering agent to optimize algorithm efficiency and standard output formatting.
