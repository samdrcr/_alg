def hanoi_recursive(n, source, target, aux):
    if n > 0:
        hanoi_recursive(n - 1, source, aux, target)
        print(f"Move disk {n} from {source} to {target}")
        hanoi_recursive(n - 1, aux, target, source)

def hanoi_iterative(n, source, target, aux):
    stack = [('call', n, source, target, aux)]
    
    while stack:
        action, num, src, tgt, mid = stack.pop()
        
        if action == 'move':
            print(f"Move disk {num} from {src} to {tgt}")
        elif num > 0:
            stack.append(('call', num - 1, mid, tgt, src))
            stack.append(('move', num, src, tgt, mid))
            stack.append(('call', num - 1, src, mid, tgt))