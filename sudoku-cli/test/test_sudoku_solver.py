import pytest
from typing import List
from sudoku_solver import SudokuSolver

@pytest.fixture
def default_sudoku():
    sudoku = SudokuSolver()
    return sudoku

def test_sudoku_initialized(default_sudoku):
    assert default_sudoku