import pytest
from typing import List
from sudoku_solver import SudokuSolver

@pytest.fixture
def sudoku():
    sudoku = SudokuSolver()
    return sudoku

def test_sudoku_initialized(sudoku):
    assert sudoku