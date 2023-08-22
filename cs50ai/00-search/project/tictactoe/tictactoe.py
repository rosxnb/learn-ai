"""
Tic Tac Toe Player
"""

X = "X"
O = "O"
EMPTY = None

from copy import deepcopy

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    return X if x_count < o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, col = action
    if board[row][col] != EMPTY:
        raise Exception("Invalid move")

    new_board = deepcopy(board)
    new_board[row][col] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    res = utility(board)
    if res == -1:
        return O
    elif res == 1:
        return X
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    for row in board:
        if (row[0] != EMPTY and row.count(row[0]) == 3):
            return 1 if row[0] == X else -1

    # check every column
    if (board[0][0] != EMPTY and board[0][0] == board[1][0] and board[1][0] == board[2][0]):
        return 1 if board[0][0] == X else -1
    if (board[0][1] != EMPTY and board[0][1] == board[1][1] and board[1][1] == board[2][1]):
        return 1 if board[0][1] == X else -1
    if (board[0][2] != EMPTY and board[0][2] == board[1][2] and board[1][2] == board[2][2]):
        return 1 if board[0][2] == X else -1

    # check diagonals
    if (board[0][0] != EMPTY and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return 1 if board[1][1] == X else -1
    if (board[0][2] != EMPTY and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return 1 if board[1][1] == X else -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(board):
        play = ()
        if terminal(board):
            return utility(board), play
        else:
            v = -2
            for action in actions(board):
                min_val = min_value(result(board, action))[0]
                if min_val > v:
                    v = min_val
                    play = action
            return v, play

    def min_value(board):
        play = ()
        if terminal(board):
            return utility(board), play
        else:
            v = 2
            for action in actions(board):
                max_val = max_value(result(board, action))[0]
                if max_val < v:
                    v = max_val
                    play = action
            return v, play

    curr_player = player(board)

    if terminal(board):
        return None

    if curr_player == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]
