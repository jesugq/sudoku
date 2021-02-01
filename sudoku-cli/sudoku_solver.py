from typing import List
from sudoku_board import SudokuBoard
from sudoku_squares import SudokuSquares

class SudokuSolver:
    def __init__(self, puzzle: List[List[int]] = None):
        self.guide: int = -1
        self.board: SudokuBoard = SudokuBoard(puzzle)
        self.squares: SudokuSquares = SudokuSquares()
        self.init_squares()

    def init_squares(self):
        for i, row in enumerate(self.board.puzzle):
            for j, number in enumerate(row):
                if number == 0:
                    potential = self.board.grab_potential_pos(i, j)
                    self.squares.append_square(i, j, potential)

    def advance_guide(self) -> bool:
        if self.guide + 1 < self.squares.get_length():
            self.guide += 1
            return True
        else:
            return False

    def backtrack_guide(self) -> bool:
        if self.guide -1 >= 0:
            self.guide -= 1
            return True
        else:
            return False

    def settle_guide(self) -> bool:
        return self.squares.settle_square(self.guide)

    def settle_puzzle(self) -> None:
        square: SudokuSquare = self.squares.array[self.guide]
        self.board.edit_puzzle(square.number, square.row, square.col)

    def solve_sudoku(self) -> bool:
        if self.squares.get_length() == 0:
            return True
        if self.squares.get_unpotential():
            return False
        self.advance_guide()
        while True:
            if self.settle_guide():
                self.settle_puzzle()
                if not self.advance_guide():
                    return True
            else:
                if not self.backtrack_guide():
                    return False