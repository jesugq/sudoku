import pytest
from ..sudokucli.sudoku import Sudoku

@pytest.fixture
def sudoku_class():
    sudoku = Sudoku()
    return sudoku

def test_sudoku_class(sudoku_class):
    if sudoku_class:
        assert sudoku_class
    else:
        assert False