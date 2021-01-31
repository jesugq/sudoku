import pytest
from sudoku_solver import SudokuSolver

run_solve_tests = False

@pytest.fixture
def default_solver():
    solver = SudokuSolver()
    return solver

@pytest.fixture
def unsolved_solver(unsolved_puzzle):
    solver = SudokuSolver(unsolved_puzzle)
    return solver

@pytest.fixture
def solved_solver(solved_puzzle):
    solver = SudokuSolver(solved_puzzle)
    return solver

@pytest.fixture
def unsolved_hard_solver(unsolved_hard_puzzle):
    solver = SudokuSolver(unsolved_hard_puzzle)
    return solver

@pytest.fixture
def impossible_solver(impossible_puzzle):
    solver = SudokuSolver(impossible_puzzle)
    return solver

@pytest.fixture
def first_solver():
    solver = SudokuSolver()
    solver.guide = 0
    return solver

@pytest.fixture
def middle_solver():
    solver = SudokuSolver()
    solver.guide = 40
    return solver

@pytest.fixture
def last_solver():
    solver = SudokuSolver()
    solver.guide = 80
    return solver

@pytest.fixture
def unsettled_solver(unsettled_puzzle):
    solver = SudokuSolver(unsettled_puzzle)
    solver.guide = 0
    solver.board.edit_puzzle(9, 1, 8)
    return solver

@pytest.fixture
def unsettled_puzzle():
    return [[1,2,3,4,5,6,7,8,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

def test_default_solver_initialized(default_solver):
    assert default_solver

def test_default_solver_default_values(default_solver, empty_puzzle):
    guide = -1
    length = 81
    potential = [1,2,3,4,5,6,7,8,9]
    assert default_solver.guide == guide
    assert default_solver.board.puzzle == empty_puzzle
    assert len(default_solver.squares) == length
    index = 0
    for i in range(9):
        for j in range(9):
            assert default_solver.squares[index].row == i
            assert default_solver.squares[index].col == j
            assert default_solver.squares[index].potential == potential
            index += 1

def test_unsolved_solver_default_values(unsolved_solver, unsolved_puzzle):
    assert unsolved_solver.board.puzzle == unsolved_puzzle
    assert len(unsolved_solver.squares) == 53
    first_index = 0
    first_potential = [5,6,9]
    last_index = 52
    last_potential = [1,4,5,6]
    assert unsolved_solver.squares[first_index].row == 0
    assert unsolved_solver.squares[first_index].col == 0
    assert unsolved_solver.squares[first_index].potential == first_potential
    assert unsolved_solver.squares[last_index].row == 8
    assert unsolved_solver.squares[last_index].col == 8
    assert unsolved_solver.squares[last_index].potential == last_potential

def test_middle_solver_advances_guide(middle_solver):
    assert middle_solver.guide == 40
    assert middle_solver.advance_guide()
    assert middle_solver.guide == 41

def test_last_solver_not_advances_guide(last_solver):
    assert last_solver.guide == 80
    assert not last_solver.advance_guide()
    assert last_solver.guide == 80

def test_middle_solver_backtracks_guide(middle_solver):
    assert middle_solver.guide == 40
    assert middle_solver.backtrack_guide()
    assert middle_solver.guide == 39

def test_first_solver_not_backtracks_guide(first_solver):
    assert first_solver.guide == 0
    assert not first_solver.backtrack_guide()
    assert first_solver.guide == 0

def test_first_solver_settles_square_guide(first_solver):
    guide = 0
    pindex = 0
    number = 1
    potential = [1,2,3,4,5,6,7,8,9]
    assert first_solver.settle_square_guide()
    assert first_solver.squares[guide].pindex == pindex
    assert first_solver.squares[guide].number == number
    assert first_solver.squares[guide].potential == potential

def test_unsettled_solver_not_settles_square_guide(unsettled_solver):
    guide = 0
    pindex = -1
    number = 0
    potential = [9]
    assert not unsettled_solver.settle_square_guide()
    assert unsettled_solver.squares[guide].pindex == pindex
    assert unsettled_solver.squares[guide].number == number
    assert unsettled_solver.squares[guide].potential == potential

@pytest.mark.skipif(not run_solve_tests, reason='solves an unsolved sudoku')
def test_unsolved_solver_solves_sudoku(unsolved_solver, solved_puzzle):
    assert unsolved_solver.solve_sudoku()
    assert unsolved_solver.board.puzzle == solved_puzzle

@pytest.mark.skipif(not run_solve_tests, reason='solves an empty sudoku')
def test_default_solver_solves_sudoku(default_solver, full_puzzle):
    assert default_solver.solve_sudoku()
    assert default_solver.board.puzzle == full_puzzle

@pytest.mark.skipif(not run_solve_tests, reason='solves a hard sudoku')
def test_unsolved_hard_solver_solves_sudoku(unsolved_hard_solver, solved_hard_puzzle):
    assert unsolved_hard_solver.solve_sudoku()
    assert unsolved_hard_solver.board.puzzle == solved_hard_puzzle

@pytest.mark.skipif(not run_solve_tests, reason='solves a completed sudoku')
def test_solved_solver_solves_sudoku(solved_solver, solved_puzzle):
    assert solved_solver.solve_sudoku()
    assert solved_solver.board.puzzle == solved_puzzle

@pytest.mark.skipif(not run_solve_tests, reason='attempts to solve an impossible sudoku')
def test_impossible_solver_not_solves_sudoku(impossible_solver):
    assert not impossible_solver.solve_sudoku()