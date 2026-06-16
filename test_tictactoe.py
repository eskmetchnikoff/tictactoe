import pytest
from tictactoe import is_full, check_winner, computer_move

# ===========================================================================
# Helpers
# ===========================================================================


def empty_board():
    return [[" "] * 3 for _ in range(3)]


def full_board():
    return [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["O", "X", "O"],
    ]


def diagonal_board(player, is_left):
    assert player in ('X', 'O')
    if is_left:
        return [
            [player, " ", " "],
            [" ", player, " "],
            [" ", " ", player],
        ]
    else:
        return [
            [" ", " ", player],
            [" ", player, " "],
            [player, " ", " "],
        ]


# ===========================================================================
# is_full
# ===========================================================================

# --- Obvious cases ---


def test_empty_board_is_not_full():
    assert is_full(empty_board()) == False


def test_full_board_is_full():
    assert is_full(full_board()) == True


# --- Boundary cases ---


def test_one_empty_cell_is_not_full():
    board = full_board()
    board[2][2] = " "
    assert is_full(board) == False


def test_one_filled_cell_is_not_full():
    board = empty_board()
    board[0][0] = "X"
    assert is_full(board) == False


def test_half_full_board_is_not_full():
    board = [["X", "O", "X"], ["O", " ", " "], [" ", " ", " "]]
    assert is_full(board) == False


# --- Adversarial / malformed inputs ---


def test_empty_string_cell_is_treated_as_filled():
    # "" != " " is True, so is_full considers empty strings as occupied
    board = full_board()
    board[1][1] = ""
    assert is_full(board) == True


def test_none_cell_is_treated_as_filled():
    # None != " " is True, same surprising behavior as empty string
    board = full_board()
    board[1][1] = None
    assert is_full(board) == True


def test_board_too_small_raises():
    board = [["X", "O"], ["O", "X"]]
    with pytest.raises(IndexError):
        is_full(board)


# ===========================================================================
# check_winner
# ===========================================================================


# --- Your tests go here ---
#   - No winner — empty board
def test_no_winner_on_empty_board():
    assert check_winner(empty_board(), "X") == False
    assert check_winner(empty_board(), "O") == False


#   - Row wins — top row, middle row, bottom row
def test_row_wins():
    for i in range(3):
        board = empty_board()
        board[i] = ["X"] * 3
        assert check_winner(board, "X") == True
        assert check_winner(board, "O") == False


#   - Column wins — left, middle, right column
def test_column_wins():
    for i in range(3):
        board = empty_board()
        for row in range(3):
            board[row][i] = "X"
        assert check_winner(board, "X") == True
        assert check_winner(board, "O") == False


#   - Diagonal wins — both diagonals
def test_diagonal_wins():
    for player in ('X', 'O'):
        competitor = 'O' if (player == 'X') else 'X'
        for is_left in (True, False):
            board = diagonal_board(player, is_left)
            assert check_winner(board, player) == True
            assert check_winner(board, competitor) == False

#   - an impossible board (e.g. row of Xs and row of Ys simultaneously) shouldn't
#     report a winner for either player
def test_dual_win_raises():
    board = [
        ['X', 'X', 'X'],
        ['O', 'O', 'O'],
        [' ', ' ', ' '],
    ]
    with pytest.raises(ValueError):
        check_winner(board, 'X')
# ===========================================================================
# computer_move
# ===========================================================================

# with an empty board, the computer picks ANY valid coordinate (on the board)
def test_computer_move_empty_board():
    board = empty_board()
    row, col = computer_move(board)
    assert 0 <= row <= 2
    assert 0 <= col <= 2

# with a full board, the computer refuses to pick
def test_computer_move_full_board():
    board = full_board()
    with pytest.raises(ValueError):
        row, col = computer_move(board)
# with a board that only has one free space, the computer must pick that space only


#   -----------
#   - Below here are placeholders for test ideas Sam came up with that weren't
#     already suggested by Claude. We will get to them later.
#   - Adversarial: garbage in cells shouldn't cause false positives
#     - garbage players (S, Q, None) can't win on an otherwise empty board

