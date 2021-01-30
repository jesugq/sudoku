from typing import List

class SudokuSquare:
    def __init__(self, row: int, col: int, potential: List[int] = []):
        self.row: int = row
        self.col: int = col
        self.pindex: int = -1
        self.number: int = 0
        self.potential: List = potential

    def lock_number(self) -> None:
        self.number = self.potential[self.pindex]

    def proceed_potential(self) -> bool:
        if self.pindex + 1 < len(self.potential):
            self.pindex += 1
            self.lock_number()
            return True
        else:
            return False

    def precede_potential(self) -> bool:
        if self.pindex - 1 >= 0:
            self.pindex -= 1
            self.lock_number()
            return True
        else:
            return False

    def reset_square(self) -> None:
        self.pindex = -1
        self.number = 0