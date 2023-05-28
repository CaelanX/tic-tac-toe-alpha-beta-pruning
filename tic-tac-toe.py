import numpy as np
#create the game board
def create_board():
        #define our 3 x 3 tic-tac-toe board
        rows, columns = 3,3
        board = [[0 for i in range(rows)] for j in range(columns)]

        for i in range(rows):
            for j in range(columns):
                board[i][j] = " "

        return board
#Print the game board
def print_board(board):
        print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
        print("_____")
        print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
        print("_____")
        print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])
#Get valid moves for the current position
def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append([i,j])
    return moves
#Apply a move and return the new board
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


#Alpha beta pruning algorithm    
def alpha_beta_pruning(board):
    best_val = np.inf
    alpha = -np.inf
    best_move = None
    for move in get_available_moves(board):
        if check_win(board) == -1:
            return move    
        v = max_value(apply_move(board, move, 'O'), alpha, best_val)
        if v < best_val:
            best_val = v
            best_move = move
    return best_move

#max fn for minimax   
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

#min fn for minimax
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
    #Create initial state
    board = create_board()
    print("Tic-Tac-Toe")
    print_board(board)

    while(check_win(board) == 0):
        
        row = int(input("Row for input 1-3? ")) - 1
        column = int(input("Column for input 1-3? ")) - 1
        move = [row,column]
        if move not in get_available_moves(board):
            print("Invalid position! Please choose another square.")
            continue
        board = apply_move(board,move,'X')
        #If game is a Tie will only happen on player turn
        if not get_available_moves(board):
             print("Tie")
             break
        print("Your Move")
        print_board(board)

        bot_move =  alpha_beta_pruning(board)
        board = apply_move(board,bot_move,'O')
        print("AIs Move")
        print_board(board)

    #Player cannot beat AI game will always result in a Tie or the AI winning
    print("AI Wins")