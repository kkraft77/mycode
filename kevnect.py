#!/usr/bin/env python3
board = [[' ' for j in range(7)] for i in range(6)]

# function for the state of my board
def print_board(board):
    for row in board:
        print('|'.join(row))

# function "Has the player won the game horizontally / vertically / diagonally
def check_win(board, player):
    # Check horizontal wins
    for row in board:
        for j in range(4):
            if row[j] == player and row[j+1] == player and row[j+2] == player and row[j+3] == player:
                return True
    # Check vertical wins
    for j in range(7):
        for i in range(3):
            if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
                return True
    # Check diagonal wins 
    for i in range(3):
        for j in range(4):
            if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                return True
    # Check diagonal wins
    for i in range(3):
        for j in range(3, 7):
            if board[i][j] == player and board[i+1][j-1] == player and board[i+2][j-2] == player and board[i+3][j-3] == player:
                return True
    return False

# Function for making moves
def make_move(board, player, column):
    for i in range(5, -1, -1):
        if board[i][column] == ' ':
            board[i][column] = player
            return

# main game loop defined
def play_game():
    print("Let's play Connect Four!")
    print_board(board)
    player = 'X'
    while True:
        column = int(input("Player " + player + ", choose a column (0-6): "))
        make_move(board, player, column)
        print_board(board)
        if check_win(board, player):
            print("WOW! Player "  + player + " has won SUCKA!")
            break
        if player == 'X':
            player = 'O'
        else:
            player = 'X'

# Fire off the game
play_game()
