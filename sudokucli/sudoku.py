from typing import List
class Sudoku:
    def __init__(self):
        self.ROW = 0
        self.COL = 1
        self.INI = 0
        self.LEN = 9
        self.board = [[]]
        self.empty_board()
    
    def empty_board(self) -> List[List]:
        self.board = [[0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0]]

    def change_board(self, board: List[List]) -> List[List]:
        self.board = board

    def verify_pos(self, pos: int) -> bool:
        return pos >= self.INI and pos < self.LEN

    def convert_box_row(self, pos: int) -> List:
        if pos in [0, 1, 2]:
            return range(0, 3)
        elif pos in [3, 4, 5]:
            return range(3, 6)
        elif pos in [6, 7, 8]:
            return range(6, 9)
        else:
            return range(self.INI)
        
    def convert_box_col(self, pos: int) -> List:
        if pos in [0, 3, 6]:
            return range(0, 3)
        elif pos in [1, 4, 7]:
            return range(3, 6)
        elif pos in [2, 5, 8]:
            return range(6, 9)
        else:
            return range(self.INI)

    def edit_board(self, number: int, position: List) -> None:
        row = position[self.ROW]
        col = position[self.COL]
        self.board[row][col] = number

    def correct_row(self, row: int) -> bool:
        seen = []
        for i in range(self.LEN):
            value = self.board[row][i]
            if value not in seen:
                seen.append(value)
            else:
                return False
        return True

    def correct_col(self, col: int) -> bool:
        seen = []
        for i in range(self.LEN):
            value = self.board[i][col]
            if value not in seen:
                seen.append(value)
            else:
                return False
        return True

    def correct_box(self, box: int) -> bool:
        seen = []
        range_row = self.convert_box_row(box)
        range_col = self.convert_box_col(box)
        for i in range_row:
            for j in range_col:
                value = self.board[i][j]
                if value not in seen:
                    seen.append(value)
                else:
                    return False
        return True

    def correct_rows(self) -> bool:
        for i in range(self.LEN):
            if not self.correct_row(i):
                return False
        return True

    def correct_cols(self) -> bool:
        for i in range(self.LEN):
            if not self.correct_col(i):
                return False
        return True

    def correct_boxs(self) -> bool:
        for i in range(self.LEN):
            if not self.correct_box(i):
                return False
        return True

    def correct_board(self) -> bool:
        for i in range(self.LEN):
            if not self.correct_row(i):
                return False
            if not self.correct_col(i):
                return False
            if not self.correct_box(i):
                return False
        return True