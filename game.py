import random
import tkinter as tk

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

    num_empty_cells = len(empty_cells)
    if num_empty_cells > 0:
        num_tiles_to_generate = min(random.randint(1, 2), num_empty_cells)
        chosen_cells = random.sample(empty_cells, num_tiles_to_generate)
        for row, col in chosen_cells:
            board[row][col] = random.choice([2, 4])

def check_game_over():
    for i in range(4):
        for j in range(4):
            if board[i][j] == 2048:
                game_status_label.config(text="You Win! Yey!", fg="green", font=("Verdana", 14, "bold"))
                return True

            if board[i][j] == 0:
                return False

            if i < 3 and board[i][j] == board[i + 1][j]:
                return False

            if j < 3 and board[i][j] == board[i][j + 1]:
                return False
    game_status_label.config(text="You Lose!", fg="red", font=("Verdana", 14, "bold"))
    return True

def update_tile_colors():
    for i in range(4):
        for j in range(4):
            cell_value = board[i][j]
            cell_text = str(cell_value) if cell_value != 0 else ""
            tiles[i][j].configure(text=cell_text, bg=tile_colors.get(cell_value, "#CDC1B4"))

def restart_game():
    global board
    board = initialize_board()
    update_board()

def update_personal_best(current_score):
    global personal_best
    personal_best = max(personal_best, current_score)
    personal_best_label.config(text=f"Personal Best: {personal_best}")

def update_board():
    for i in range(4):
        for j in range(4):
            cell_value = board[i][j]
            cell_text = str(cell_value) if cell_value != 0 else ""
            tiles[i][j].configure(text=cell_text, bg=tile_colors.get(cell_value, "#CDC1B4"))

def get_current_score():
    return max(max(row) for row in board)

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
    add_new_tile(board)
    update_board()
    update_personal_best(get_current_score())

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
    add_new_tile(board)
    update_board()
    update_personal_best(get_current_score())

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
    add_new_tile(board)
    update_board()
    update_personal_best(get_current_score())

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
    add_new_tile(board)
    update_board()
    update_personal_best(get_current_score())

def restart_game():
    global board, game_status_label
    board = initialize_board()
    update_tile_colors()
    game_status_label.config(text="", fg="black")

def handle_key(event):
    global board
    prev_board = [row[:] for row in board]
    if event.keysym == 'a':
        move_left(board)
    elif event.keysym == 'd':
        move_right(board)
    elif event.keysym == 'w':
        move_up(board)
    elif event.keysym == 's':
        move_down(board)
    if board != prev_board:
        update_tile_colors()
        if check_game_over():
            update_personal_best(get_current_score())

root = tk.Tk()
root.title("2048 Game")

tile_colors = {
    0: "#CDC1B4",
    2: "#EEE4DA",
    4: "#EDE0C8",
    8: "#F2B179",
    16: "#F59563",
    32: "#F67C5F",
    64: "#F65E3B",
    128: "#EDCF72",
    256: "#EDCC61",
    512: "#EDC850",
    1024: "#EDC53F",
    2048: "#EDC22E",
}

board = initialize_board()
tiles = [[None]*4 for _ in range(4)]

for i in range(4):
    for j in range(4):
        cell_value = board[i][j]
        cell_text = str(cell_value) if cell_value != 0 else ""
        tile = tk.Label(root, text=cell_text, font=("Verdana", 20, "bold"), width=4, height=2,
                        relief="raised", borderwidth=4)
        tile.grid(row=i, column=j, padx=5, pady=5)
        tiles[i][j] = tile
        tile.configure(bg=tile_colors.get(cell_value, "#CDC1B4"))

restart_button = tk.Button(root, text="Restart", command=restart_game)
restart_button.grid(row=4, columnspan=4)

personal_best = 0
personal_best_label = tk.Label(root, text=f"Personal Best: {personal_best}", font=("Verdana", 12))
personal_best_label.grid(row=5, columnspan=4)

def check_game_status():
    if check_game_over():
        game_status_label.config(text="Game Over! You Lose.", fg="red", font=("Verdana", 14, "bold"))

game_status_label = tk.Label(root, text="", font=("Verdana", 14))
game_status_label.grid(row=6, columnspan=4)

def update_game_status():
    check_game_status()

root.bind("<Key>", lambda event: [handle_key(event), update_game_status()])
root.mainloop()