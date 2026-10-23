N = 8
board = [-1] * N

def safe(row, col):
    for previous_row in range(row):
        previous_col = board[previous_row]

        if previous_col == col:
            return False

        if abs(previous_col - col) == abs(previous_row - row):
            return False

    return True

def solve(row):
    if row == N:
        return True

    for col in range(N):
        if safe(row, col):
            board[row] = col

            if solve(row + 1):
                return True

            board[row] = -1

    return False

if solve(0):
    print("Solution to 8-Queens Problem:")
    for row in range(N):
        print(" ".join(
            "Q" if board[row] == col else "."
            for col in range(N)
        ))
else:
    print("No solution found")