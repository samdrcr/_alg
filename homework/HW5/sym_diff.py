def sym_diff(expr, var='x'):
    if isinstance(expr, (int, float)):
        return 0
    if isinstance(expr, str):
        return 1 if expr == var else 0
    
    op, left, right = expr
    
    if op == '+':
        return ('+', sym_diff(left, var), sym_diff(right, var))
    elif op == '-':
        return ('-', sym_diff(left, var), sym_diff(right, var))
    elif op == '*':
        return ('+', 
                ('*', sym_diff(left, var), right), 
                ('*', left, sym_diff(right, var)))
    elif op == '/':
        return ('/', 
                ('-', ('*', sym_diff(left, var), right), ('*', left, sym_diff(right, var))), 
                ('*', right, right))
    else:
        raise ValueError(f"Unsupported operator: {op}")