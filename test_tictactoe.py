import pytest
from tictactoe import is_full


# --- Helpers ---

def empty_board():
    return [[" "] * 3 for _ in range(3)]

def full_board():
    return [["X", "O", "X"],
            ["O", "X", "O"],
            ["O", "X", "O"]]


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
    board = [["X", "O", "X"],
             ["O", " ", " "],
             [" ", " ", " "]]
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
    board = [["X", "O"],
             ["O", "X"]]
    with pytest.raises(IndexError):
        is_full(board)
