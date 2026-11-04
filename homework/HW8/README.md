# Search Algorithms Assignment

## Project Overview

This repository contains Python implementations of five classic search algorithms applied to various logical and grid-based problems. The primary objective of this project is to demonstrate how different problem spaces require specific traversal strategies to find optimal or valid solutions efficiently. The implementations cover Depth-First Search (DFS), Breadth-First Search (BFS), Backtracking, and A\* Heuristic Search.

## Problem 1: Mouse in a Maze (DFS)

- **Algorithm**: Depth-First Search (DFS)
- **State Representation**: Grid coordinates `(row, col)`.
- **Data Structure**: Call stack (via Recursion) and a `Set` to track visited nodes.
- **Explanation**: DFS naturally models exploring a physical maze. The algorithm ventures as deep as possible down a single path until it hits a wall or the goal. If a dead end is reached, it uses backtracking to return to the last intersection and tries an alternative route. The visited set prevents the mouse from walking in infinite loops.
- **Time Complexity**: O(V + E), where V is the number of empty cells and E is the number of valid moves between them.
- **Space Complexity**: O(V) for the visited set and the recursion stack in the worst-case scenario.

## Problem 2: Wolf, Goat, and Cabbage River Crossing (BFS)

- **Algorithm**: Breadth-First Search (BFS)
- **State Representation**: A four-element tuple `(Farmer, Wolf, Goat, Cabbage)` where `0` represents the left bank and `1` represents the right bank.
- **Data Structure**: `Queue` (using `collections.deque`) and a `Set` for visited states.
- **Explanation**: BFS is chosen because it explores all possible game states layer by layer, guaranteeing that the first discovered solution requires the minimum number of boat trips (the shortest path). During successor generation, the algorithm prunes invalid states where predators are left alone with their prey without the farmer's supervision.
- **Time Complexity**: O(V + E). Since there are only 2^4 = 16 possible states, it runs in O(1) constant time effectively.
- **Space Complexity**: O(1) for storing at most 16 states in the queue and visited set.

## Problem 3: 8-Queens Problem (DFS / Backtracking)

- **Algorithm**: Backtracking (Constraint Satisfaction Problem formulation)
- **State Representation**: A 1D array `board` of size 8, where the index `i` represents the row and the value `board[i]` stores the column position of the queen.
- **Data Structure**: Call stack (Recursion) and a 1D Array.
- **Explanation**: The algorithm places queens row by row. Before placing a queen, it checks for column and diagonal conflicts with all previously placed queens. If a conflict is detected, the algorithm prunes that branch and backtracks. This aggressive pruning reduces the search space drastically compared to a brute-force approach.
- **Time Complexity**: O(N!), where N is the number of queens (8).
- **Space Complexity**: O(N) for the recursion stack and the board array.

## Problem 4: NPC Pathfinding (A\* Search)

- **Algorithm**: A\* Search
- **State Representation**: Grid coordinates `(row, col)`.
- **Data Structure**: `Min-Heap` (Priority Queue using Python's `heapq`), a `Set` for visited nodes, and a `Dictionary` for tracking `g_score`.
- **Explanation**: A* balances the exact cost of the path traveled so far `g(n)` with a heuristic estimate of the remaining cost to the goal `h(n)`. Because the NPC moves in a 4-way grid (up, down, left, right), the **Manhattan Distance** is used as the heuristic. It is admissible (never overestimates the cost), ensuring A* finds the optimal shortest path while expanding significantly fewer nodes than a standard BFS.
- **Time Complexity**: O(E), but practically much faster than BFS due to heuristic pruning.
- **Space Complexity**: O(V) for the priority queue and cost dictionaries.

## Problem 5: IC Circuit Routing (Lee's Algorithm)

- **Algorithm**: Lee's Algorithm (Grid-based BFS)
- **State Representation**: Grid coordinates `(row, col)` representing the circuit board layout.
- **Data Structure**: `Queue` for wave propagation and a `Dictionary` for tracking parent nodes to reconstruct the path.
- **Explanation**: In Electronic Design Automation (EDA), Lee's algorithm is standard for single-net routing. It propagates a wave outward from the source pin, exploring equally in all directions while avoiding obstacles (previously routed wires). Once the target pin is reached, the algorithm traces back through the parent pointers to establish the final wire route.
- **Time Complexity**: O(V + E), where V is the total number of grid cells on the layout.
- **Space Complexity**: O(V) for the queue and the parent mapping.

## Example Console Outputs

### 1. Mouse Maze (DFS)

```text
Mouse Maze Path (DFS): [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
```

### 2. River Crossing (BFS)

```text
River Crossing Shortest Steps (BFS):
Step 0: (0, 0, 0, 0)
Step 1: (1, 0, 1, 0)
Step 2: (0, 0, 1, 0)
Step 3: (1, 1, 1, 0)
Step 4: (0, 1, 0, 0)
Step 5: (1, 1, 0, 1)
Step 6: (0, 1, 0, 1)
Step 7: (1, 1, 1, 1)
```

### 3. 8-Queens (DFS)

```text
Total 8-Queens solutions found: 92
First solution (Index=Row, Value=Col): [0, 4, 7, 5, 2, 6, 1, 3]
```

### 4. NPC Pathfinding (A\*)

```text
NPC A* Path: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
```

### 5. IC Circuit Routing (Lee's)

```text
IC Routed Wire Path (Lee's Algorithm): [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (1, 4), (0, 4)]
```

## Setup and Execution

### Requirements

- Python 3.6 or higher.
- No external third-party libraries (e.g., NumPy) are required; all scripts use built-in Python standard libraries.

### Running the Scripts

Navigate to the project directory in your terminal and execute each script individually:

```bash
# 1. Run the Mouse Maze DFS solver
python3 1_mouse_maze_dfs.py

# 2. Run the River Crossing BFS solver
python3 2_river_crossing_bfs.py

# 3. Run the 8-Queens solver
python3 3_eight_queens_dfs.py

# 4. Run the NPC A* Pathfinding solver
python3 4_npc_astar.py

# 5. Run the IC Circuit Routing solver
python3 5_ic_routing.py
```
