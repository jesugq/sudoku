from typing import List
from sudoku_board import SudokuBoard
from sudoku_square import SudokuSquare

class SudokuSolver:
    def __init__(self, puzzle: List[List[int]] = None):
        self.guide: int = -1
        self.board: SudokuBoard = SudokuBoard(puzzle)
        self.squares: List[SudokuSquare] = []
        self.init_squares()

    def init_squares(self):
        for i, row in enumerate(self.board.puzzle):
            for j, number in enumerate(row):
                if number == 0:
                    potentials = self.board.grab_potential_pos(i, j)
                    self.squares.append(SudokuSquare(i, j, potentials))

    def advance_guide(self) -> bool:
        if self.guide + 1 < len(self.squares):
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
    
    def settle(self) -> bool:
        board = self.board
        square = self.squares[self.guide]
        while square.proceed_potential():
            board.edit_puzzle(square.number, square.row, square.col)
            board.print_puzzle()
            if board.check_pos(square.row, square.col):
                return True
        board.edit_puzzle(0, square.row, square.col)
        square.reset_square()
        return False
