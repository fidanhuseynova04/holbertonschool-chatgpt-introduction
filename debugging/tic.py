#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not (check_winner(board) or check_draw(board)):
        print_board(board)
        row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
        col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == " ":
                board[row][col] = player
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")
        else:
            print("Invalid input! Row and column must be in range 0 to 2.")

    print_board(board)
    if check_winner(board):
        if player == "X":
            winner = "O"
        else:
            winner = "X"
        print("Player " + winner + " wins!")
    else:
        print("It's a draw!")

tic_tac_toe()
