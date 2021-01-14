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
def sudoku_easy_board():
    return [[0,6,0,3,0,0,7,4,0],
            [5,3,7,0,9,0,0,0,0],
            [0,4,0,0,0,6,3,0,7],
            [0,9,0,0,5,1,2,3,8],
            [0,0,0,0,0,0,0,0,0],
            [7,1,3,6,2,0,0,4,0],
            [3,0,6,4,0,0,0,1,0],
            [0,0,0,0,6,0,5,2,3],
            [1,0,2,0,0,9,0,8,0]]

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

def test_sudoku_class_initialized(sudoku_class):
    if sudoku_class:
        assert sudoku_class
    else:
        assert False

def test_sudoku_class_has_empty_board(sudoku_class, sudoku_empty_board):
    assert sudoku_class.board == sudoku_empty_board

def test_sudoku_class_changes_easy_board(sudoku_class, sudoku_easy_board):
    sudoku_class.change_board(sudoku_easy_board)
    assert sudoku_class.board == sudoku_easy_board

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