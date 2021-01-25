import pytest
from typing import List
from sudoku_square import SudokuSquare

@pytest.fixture
def default_square():
    row: int = 0
    col: int = 0
    square = SudokuSquare(row,col)
    return square

@pytest.fixture
def common_square():
    row: int = 0
    col: int = 0
    potentials: List = [1,2]
    square = SudokuSquare(row, col, potentials)
    return square

@pytest.fixture
def middle_square():
    row: int = 0
    col: int = 0
    potentials: List = [1,2,3]
    square = SudokuSquare(row, col, potentials)
    square.proceed_potential()
    square.proceed_potential()
    return square

def test_default_square_class_initialized(default_square):
    assert default_square

def test_default_square_class_default_values(default_square):
    pindex: int = -1
    number: int = 0
    solved: bool = False
    potentials: List = []
    assert default_square.pindex == pindex
    assert default_square.number == number
    assert default_square.solved == solved
    assert default_square.potentials == potentials

def test_common_square_locks_number(common_square):
    pindex = 0
    potentials = [1,2]
    common_square.pindex = pindex
    common_square.lock_number()
    assert common_square.number == potentials[pindex]

def test_common_square_proceeds_potential(common_square):
    potentials = [1,2]
    assert common_square.number == 0
    assert common_square.proceed_potential()
    assert common_square.number == potentials[0]
    assert common_square.proceed_potential()
    assert common_square.number == potentials[1]
    assert not common_square.proceed_potential()
    assert common_square.number == potentials[1]

def test_default_square_not_proceeds_potential(default_square):
    assert default_square.number == 0
    assert not default_square.proceed_potential()
    assert default_square.number == 0

def test_middle_square_precedes_potential(middle_square):
    potentials = [1,2,3]
    assert middle_square.number == potentials[1]
    assert middle_square.precede_potential()
    assert middle_square.number == potentials[0]
    assert not middle_square.precede_potential()
    assert middle_square.number == potentials[0]