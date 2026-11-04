# 3_eight_queens_dfs.py
def solve_n_queens(n=8):
    solutions = []
    board = [-1] * n # board[i] = column index of queen in row i

    def is_safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(list(board))
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)

    backtrack(0)
    return solutions

if __name__ == "__main__":
    sols = solve_n_queens(8)
    print(f"Total 8-Queens solutions found: {len(sols)}")
    print(f"First solution (Index=Row, Value=Col): {sols[0]}")
