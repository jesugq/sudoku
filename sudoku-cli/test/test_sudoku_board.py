import pytest
from typing import List
from sudoku_board import SudokuBoard

@pytest.fixture
def empty_board():
    board = SudokuBoard()
    return board

@pytest.fixture
def unsolved_board(unsolved_puzzle):
    board = SudokuBoard(unsolved_puzzle)
    return board

@pytest.fixture
def solved_board(solved_puzzle):
    board = SudokuBoard(solved_puzzle)
    return board

@pytest.fixture
def ordered_board(ordered_puzzle):
    board = SudokuBoard(ordered_puzzle)
    return board

@pytest.fixture
def boxed_board(boxed_puzzle):
    board = SudokuBoard(boxed_puzzle)
    return board

@pytest.fixture
def unique_board(unique_puzzle):
    board = SudokuBoard(unique_puzzle)
    return board

@pytest.fixture
def broken_board(broken_puzzle):
    board = SudokuBoard(broken_puzzle)
    return board

@pytest.fixture
def potential_board(potential_puzzle):
    board = SudokuBoard(potential_puzzle)
    return board

@pytest.fixture
def empty_puzzle():
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
def edited_puzzle():
    return [[9,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,9]]

@pytest.fixture
def unsolved_puzzle():
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
def solved_puzzle():
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
def ordered_puzzle():
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
def boxed_puzzle():
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
def unique_puzzle():
    return [[1,2,3,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,1,0,0,0,0],
            [0,0,0,0,2,0,0,0,0],
            [0,0,0,0,3,0,0,0,0],
            [0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,2,0],
            [0,0,0,0,0,0,0,0,3]]

@pytest.fixture
def broken_puzzle():
    return [[1,1,1,9,1,9,1,1,1],
            [1,3,4,5,6,7,8,9,1],
            [1,4,5,6,7,8,9,1,2],
            [9,5,6,7,8,9,1,2,3],
            [1,6,7,8,9,1,2,3,4],
            [9,7,8,9,1,2,3,4,5],
            [1,8,9,1,2,3,1,1,1],
            [1,9,1,2,3,4,9,1,9],
            [1,1,2,3,4,5,1,1,1]]

@pytest.fixture
def potential_puzzle():
    return [[0,0,0,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,5,0,0,0,0,0],
            [3,0,0,0,0,0,0,0,4],
            [0,0,0,0,0,6,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,2,0,0,0,0]]

def test_empty_board_initialized(empty_board):
    assert empty_board

def test_empty_board_default_values(empty_board, empty_puzzle):
    assert empty_board.puzzle == empty_puzzle

def test_empty_board_edits_puzzle(empty_board, edited_puzzle):
    edited_number = 9
    first_edited_pos = 0
    last_edited_pos = 8
    empty_board.edit_puzzle(edited_number, first_edited_pos, first_edited_pos)
    empty_board.edit_puzzle(edited_number, last_edited_pos, last_edited_pos)
    assert empty_board.puzzle == edited_puzzle

def test_ordered_board_grabs_row(ordered_board):
    first_row = [1,2,3,4,5,6,7,8,9]
    first_index = 0
    last_row = [9,1,2,3,4,5,6,7,8]
    last_index = 8
    assert ordered_board.grab_row(first_index) == first_row
    assert ordered_board.grab_row(last_index) == last_row

def test_ordered_board_grabs_col(ordered_board):
    first_col = [1,2,3,4,5,6,7,8,9]
    first_index = 0
    last_col = [9,1,2,3,4,5,6,7,8]
    last_index = 8
    assert ordered_board.grab_col(first_index) == first_col
    assert ordered_board.grab_col(last_index) == last_col

def test_boxed_board_grabs_box(boxed_board):
    first_box = [1,2,3,4,5,6,7,8,9]
    first_index = 0
    last_box = [9,1,2,3,4,5,6,7,8]
    last_index = 8
    assert boxed_board.grab_box(first_index) == first_box
    assert boxed_board.grab_box(last_index) == last_box

def test_boxed_board_ranges_pos_to_box(boxed_board):
    first_row = 0
    first_col = 0
    first_box = 0
    last_row = 8
    last_col = 8
    last_box = 8
    assert boxed_board.range_pos_to_box(first_row, first_col) == first_box
    assert boxed_board.range_pos_to_box(last_row, last_col) == last_box

def test_boxed_board_ranges_box_to_row(boxed_board):
    upper_left_box = 0
    upper_left_range = range(0, 3)
    center_left_box = 3
    center_left_range = range(3, 6)
    lower_left_box = 6
    lower_left_range = range(6, 9)
    assert boxed_board.range_box_to_row(upper_left_box) == upper_left_range
    assert boxed_board.range_box_to_row(center_left_box) == center_left_range
    assert boxed_board.range_box_to_row(lower_left_box) == lower_left_range

def test_boxed_board_ranges_box_to_col(boxed_board):
    upper_left_box = 0
    upper_left_range = range(0, 3)
    upper_middle_box = 1
    upper_middle_range = range(3, 6)
    upper_right_box = 2
    upper_right_range = range(6, 9)
    assert boxed_board.range_box_to_col(upper_left_box) == upper_left_range
    assert boxed_board.range_box_to_col(upper_middle_box) == upper_middle_range
    assert boxed_board.range_box_to_col(upper_right_box) == upper_right_range

def test_unique_board_grabs_unique(unique_board):
    entire = [1,2,3,0,0,0,0,0,0]
    unique = [1,2,3]
    assert unique_board.grab_unique(entire) == unique

def test_unique_board_grabs_unique_row(unique_board):
    unique_row = [1,2,3]
    unique_index = 0
    assert unique_board.grab_unique_row(unique_index) == unique_row

def test_unique_board_grabs_unique_col(unique_board):
    unique_col = [1,2,3]
    unique_index = 4
    assert unique_board.grab_unique_col(unique_index) == unique_col

def test_unique_board_grabs_unique_box(unique_board):
    unique_box = [1,2,3]
    unique_index = 8
    assert unique_board.grab_unique_box(unique_index) == unique_box

def test_unique_board_evaluates(unique_board):
    full = [1,2,3,4,5,6,7,8,9]
    assert unique_board.evaluate(full)

def test_unique_board_not_evaluates(unique_board):
    halfway = [1,2,3]
    assert not unique_board.evaluate(halfway)    

def test_ordered_board_evaluates_row(ordered_board):
    first_row = 0
    last_row = 8
    assert ordered_board.evaluate_row(first_row)
    assert ordered_board.evaluate_row(last_row)

def test_broken_board_not_evaluates_row(broken_board):
    wrong_row = 0
    assert not broken_board.evaluate_row(wrong_row)

def test_ordered_board_evaluates_col(ordered_board):
    first_col = 0
    last_col = 8
    assert ordered_board.evaluate_col(first_col)
    assert ordered_board.evaluate_col(last_col)

def test_broken_board_not_evaluates_col(broken_board):
    wrong_col = 0
    assert not broken_board.evaluate_col(wrong_col)

def test_boxed_board_evaluates_box(boxed_board):
    upper_left_box = 0
    lower_right_box = 8
    assert boxed_board.evaluate_box(upper_left_box)
    assert boxed_board.evaluate_box(lower_right_box)
    
def test_broken_board_not_evaluates_box(broken_board):
    wrong_box = 8
    assert not broken_board.evaluate_box(wrong_box)

def test_solved_board_evaluates_board(solved_board):
    assert solved_board.evaluate_board()

def test_unsolved_board_not_evaluates_board(unsolved_board):
    assert not unsolved_board.evaluate_board()

def test_solved_board_evaluate_pos(solved_board):
    row = 0
    col = 0
    assert solved_board.evaluate_pos(row, col)

def test_unique_board_grabs_potential(unique_board):
    unique = [1,2,3]
    potential = [4,5,6,7,8,9]
    assert unique_board.grab_potential(unique) == potential

def test_unique_board_grabs_potential_row(unique_board):
    index = 0
    potential = [4,5,6,7,8,9]
    assert unique_board.grab_potential_row(index)

def test_unique_board_grabs_potential_col(unique_board):
    index = 4
    potential = [4,5,6,7,8,9]
    assert unique_board.grab_potential_col(index)

def test_unique_board_grabs_potential_box(unique_board):
    index = 8
    potential = [4,5,6,7,8,9]
    assert unique_board.grab_potential_box(index)

def test_potential_board_grabs_potential_pos(potential_board):
    row = 4
    col = 4
    potential = [7,8,9]
    assert potential_board.grab_potential_pos(row, col) == potential