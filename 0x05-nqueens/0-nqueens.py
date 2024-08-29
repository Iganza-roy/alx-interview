#!/usr/bin/python3
def is_safe(board, row, col):
    """Checks if placing a queen at (row, col) is safe."""
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - i) == abs(col - row):
            return False
    return True

def solve_nqueens(N):
    """Solves the N-Queens problem."""
    def backtrack(row, board):
        if row == N:
            print(board)
        else:
            for col in range(N):
                if is_safe(board, row, col):
                    board[row] = col
                    backtrack(row + 1, board)
                    board[row] = -1

    board = [-1] * N
    backtrack(0, board)

if __name__ == "__main__":
    N = int(input("Enter the board size (N): "))
    if N < 4:
        print("N must be at least 4")
    else:
        solve_nqueens(N)