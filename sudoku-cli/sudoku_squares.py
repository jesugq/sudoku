from typing import List
from sudoku_square import SudokuSquare

class SudokuSquares:
    def __init__(self):
        self.index: int = -1
        self.array: List[SudokuSquare] = []
        self.grid: List[List] = [[]]
        self.init_grid()
    
    def init_grid(self):
        self.grid = [[-1,-1,-1,-1,-1,-1,-1,-1,-1], [-1,-1,-1,-1,-1,-1,-1,-1,-1], [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1], [-1,-1,-1,-1,-1,-1,-1,-1,-1], [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1], [-1,-1,-1,-1,-1,-1,-1,-1,-1], [-1,-1,-1,-1,-1,-1,-1,-1,-1]]

    def append_square(self, row:int, col:int, potential:List[int]):
        self.index += 1
        self.array.append(SudokuSquare(row, col, potential))
        self.grid[row][col] = self.index

    def settle_square(self, index: int) -> bool:
        square = self.array[index]
        while square.proceed_potential():
            if self.check_unique_in_pos(square.row, square.col):
                return True
        square.reset_square()
        return False

    def get_length(self):
        return self.index + 1

    def get_unpotential(self):
        for index in range(self.get_length()):
            if self.array[index].potential == []:
                return True
        return False
            
    def convert_pos_to_box(self, row: int, col: int) -> int:
        region_row: int = int(row / 3)
        region_col: int = int(col / 3)
        return region_row * 3 + region_col

    def range_box_to_row(self, box: int) -> List[int]:
        region_row: int = int(box / 3)
        start_row: int = region_row * 3
        return range(start_row, start_row + 3)

    def range_box_to_col(self, box: int) -> List[int]:
        region_col: int = int(box % 3)
        start_col: int = region_col * 3
        return range(start_col, start_col + 3)

    def check_unique_in_row(self, row:int, col:int):
        square: SudokuSquare = self.array[self.grid[row][col]]
        for i in range(9):
            if i != row and self.grid[i][col] != -1:
                if square.number == self.array[self.grid[i][col]].number:
                    return False
        return True

    def check_unique_in_col(self, row:int, col:int):
        square: SudokuSquare = self.array[self.grid[row][col]]
        for i in range(9):
            if i != col and self.grid[row][i] != -1:
                if square.number == self.array[self.grid[row][i]].number:
                    return False
        return True

    def check_unique_in_box(self, row:int, col:int):
        box: int = self.convert_pos_to_box(row, col)
        range_row: List[int] = self.range_box_to_row(box)
        range_col: List[int] = self.range_box_to_col(box)
        square: SudokuSquare = self.array[self.grid[row][col]]
        for i in range_row:
            for j in range_col:
                if i != row and j != col and self.grid[i][j] != -1:
                    if square.number == self.array[self.grid[i][j]].number:
                        return False
        return True

    def check_unique_in_pos(self, row:int, col:int):
        if not self.check_unique_in_row(row, col): return False
        if not self.check_unique_in_col(row, col): return False
        if not self.check_unique_in_box(row, col): return False
        return True