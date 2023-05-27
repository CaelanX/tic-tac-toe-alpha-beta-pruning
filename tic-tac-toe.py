import math
class Game:
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
    move = max_value(board, -math.inf, math.inf)
    return move

   
def max_value(board, alpha, beta):
    if check_win(board) == 1:
        return check_win(board), None
    max_val = -math.inf
    best_state = None

    for move in get_available_moves(board):
        move_state = apply_move(board, move, 'X')
        val = check_win(move_state)
        val, move_state = min_value(move_state, alpha, beta)
        if val > max_val:
            max_val, best_state = val, move_state
            alpha = max(alpha, max_val)
        if max_val >= beta:
            return max_val, best_state
    return max_val, best_state


def min_value(board, alpha, beta):
    if check_win(board) == -1:
        return check_win(board), board
    min_val = math.inf
    best_state = None

    for move in get_available_moves(board):
        move_state = apply_move(board, move, 'O')
        val = check_win(move_state)
        val, move_state = min_value(move_state, alpha, beta)
        if val < min_val:
            min_val, best_state = val, move_state
            beta = min(beta, min_val)
        if min_val <= alpha:
            return min_val, best_state
    return min_val, best_state



if __name__ == '__main__':
    board = create_board()
    print_board(board)
    board = create_board()
    while(check_win(board) == 0):
       
       row = int(input("Row for input 1-3")) - 1
       column = int(input("Column for input 1-3")) - 1
       move = [row,column]
       board = apply_move(board,move,'O')
       print_board(board)
       board =  alpha_beta_pruning(board)
       print_board(board)

    won = 'X' if check_win(board) == 1 else 'O'