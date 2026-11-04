# 1_mouse_maze_dfs.py
def solve_maze(maze, start, end):
    path = []
    rows, cols = len(maze), len(maze[0])
    visited = set()

    def dfs(r, c):
        if (r, c) == end:
            path.append((r, c))
            return True
        
        if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0 and (r, c) not in visited:
            visited.add((r, c))
            path.append((r, c))
            
            # Explore neighbors: Down, Right, Up, Left
            if dfs(r+1, c) or dfs(r, c+1) or dfs(r-1, c) or dfs(r, c-1):
                return True
            
            path.pop() # Backtrack
        return False

    dfs(start[0], start[1])
    return path

if __name__ == "__main__":
    # 0 = path, 1 = wall
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    path = solve_maze(maze, (0,0), (4,4))
    print(f"Mouse Maze Path (DFS): {path}")
