import numpy as np

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

def apply_move(board, move, turn):
    new_state = [row[:] for row in board]
    new_state[move[0]][move[1]] = turn
    return new_state

    #Check if Terminal State
def check_win(board):
        #Check X
        # Check horizontal
    for row in range(3):
            if all(board[row][col] == 'X' for col in range(3)):
                return 1

        # Check vertical
    for col in range(3):
            if all(board[row][col] == 'X' for row in range(3)):
                return 1

        # Check diagonal
    if all(board[i][i] == 'X' for i in range(3)):
            return 1
    if all(board[i][2 - i] == 'X' for i in range(3)):
            return 1


        #Check O
        # Check horizontal
    for row in range(3):
            if all(board[row][col] == 'O' for col in range(3)):
                return -1

        # Check vertical
    for col in range(3):
            if all(board[row][col] == 'O' for row in range(3)):
                return -1

        # Check diagonal
    if all(board[i][i] == 'O' for i in range(3)):
            return -1
    if all(board[i][2 - i] == 'O' for i in range(3)):
            return -1




    return 0


    
def alpha_beta_pruning(board):
    best_val = np.inf
    alpha = -np.inf
    best_move = None
    print(get_available_moves(board))
    for move in get_available_moves(board):
        v = max_value(apply_move(board, move, 'O'), alpha, best_val)
        if v < best_val:
            best_val = v
            best_move = move
    return best_move

   
def max_value(board, alpha, beta):
    if check_win(board) != 0:
        return check_win(board)
    if not get_available_moves(board):
         return 0

    val = -np.inf

    for move in get_available_moves(board):
        val = max(val, min_value(apply_move(board, move, 'X'), alpha, beta))
        if val >= beta:
            return val
        alpha = max(alpha,val)

    return val


def min_value(board, alpha, beta):
    if check_win(board) != 0:
        return check_win(board)
    if not get_available_moves(board):
         return 0
    val = np.inf
    for move in get_available_moves(board):
        val = min(val, max_value(apply_move(board, move, 'O'), alpha, beta))
        if val <= alpha:
            return val
        beta = min(beta,val)

    return val



if __name__ == '__main__':
    board = create_board()
    print_board(board)
    board = create_board()
while(check_win(board) == 0):

       row = int(input("Row for input 1-3")) - 1
       column = int(input("Column for input 1-3")) - 1
       move = [row,column]
       board = apply_move(board,move,'X')
       print_board(board)
       bot_move =  alpha_beta_pruning(board)
       board = apply_move(board,bot_move,'O')
       print_board(board)
won = 'X' if check_win(board) == 1 else 'O'