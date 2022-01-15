'''
W02 Prove: Developer - Solo Code Submission
Tic-Tac-Toe
Author: Filipi Santos
'''
def main():
    print('WELCOME TO THE BEST TIC-TAC-TOE GAME EVER')
    gamer1 = input('What is the name of the gamer 1? ')
    gamer2 = input('What is the name of the gamer 2? ')
    print(f"{gamer1} and {gamer2} let's begin!!!")
    gamer = ""
    board = []
    while winning(board) == False and draw(board) == False:
        drawing_board(board)
        moving(gamer,board)
        gamer = play(gamer)
    drawing_board(board)
    print('Great! I hope you have enjoyed the game!')


def board():
    board = []
    for place in range(9):
        board.append(place + 1)
    return board

def drawing_board(board):
    print()
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('---------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('---------')
    print(f'{board[6]} | {board[7]} | {board[8]}')
    print()

def winning(board):
    if (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6]):
        return True
    else:
        return False

def draw(board):
    for place in range(9):
        if board[place] == 'x' or board[place] == 'o':
            return True
    return False

def moving(player,board):
    square = int(input(f"{player} turn to choose a square (1-9): "))
    board[square - 1] = player

def play(your_time,gamer1,gamer2):
    if your_time == "" or your_time == {gamer1}:
        return {gamer2}
    elif your_time == {gamer2}:
        return {gamer1}

if __name__ == "__main__":
    main()