
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

line = "---+---+---"

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def display_board(board):
    print(line)
    for row in board:
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        print(line)
display_board(board)
current_player = "X"
while True:
    if check_winner(board):
        print(f"Player {current_player} wins!")
        break
    print(f"Player {current_player}'s turn")
    row = int(input("Enter row(0,2): "))
    col = int(input("Enter col:(0,2) "))
    
    if board[row][col] == " ":
        board[row][col] = current_player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
    else:
        print("Cell is already taken. Choose another.")
        continue
    display_board(board)