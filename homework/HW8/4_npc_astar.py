# 4_npc_astar.py
import heapq

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    pq = [(0, start, [start])]
    visited = set()
    g_score = {start: 0}

    while pq:
        f, current, path = heapq.heappop(pq)
        
        if current in visited: continue
        visited.add(current)
        
        if current == goal: return path
        
        r, c = current
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                nxt = (nr, nc)
                new_g = g_score[current] + 1
                
                if nxt not in g_score or new_g < g_score[nxt]:
                    g_score[nxt] = new_g
                    f_score = new_g + heuristic(nxt, goal)
                    heapq.heappush(pq, (f_score, nxt, path + [nxt]))
    return []

if __name__ == "__main__":
    # 0 = open, 1 = obstacle
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    path = astar_search(grid, (0,0), (4,4))
    print(f"NPC A* Path: {path}")
