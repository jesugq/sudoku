from typing import List

class SudokuSquare:
    def __init__(self, row: int, col: int, potentials: List[int] = []):
        self.row: int = row
        self.col: int = col
        self.pindex: int = -1
        self.number: int = 0
        self.solved: bool = False
        self.potentials: List = potentials

    def lock_number(self) -> None:
        self.number = self.potentials[self.pindex]
        self.solved = True

    def proceed_potential(self) -> bool:
        if self.pindex + 1 < len(self.potentials):
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