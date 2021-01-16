import pytest
from typing import List
from ..sudokucli.sudoku import Sudoku

@pytest.fixture
def sudoku_class():
    sudoku = Sudoku()
    return sudoku

@pytest.fixture
def sudoku_empty_board():
    return [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

@pytest.fixture
def sudoku_edited_board():
    return [[9,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

@pytest.fixture
def sudoku_easy_unsolved_board():
    return [[0,2,7,0,3,8,1,0,0],
            [1,0,4,0,0,2,0,8,0],
            [0,0,0,7,0,0,4,9,0],
            [8,7,0,0,0,0,0,0,0],
            [0,0,0,0,4,0,0,0,0],
            [0,0,0,0,0,0,0,1,8],
            [0,3,1,0,0,5,0,0,0],
            [0,4,0,2,0,0,9,0,7],
            [0,0,9,3,8,0,2,0,0]]

@pytest.fixture
def sudoku_easy_solved_board():
    return [[9,2,7,4,3,8,1,6,5],
            [1,5,4,6,9,2,7,8,3],
            [3,8,6,7,5,1,4,9,2],
            [8,7,5,1,6,9,3,2,4],
            [6,1,2,8,4,3,5,7,9],
            [4,9,3,5,2,7,6,1,8],
            [2,3,1,9,7,5,8,4,6],
            [5,4,8,2,1,6,9,3,7],
            [7,6,9,3,8,4,2,5,1]]

@pytest.fixture
def sudoku_easy_absolved_board():
    return [[1,1,1,1,1,1,1,1,1],
            [1,1,1,6,9,2,7,8,3],
            [1,1,1,7,5,1,4,9,2],
            [1,7,5,1,6,9,3,2,4],
            [1,1,2,8,4,3,5,7,9],
            [1,9,3,5,2,7,6,1,8],
            [1,3,1,9,7,5,8,4,6],
            [1,4,8,2,1,6,9,3,7],
            [1,6,9,3,8,4,2,5,1]]

@pytest.fixture
def sudoku_correct_row_board():
    return [[1,2,3,4,5,6,7,8,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

@pytest.fixture
def sudoku_incorrect_row_board():
    return [[1,2,3,1,5,9,7,8,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

@pytest.fixture
def sudoku_correct_col_board():
    return [[1,0,0,0,0,0,0,0,0],
            [2,0,0,0,0,0,0,0,0],
            [3,0,0,0,0,0,0,0,0],
            [4,0,0,0,0,0,0,0,0],
            [5,0,0,0,0,0,0,0,0],
            [6,0,0,0,0,0,0,0,0],
            [7,0,0,0,0,0,0,0,0],
            [8,0,0,0,0,0,0,0,0],
            [9,0,0,0,0,0,0,0,0]]

@pytest.fixture
def sudoku_incorrect_col_board():
    return [[1,0,0,0,0,0,0,0,0],
            [2,0,0,0,0,0,0,0,0],
            [3,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0],
            [5,0,0,0,0,0,0,0,0],
            [9,0,0,0,0,0,0,0,0],
            [7,0,0,0,0,0,0,0,0],
            [8,0,0,0,0,0,0,0,0],
            [9,0,0,0,0,0,0,0,0]]

@pytest.fixture
def sudoku_correct_box_board():
    return [[1,2,3,0,0,0,0,0,0],
            [4,5,6,0,0,0,0,0,0],
            [7,8,9,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

@pytest.fixture
def sudoku_incorrect_box_board():
    return [[1,2,3,0,0,0,0,0,0],
            [1,5,9,0,0,0,0,0,0],
            [7,8,9,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

@pytest.fixture
def sudoku_correct_rows_board():
    return [[1,2,3,4,5,6,7,8,9],
            [2,3,4,5,6,7,8,9,1],
            [3,4,5,6,7,8,9,1,2],
            [4,5,6,7,8,9,1,2,3],
            [5,6,7,8,9,1,2,3,4],
            [6,7,8,9,1,2,3,4,5],
            [7,8,9,1,2,3,4,5,6],
            [8,9,1,2,3,4,5,6,7],
            [9,1,2,3,4,5,6,7,8]]

@pytest.fixture
def sudoku_incorrect_rows_board():
    return [[1,2,3,1,5,9,7,8,9],
            [2,3,4,2,6,1,8,9,1],
            [3,4,5,3,7,2,9,1,2],
            [4,5,6,4,8,9,1,2,3],
            [5,6,7,5,9,4,2,3,4],
            [6,7,8,6,1,5,3,4,5],
            [7,8,9,7,2,6,4,5,6],
            [8,9,1,8,3,7,5,6,7],
            [9,1,2,9,4,8,6,7,8]]

@pytest.fixture
def sudoku_correct_cols_board():
    return [[1,2,3,4,5,6,7,8,9],
            [2,3,4,5,6,7,8,9,1],
            [3,4,5,6,7,8,9,1,2],
            [4,5,6,7,8,9,1,2,3],
            [5,6,7,8,9,1,2,3,4],
            [6,7,8,9,1,2,3,4,5],
            [7,8,9,1,2,3,4,5,6],
            [8,9,1,2,3,4,5,6,7],
            [9,1,2,3,4,5,6,7,8]]

@pytest.fixture
def sudoku_incorrect_cols_board():
    return [[1,2,3,1,5,9,7,8,9],
            [2,3,4,2,6,1,8,9,1],
            [3,4,5,3,7,2,9,1,2],
            [1,2,3,4,5,6,7,8,9],
            [5,6,7,5,9,4,2,3,4],
            [9,1,2,3,4,5,6,7,8],
            [7,8,9,7,2,6,4,5,6],
            [8,9,1,8,3,7,5,6,7],
            [9,1,2,9,4,8,6,7,8]]

@pytest.fixture
def sudoku_correct_boxs_board():
    return [[1,2,3,2,3,4,3,4,5],
            [4,5,6,5,6,7,6,7,8],
            [7,8,9,8,9,1,9,1,2],
            [4,5,6,5,6,7,6,7,8],
            [7,8,9,8,9,1,9,1,2],
            [1,2,3,2,3,4,3,4,5],
            [7,8,9,8,9,1,9,1,2],
            [1,2,3,2,3,4,3,4,5],
            [4,5,6,5,6,7,6,7,8]]

@pytest.fixture
def sudoku_incorrect_boxs_board():
    return [[1,2,3,2,3,4,3,4,5],
            [1,5,9,2,6,1,3,7,2],
            [7,8,9,8,9,1,9,1,2],
            [4,5,6,5,6,7,6,7,8],
            [4,8,3,5,9,4,6,1,5],
            [1,2,3,2,3,4,3,4,5],
            [7,8,9,8,9,1,9,1,2],
            [7,2,6,8,3,7,9,4,8],
            [4,5,6,5,6,7,6,7,8]]

def test_sudoku_class_initialized(sudoku_class):
    if sudoku_class:
        assert sudoku_class
    else:
        assert False

def test_sudoku_class_has_empty_board(sudoku_class, sudoku_empty_board):
    assert sudoku_class.board == sudoku_empty_board

def test_sudoku_class_fails_empty_board(sudoku_class):
    assert not sudoku_class.correct_rows()
    assert not sudoku_class.correct_cols()
    assert not sudoku_class.correct_boxs()
    assert not sudoku_class.correct_board()

def test_sudoku_class_changes_easy_board(sudoku_class, sudoku_easy_unsolved_board):
    sudoku_class.change_board(sudoku_easy_unsolved_board)
    assert sudoku_class.board == sudoku_easy_unsolved_board

def test_sudoku_class_edits_board_at_position(sudoku_class, sudoku_edited_board):
    number: int = 9
    position: List = [0,0]
    sudoku_class.edit_board(9, position)
    assert sudoku_class.board == sudoku_edited_board

def test_sudoku_class_verifies_correct_pos(sudoku_class):
    low_boundary: int = 0
    high_boundary: int = 8
    assert sudoku_class.verify_pos(low_boundary)
    assert sudoku_class.verify_pos(high_boundary)

def test_sudoku_class_verifies_incorrect_pos(sudoku_class):
    low_broken: int = -1
    high_broken: int = 9
    assert not sudoku_class.verify_pos(low_broken)
    assert not sudoku_class.verify_pos(high_broken)

def test_sudoku_class_converts_correct_box_row(sudoku_class):
    low_boundary: int = 0
    high_boundary: int = 8
    low_range: List = range(0, 3)
    high_range: List = range(6, 9)
    assert sudoku_class.convert_box_row(low_boundary) == low_range
    assert sudoku_class.convert_box_row(high_boundary) == high_range

def test_sudoku_class_converts_incorrect_box_row(sudoku_class):
    low_broken: int = -1
    high_broken: int = 9
    broken_range: List = range(0)
    assert sudoku_class.convert_box_row(low_broken) == broken_range
    assert sudoku_class.convert_box_row(high_broken) == broken_range

def test_sudoku_class_converts_correct_box_col(sudoku_class):
    low_boundary: int = 0
    high_boundary: int = 8
    low_range: List = range(0, 3)
    high_range: List = range(6, 9)
    assert sudoku_class.convert_box_row(low_boundary) == low_range
    assert sudoku_class.convert_box_row(high_boundary) == high_range

def test_sudoku_class_converts_incorrect_box_col(sudoku_class):
    low_broken: int = -1
    high_broken: int = 9
    broken_range: List = range(0)
    assert sudoku_class.convert_box_col(low_broken) == broken_range
    assert sudoku_class.convert_box_col(high_broken) == broken_range

def test_sudoku_class_correct_row(sudoku_class, sudoku_correct_row_board):
    row = 0
    sudoku_class.change_board(sudoku_correct_row_board)
    assert sudoku_class.correct_row(row)

def test_sudoku_class_incorrect_row(sudoku_class, sudoku_incorrect_row_board):
    row = 0
    sudoku_class.change_board(sudoku_incorrect_row_board)
    assert not sudoku_class.correct_row(row)

def test_sudoku_class_correct_col(sudoku_class, sudoku_correct_col_board):
    col = 0
    sudoku_class.change_board(sudoku_correct_col_board)
    assert sudoku_class.correct_col(col)

def test_sudoku_class_incorrect_col(sudoku_class, sudoku_incorrect_col_board):
    col = 0
    sudoku_class.change_board(sudoku_incorrect_col_board)
    assert not sudoku_class.correct_col(col)

def test_sudoku_class_correct_box(sudoku_class, sudoku_correct_box_board):
    box = 0
    sudoku_class.change_board(sudoku_correct_box_board)
    assert sudoku_class.correct_box(box)

def test_sudoku_class_incorrect_box(sudoku_class, sudoku_incorrect_box_board):
    box = 0
    sudoku_class.change_board(sudoku_incorrect_box_board)
    assert not sudoku_class.correct_box(box)

def test_sudoku_class_correct_rows(sudoku_class, sudoku_correct_rows_board):
    sudoku_class.change_board(sudoku_correct_rows_board)
    assert sudoku_class.correct_rows()

def test_sudoku_class_incorrect_rows(sudoku_class, sudoku_incorrect_rows_board):
    sudoku_class.change_board(sudoku_incorrect_rows_board)
    assert not sudoku_class.correct_rows()

def test_sudoku_class_correct_cols(sudoku_class, sudoku_correct_cols_board):
    sudoku_class.change_board(sudoku_correct_cols_board)
    assert sudoku_class.correct_cols()

def test_sudoku_class_incorrect_cols(sudoku_class, sudoku_incorrect_cols_board):
    sudoku_class.change_board(sudoku_incorrect_cols_board)
    assert not sudoku_class.correct_cols()

def test_sudoku_class_correct_boxs(sudoku_class, sudoku_correct_boxs_board):
    sudoku_class.change_board(sudoku_correct_boxs_board)
    assert sudoku_class.correct_boxs()

def test_sudoku_class_incorrect_boxs(sudoku_class, sudoku_incorrect_boxs_board):
    sudoku_class.change_board(sudoku_incorrect_boxs_board)
    assert not sudoku_class.correct_boxs()

def test_sudoku_class_correct_board(sudoku_class, sudoku_easy_solved_board):
    sudoku_class.change_board(sudoku_easy_solved_board)
    assert sudoku_class.correct_rows()
    assert sudoku_class.correct_cols()
    assert sudoku_class.correct_boxs()
    assert sudoku_class.correct_board()

def test_sudoku_class_incorrect_board(sudoku_class, sudoku_easy_absolved_board):
    sudoku_class.change_board(sudoku_easy_absolved_board)
    assert not sudoku_class.correct_rows()
    assert not sudoku_class.correct_cols()
    assert not sudoku_class.correct_boxs()
    assert not sudoku_class.correct_board()