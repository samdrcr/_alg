# 5_ic_routing.py
from collections import deque

def lee_routing(grid, pin_A, pin_B):
    rows, cols = len(grid), len(grid[0])
    queue = deque([pin_A])
    parent = {pin_A: None}
    
    found = False
    while queue and not found:
        curr = queue.popleft()
        if curr == pin_B:
            found = True
            break
            
        r, c = curr
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if (grid[nr][nc] == 0 or (nr, nc) == pin_B) and (nr, nc) not in parent:
                    parent[(nr, nc)] = curr
                    queue.append((nr, nc))
                    
    if not found: return None
    
    path = []
    curr = pin_B
    while curr:
        path.append(curr)
        curr = parent[curr]
    return path[::-1]

if __name__ == "__main__":
    # 0=empty, 1=existing wire block
    layout = [
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    wire_path = lee_routing(layout, (0,0), (0,4))
    print(f"IC Routed Wire Path (Lee's Algorithm): {wire_path}")
