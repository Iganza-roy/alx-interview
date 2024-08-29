#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    def backtrack(row, board):
        if row == N:
            print([[i, board[i]] for i in range(N)])
        else:
            for col in range(N):
                if is_safe(board, row, col, N):
                    board[row] = col
                    backtrack(row + 1, board)

    board = [-1] * N
    backtrack(0, board)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solve_nqueens(N)
