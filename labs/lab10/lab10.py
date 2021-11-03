'Justin Kerosetz'
'lab10.py'

def build():
    return list(range(1, 10))

def display(board):
    for i in range(3):
        n = i*3
        print(board[n],  " | ", board[n+1], " | ", board[n+2])
        print(10 * "-")

def place(board, pos, piece):
    if piece == "X" or piece == "O":
        board[pos - 1] = piece
    else:
        print("This is not a valid piece")

def legal(board, pos):
    if 1 <= pos <= 9 and board[pos - 1] == pos:
        return True
    else:
        return False

def isWon(board,piece):
    for i in range(3):
        n = i * 3
        if board[n] != piece:
            continue
        if board[n+1] != piece:
            continue
        if board[n+2] != piece:
            continue
        return True

    for i in range(3):
        if board[i] != piece:
            continue
        if board[i + 3] != piece:
            continue
        if board[i + 6] != piece:
            continue
        return True

    if board[0] == piece:
        if board[4] == piece:
            if board[8] == piece:
                return True
    if board[2] == piece:
        if board[4] == piece:
            if board[6] == piece:
                return True
    return False

def over(board):
    if isWon(board, "X"):
        return True
    elif isWon(board, "O"):
        return True
    else:
        for i in range(9):
            if board[i] == i + 1:
                return False
        return True

def play():
    board = build()
    while True:
        display(board)
        player = eval(input("X's turn.Enter a number 1 through 9: "))
        if legal(board, player):
            place(board, player, "X")
        if over(board):
            if isWon(board, "X"):
                print("X Wins!")
                break
            else:
                display(board)
                print("Its a tie")
                break
        display(board)
        player = eval(input("O's turn.Enter a number 1 through 9: "))
        if legal(board, player):
            place(board, player, "O")
        if over(board):
            if isWon(board, "O"):
                print("O Wins!")
                break
            else:
                print("Tie")
                break


def main():
    play()

main()