#!/usr/bin/env python3
"""DPLL SAT solver via recursive backtracking and unit propagation."""

import sys

def parse_dimacs(text):
    """Parse DIMACS CNF text into (num_vars, clauses)."""
    tokens = []
    declared_vars = 0
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("c"):
            continue
        if line.startswith("p"):
            parts = line.split()
            if len(parts) >= 3:
                declared_vars = int(parts[2])
            continue
        tokens.extend(line.split())

    clauses = []
    current = []
    for tok in tokens:
        value = int(tok)
        if value == 0:
            clauses.append(current)
            current = []
        else:
            current.append(value)
    if current:
        clauses.append(current)

    max_literal = max((abs(lit) for clause in clauses for lit in clause), default=0)
    num_vars = max(declared_vars, max_literal)
    return num_vars, clauses

def simplify_clauses(clauses, literal):
    """
    Simplifies the formula given that `literal` is True.
    - Drops clauses containing `literal` (they are satisfied).
    - Removes `-literal` from remaining clauses (that option is false).
    """
    new_clauses = []
    for clause in clauses:
        if literal in clause:
            continue  # Clause is satisfied, drop it
        if -literal in clause:
            # Remove the false literal from the clause
            new_clause = [l for l in clause if l != -literal]
            new_clauses.append(new_clause)
        else:
            new_clauses.append(clause)
    return new_clauses

def dpll(clauses, assignment):
    """
    Core recursive DPLL algorithm.
    Returns (True, final_assignment) or (False, None).
    """
    # 1. Unit Propagation
    while True:
        unit_clauses = [c for c in clauses if len(c) == 1]
        if not unit_clauses:
            break
        
        # Force the assignment of the unit literal
        unit_lit = unit_clauses[0][0]
        assignment[abs(unit_lit)] = (unit_lit > 0)
        clauses = simplify_clauses(clauses, unit_lit)

    # 2. Base Cases (After Propagation)
    if not clauses:
        # All clauses satisfied and removed
        return True, assignment
    if any(len(c) == 0 for c in clauses):
        # Conflict: An empty clause means a requirement is impossible to meet
        return False, None

    # 3. Branching (Choose a variable and guess)
    # Heuristic: Pick the first literal from the shortest remaining clause
    shortest_clause = min(clauses, key=len)
    chosen_lit = shortest_clause[0]
    var = abs(chosen_lit)

    # Branch A: Try True for the chosen literal
    clauses_a = simplify_clauses(clauses, chosen_lit)
    assignment_a = dict(assignment)
    assignment_a[var] = (chosen_lit > 0)
    
    sat, final_assignment = dpll(clauses_a, assignment_a)
    if sat:
        return True, final_assignment

    # Branch B: Try False (Backtrack)
    clauses_b = simplify_clauses(clauses, -chosen_lit)
    assignment_b = dict(assignment)
    assignment_b[var] = (chosen_lit < 0)
    
    return dpll(clauses_b, assignment_b)

def solve(num_vars, clauses):
    """Execute DPLL and print the verdict."""
    print(f"Variables: {num_vars}   Clauses: {len(clauses)}")
    print("Formula (CNF):", format_formula(clauses) or "(empty -> trivially true)")
    print("\n[DPLL Execution Started...]")
    
    is_sat, model = dpll(clauses, {})
    
    if is_sat:
        # Fill in any variables that weren't assigned during DPLL
        # (meaning their value didn't matter to the outcome)
        for v in range(1, num_vars + 1):
            if v not in model:
                model[v] = True
                
        witness = " ".join(f"x{v}={'T' if model[v] else 'F'}" for v in range(1, num_vars + 1))
        print(f"\nResult: SATISFIABLE")
        print(f"  A satisfying assignment: {witness}")
        return True, model
    else:
        print("\nResult: UNSATISFIABLE")
        return False, None

def format_formula(clauses):
    """Human-readable CNF like: (x1 v ~x3) ^ (x2 v x3 v ~x1)."""
    def lit(l): return f"~x{abs(l)}" if l < 0 else f"x{l}"
    parts = []
    for clause in clauses:
        if not clause: parts.append("(FALSE)")
        else: parts.append("(" + " v ".join(lit(l) for l in clause) + ")")
    return " ^ ".join(parts)

# --- Built-in demonstration formulas ---
DEMOS = [
    ("Demo 1 -- satisfiable: (x1 v ~x3) ^ (x2 v x3 v ~x1)",
     3, [[1, -3], [2, 3, -1]]),
    ("Demo 2 -- unsatisfiable: (x1) ^ (~x1)",
     1, [[1], [-1]]),
]

def run_demos():
    for i, (title, num_vars, clauses) in enumerate(DEMOS):
        if i: print("\n" + "=" * 60 + "\n")
        print(title, "\n")
        solve(num_vars, clauses)

def run_file(path):
    try:
        with open(path, "r", encoding="utf-8") as fh: text = fh.read()
    except OSError as exc:
        print(f"Error: cannot read '{path}': {exc}", file=sys.stderr)
        return 1
    num_vars, clauses = parse_dimacs(text)
    print(f"Loaded DIMACS file: {path}\n")
    solve(num_vars, clauses)
    return 0

def main(argv):
    if len(argv) <= 1:
        run_demos()
        return 0
    return run_file(argv[1])

if __name__ == "__main__":
    sys.exit(main(sys.argv))