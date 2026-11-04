# 2_river_crossing_bfs.py
from collections import deque

def is_valid(state):
    f, w, g, c = state
    # Wolf eats goat if farmer is absent
    if w == g and f != w: return False
    # Goat eats cabbage if farmer is absent
    if g == c and f != g: return False
    return True

def get_successors(state):
    successors = []
    f, w, g, c = state
    new_f = 1 - f # Farmer always moves
    
    # Farmer moves alone
    successors.append((new_f, w, g, c))
    # Farmer takes wolf
    if f == w: successors.append((new_f, new_f, g, c))
    # Farmer takes goat
    if f == g: successors.append((new_f, w, new_f, c))
    # Farmer takes cabbage
    if f == c: successors.append((new_f, w, g, new_f))
    
    return [s for s in successors if is_valid(s)]

def solve_river():
    start = (0, 0, 0, 0)
    goal = (1, 1, 1, 1)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        current, path = queue.popleft()
        if current == goal: return path
        
        for nxt in get_successors(current):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))
    return []

if __name__ == "__main__":
    solution = solve_river()
    print(f"River Crossing Shortest Steps (BFS):")
    for step, state in enumerate(solution):
        print(f"Step {step}: {state}")
