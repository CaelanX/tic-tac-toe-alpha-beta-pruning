class Node:
    def __init__(self, state, actions):
        self.STATE = state
        self.actions = actions

def create_board():
    #define our 3 x 3 tic-tac-toe board
    rows, columns = 3,3
    board = [[0 for i in range(rows)] for j in range(columns)]

    for i in range(rows):
        for j in range(columns):
            board[i][j] = " "

    return board

def print_board(board):
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print("_____")
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print("_____")
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])

def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append([i,j])
    return moves
        


if __name__ == '__main__':
    print_board(create_board())
