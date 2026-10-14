from collections import namedtuple
import re

Var = namedtuple('Var', 'name')
Abs = namedtuple('Abs', 'param body')
App = namedtuple('App', 'func arg')

def free_vars(term):
    if isinstance(term, Var):
        return {term.name}
    elif isinstance(term, Abs):
        return free_vars(term.body) - {term.param}
    elif isinstance(term, App):
        return free_vars(term.func) | free_vars(term.arg)
    raise TypeError(f"Unknown term type: {type(term)}")

def fresh_name(name, avoid_set):
    while name in avoid_set:
        name += "'"
    return name

def subst(term, x, N):
    if isinstance(term, Var):
        return N if term.name == x else term
        
    elif isinstance(term, App):
        return App(subst(term.func, x, N), subst(term.arg, x, N))
        
    elif isinstance(term, Abs):
        y = term.param
        M = term.body
        
        if y == x:
            return term
            
        if y not in free_vars(N):
            return Abs(y, subst(M, x, N))
            
        y_prime = fresh_name(y, free_vars(M) | free_vars(N) | {x})
        
        alpha_renamed_M = subst(M, y, Var(y_prime))
        
        return Abs(y_prime, subst(alpha_renamed_M, x, N))
        
    raise TypeError(f"Unknown term type: {type(term)}")

def step(term):
    if isinstance(term, Var):
        return term, False
        
    elif isinstance(term, Abs):
        new_body, reduced = step(term.body)
        return Abs(term.param, new_body), reduced
        
    elif isinstance(term, App):
        if isinstance(term.func, Abs):
            return subst(term.func.body, term.func.param, term.arg), True
            
        new_func, reduced = step(term.func)
        if reduced:
            return App(new_func, term.arg), True
            
        new_arg, reduced = step(term.arg)
        return App(term.func, new_arg), reduced
        
    raise TypeError(f"Unknown term type: {type(term)}")

def reduce_steps(term, max_steps=200):
    steps = [term]
    current = term
    for _ in range(max_steps):
        next_term, reduced = step(current)
        if not reduced:
            break
        steps.append(next_term)
        current = next_term
    return steps

def pretty(term):
    if isinstance(term, Var):
        return term.name
    elif isinstance(term, Abs):
        return f"λ{term.param}.{pretty(term.body)}"
    elif isinstance(term, App):
        f_str = pretty(term.func)
        if isinstance(term.func, Abs):
            f_str = f"({f_str})"
            
        a_str = pretty(term.arg)
        if isinstance(term.arg, (Abs, App)):
            a_str = f"({a_str})"
            
        return f"{f_str} {a_str}"
    raise TypeError(f"Unknown term type: {type(term)}")

def tokenize(chars):
    return re.findall(r'[()λ\.\\]|[a-zA-Z0-9_\']+|\S', chars)

def parse(source, macros=None):
    if macros is None:
        macros = {}
    tokens = tokenize(source)
    pos = 0

    def peek():
        return tokens[pos] if pos < len(tokens) else None

    def consume():
        nonlocal pos
        t = tokens[pos]
        pos += 1
        return t

    def parse_term():
        term = parse_atom()
        while peek() is not None and peek() not in (')', '.'):
            term = App(term, parse_atom())
        return term

    def parse_atom():
        t = peek()
        if t == '(':
            consume()
            term = parse_term()
            if peek() != ')':
                raise SyntaxError(f"Missing closing parenthesis, got {peek()}")
            consume()
            return term
        elif t in ('λ', '\\'):
            consume()
            params = []
            while peek() != '.':
                if peek() is None:
                    raise SyntaxError("Unexpected EOF while parsing abstraction parameters")
                params.append(consume())
            consume() 
            body = parse_term()
            
            for p in reversed(params):
                body = Abs(p, body)
            return body
        else:
            name = consume()
            if name in macros:
                return macros[name]
            return Var(name)

    term = parse_term()
    if pos < len(tokens):
        raise SyntaxError(f"Unexpected trailing token: {peek()}")
    return term

MACROS = {}
macro_definitions = {
    'TRUE': r'\x y. x',
    'FALSE': r'\x y. y',
    'AND': r'\p q. p q p',
    'ZERO': r'\f x. x',
    'ONE': r'\f x. f x',
    'TWO': r'\f x. f (f x)',
    'THREE': r'\f x. f (f (f x))',
    'SUCC': r'\n f x. f (n f x)',
    'PLUS': r'\m n f x. m f (n f x)',
    'OMEGA': r'(\x. x x) (\x. x x)'
}

for name, source in macro_definitions.items():
    MACROS[name] = parse(source, MACROS)

def run_example(source, label, max_steps=200):
    print(f"\n--- Example: {label} ---")
    print(f"Source: {source}")
    term = parse(source, MACROS)
    
    steps = reduce_steps(term, max_steps=max_steps)
    total = len(steps)
    
    for i, t in enumerate(steps):
        if total > 20 and 5 < i < total - 5:
            if i == 6:
                print("... (intermediate steps omitted) ...")
            continue
        print(f"Step {i:2d}: {pretty(t)}")

    if total >= max_steps:
        print(f"Result: Did not terminate (hit cap of {max_steps} steps)")
    else:
        print(f"Result: {pretty(steps[-1])}")

def run_self_checks():
    print("\n--- Running Self-Checks ---")
    
    orig = Abs('y', Var('x'))
    replaced = subst(orig, 'x', Var('y'))
    
    assert isinstance(replaced, Abs), "Expected Abstraction"
    assert replaced.param != 'y', "Variable capture occurred! 'y' was not alpha-renamed."
    assert isinstance(replaced.body, Var) and replaced.body.name == replaced.param, "Substitution failed inside the renamed body."
    
    print(f"Capture avoidance check passed: (λy. x)[x := y] -> {pretty(replaced)}")
    print("All self-checks passed successfully.")

if __name__ == '__main__':
    run_example(r'(\x.x) y', "Simple application")
    run_example(r'AND TRUE FALSE', "Boolean AND (True, False)")
    run_example(r'AND TRUE TRUE', "Boolean AND (True, True)")
    run_example(r'SUCC ONE', "Church numeral successor (1 -> 2)")
    run_example(r'PLUS TWO THREE', "Church numeral addition (2 + 3 -> 5)")
    run_example(r'OMEGA', "Divergent combinator (OMEGA)", max_steps=20)
    
    run_self_checks()