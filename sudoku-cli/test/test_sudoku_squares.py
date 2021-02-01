import pytest
from sudoku_square import SudokuSquare
from sudoku_squares import SudokuSquares

@pytest.fixture
def default_squares():
    squares = SudokuSquares()
    return squares

@pytest.fixture
def appended_squares():
    squares = SudokuSquares()
    row = 0
    col = 0
    potential = [1,2,3]
    squares.append_square(row, col, potential)
    return squares

@pytest.fixture
def row_squares():
    squares = SudokuSquares()
    squares.append_square(0, 0, [1,2,3])
    squares.append_square(4, 0, [4,5,6])
    squares.append_square(8, 0, [7,8,9])
    squares.array[0].proceed_potential()
    squares.array[1].proceed_potential()
    squares.array[2].proceed_potential()
    return squares

@pytest.fixture
def col_squares():
    squares = SudokuSquares()
    squares.append_square(0, 0, [1,2,3])
    squares.append_square(0, 4, [4,5,6])
    squares.append_square(0, 8, [7,8,9])
    squares.array[0].proceed_potential()
    squares.array[1].proceed_potential()
    squares.array[2].proceed_potential()
    return squares

@pytest.fixture
def box_squares():
    squares = SudokuSquares()
    squares.append_square(0, 0, [1,2,3])
    squares.append_square(1, 1, [4,5,6])
    squares.append_square(2, 2, [7,8,9])
    squares.array[0].proceed_potential()
    squares.array[1].proceed_potential()
    squares.array[2].proceed_potential()
    return squares

@pytest.fixture
def default_grid():
    return [[-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1]]

@pytest.fixture
def appended_grid():
    return [[-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1, 0,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1,-1,-1,-1]]

def test_default_squares_class_initialized(default_squares):
    assert type(default_squares) is SudokuSquares

def test_default_squares_class_default_values(default_squares, default_grid):
    index = -1
    array = []
    assert default_squares.index == index
    assert default_squares.array == array
    assert default_squares.grid == default_grid

def test_default_squares_appends_square(default_squares, appended_grid):
    row = 4
    col = 4
    potential = [1,2,3]
    default_squares.append_square(row, col, potential)
    index = 0
    assert default_squares.index == index
    assert type(default_squares.array[0]) is SudokuSquare
    assert default_squares.grid == appended_grid

def test_default_squares_gets_length(default_squares):
    length = 0
    assert default_squares.get_length() == length

def test_default_squares_converts_pos_to_box(default_squares):
    first_row = 0
    first_col = 0
    first_box = 0
    last_row = 8
    last_col = 8
    last_box = 8
    assert default_squares.convert_pos_to_box(first_row, first_col) == first_box
    assert default_squares.convert_pos_to_box(last_row, last_col) == last_box

def test_default_squares_ranges_box_to_row(default_squares):
    upper_left_box = 0
    upper_left_range = range(0, 3)
    center_left_box = 3
    center_left_range = range(3, 6)
    lower_left_box = 6
    lower_left_range = range(6, 9)
    assert default_squares.range_box_to_row(upper_left_box) == upper_left_range
    assert default_squares.range_box_to_row(center_left_box) == center_left_range
    assert default_squares.range_box_to_row(lower_left_box) == lower_left_range

def test_default_squares_ranges_box_to_col(default_squares):
    upper_left_box = 0
    upper_left_range = range(0, 3)
    upper_middle_box = 1
    upper_middle_range = range(3, 6)
    upper_right_box = 2
    upper_right_range = range(6, 9)
    assert default_squares.range_box_to_col(upper_left_box) == upper_left_range
    assert default_squares.range_box_to_col(upper_middle_box) == upper_middle_range
    assert default_squares.range_box_to_col(upper_right_box) == upper_right_range

def test_row_squares_checks_unique_in_row(row_squares):
    row = 0
    col = 0
    assert row_squares.check_unique_in_row(row, col)

def test_row_squares_not_checks_unique_in_row(row_squares):
    row = 0
    col = 0
    row_squares.array[2].number = 1
    assert not row_squares.check_unique_in_row(row, col)

def test_col_squares_checks_unique_in_col(col_squares):
    row = 0
    col = 0
    assert col_squares.check_unique_in_col(row, col)

def test_col_squares_not_checks_unique_in_col(col_squares):
    row = 0
    col = 0
    col_squares.array[2].number = 1
    assert not col_squares.check_unique_in_col(row, col)

def test_box_squares_checks_unique_in_box(box_squares):
    row = 0
    col = 0
    assert box_squares.check_unique_in_box(row, col)

def test_box_squares_not_checks_unique_in_box(box_squares):
    row = 0
    col = 0
    box_squares.array[2].number = 1
    assert not box_squares.check_unique_in_box(row, col)