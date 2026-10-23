def display(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("--+---+--")

def check_winner(board, player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(
        all(board[i] == player for i in line)
        for line in wins
    )

board = [str(i) for i in range(1, 10)]
player = "X"

while True:
    display(board)
    move = input(f"Player {player}, enter position (1-9): ")

    if not move.isdigit() or not 1 <= int(move) <= 9:
        print("Invalid position")
        continue

    index = int(move) - 1

    if board[index] in ("X", "O"):
        print("Position already occupied")
        continue

    board[index] = player

    if check_winner(board, player):
        display(board)
        print("Player", player, "wins!")
        break

    if all(cell in ("X", "O") for cell in board):
        display(board)
        print("Game Draw!")
        break

    player = "O" if player == "X" else "X"
    