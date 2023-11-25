import random

def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                empty_cells.append((i, j))
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = random.choice([2, 4])

def print_board(board):
    for row in board:
        print(row)

def move_left(board):
    for i in range(4):
        merged = [False] * 4
        for j in range(1, 4):
            if board[i][j] != 0:
                k = j
                while k > 0 and board[i][k - 1] == 0:
                    board[i][k - 1] = board[i][k]
                    board[i][k] = 0
                    k -= 1
                if k > 0 and board[i][k - 1] == board[i][k] and not merged[k - 1]:
                    board[i][k - 1] *= 2
                    board[i][k] = 0
                    merged[k - 1] = True

def move_right(board):
    for i in range(4):
        merged = [False] * 4
        for j in range(2, -1, -1):
            if board[i][j] != 0:
                k = j
                while k < 3 and board[i][k + 1] == 0:
                    board[i][k + 1] = board[i][k]
                    board[i][k] = 0
                    k += 1
                if k < 3 and board[i][k + 1] == board[i][k] and not merged[k + 1]:
                    board[i][k + 1] *= 2
                    board[i][k] = 0
                    merged[k + 1] = True

def move_up(board):
    for j in range(4):
        merged = [False] * 4
        for i in range(1, 4):
            if board[i][j] != 0:
                k = i
                while k > 0 and board[k - 1][j] == 0:
                    board[k - 1][j] = board[k][j]
                    board[k][j] = 0
                    k -= 1
                if k > 0 and board[k - 1][j] == board[k][j] and not merged[k - 1]:
                    board[k - 1][j] *= 2
                    board[k][j] = 0
                    merged[k - 1] = True

def move_down(board):
    for j in range(4):
        merged = [False] * 4
        for i in range(2, -1, -1):
            if board[i][j] != 0:
                k = i
                while k < 3 and board[k + 1][j] == 0:
                    board[k + 1][j] = board[k][j]
                    board[k][j] = 0
                    k += 1
                if k < 3 and board[k + 1][j] == board[k][j] and not merged[k + 1]:
                    board[k + 1][j] *= 2
                    board[k][j] = 0
                    merged[k + 1] = True

def is_game_over(board):
    for row in board:
        if 2048 in row:
            return True
    return False

def play_game():
    board = initialize_board()
    while True:
        print_board(board)
        move = input("Enter move (left, right, up, down): ")
        if move == "left":
            move_left(board)
        elif move == "right":
            move_right(board)
        elif move == "up":
            move_up(board)
        elif move == "down":
            move_down(board)
        else:
            print("Invalid move. Please try again.")
            continue
        add_new_tile(board)
        if is_game_over(board):
            print("Congratulations! You won!")
            break

play_game()
