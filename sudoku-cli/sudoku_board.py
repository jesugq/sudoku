from typing import List

class SudokuBoard:
    def __init__(self, puzzle: List[List[int]] = None):
        self.puzzle: List[List[int]] = puzzle
        if self.puzzle is None:
            self.init_puzzle()

    def init_puzzle(self) -> List[List[int]]:
        self.puzzle = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

    def print_puzzle(self) -> None:
        print()
        for i in range(len(self.puzzle)):
            print(self.puzzle[i])
        print()

    def edit_puzzle(self, number: int, row: int, col: int) -> None:
        self.puzzle[row][col] = number

    def grab_row(self, row: int) -> List[int]:
        return self.puzzle[row]

    def grab_col(self, col: int) -> List[int]:
        return [row[col] for row in self.puzzle]

    def grab_box(self, box: int) -> List[int]:
        range_row: List[int] = self.range_box_to_row(box)
        range_col: List[int] = self.range_box_to_col(box)
        numbers: List = []
        for i in range_row:
            for j in range_col:
                numbers.append(self.puzzle[i][j])
        return numbers

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

    def grab_unique(self, entire: List[int]) -> List[int]:
        unique: List = []
        for i in range(len(entire)):
            if entire[i] != 0 and entire[i] not in unique:
                unique.append(entire[i])
        return unique

    def grab_unique_row(self, row: int) -> List[int]:
        entire: List = self.grab_row(row)
        return self.grab_unique(entire)

    def grab_unique_col(self, col: int) -> List[int]:
        entire: List = self.grab_col(col)
        return self.grab_unique(entire)

    def grab_unique_box(self, box: int) -> List[int]:
        entire: List = self.grab_box(box)
        return self.grab_unique(entire)

    def evaluate(self, unique: List[int]) -> bool:
        return len(unique) == 9

    def evaluate_row(self, row: int) -> bool:
        unique: List[int] = self.grab_unique_row(row)
        return self.evaluate(unique)

    def evaluate_col(self, col: int) -> bool:
        unique: List[int] = self.grab_unique_col(col)
        return self.evaluate(unique)

    def evaluate_box(self, box: int) -> bool:
        unique: List[int] = self.grab_unique_box(box)
        return self.evaluate(unique)

    def evaluate_board(self) -> bool:
        for i in range(9):
            if not self.evaluate_row(i): return False
            if not self.evaluate_col(i): return False
            if not self.evaluate_box(i): return False
        return True

    def grab_active(self, entire: List[int]) -> List[int]:
        active: List = []
        for i in range(len(entire)):
            if entire[i] != 0:
                active.append(entire[i])
        return active

    def grab_active_row(self, row: int) -> List[int]:
        entire: List = self.grab_row(row)
        return self.grab_active(entire)
    
    def grab_active_col(self, col: int) -> List[int]:
        entire: List = self.grab_col(col)
        return self.grab_active(entire)

    def grab_active_box(self, box: int) -> List[int]:
        entire: List = self.grab_box(box)
        return self.grab_active(entire)
    
    def check(self, active: List[int], target: int) -> bool:
        count = 0
        for number in active:
            if number == target:
                count += 1
        return count == 1

    def check_pos(self, row: int, col: int) -> bool:
        target = self.puzzle[row][col]
        active_row = self.grab_active_row(row)
        active_col = self.grab_active_col(col)
        active_box = self.grab_active_box(self.convert_pos_to_box(row, col))
        if target in active_row:
            active_row.remove(target)
        if target in active_col:
            active_col.remove(target)
        return self.check(active_row + active_col + active_box, target)

    def grab_potential(self, unique: List[int]) -> List[int]:
        potential: List[int] = []
        for i in range(1,10):
            if i not in unique:
                potential.append(i)
        return potential

    def grab_potential_row(self, row: int) -> List[int]:
        unique: List[int] = self.grab_unique_row(row)
        return self.grab_potential(unique)

    def grab_potential_col(self, col: int) -> List[int]:
        unique: List[int] = self.grab_unique_col(col)
        return self.grab_potential(unique)

    def grab_potential_box(self, box: int) -> List[int]:
        unique: List[int] = self.grab_unique_box(box)
        return self.grab_potential(unique)

    def grab_potential_pos(self, row: int, col: int) -> List[int]:
        unique_row: List[int] = self.grab_unique_row(row)
        unique_col: List[int] = self.grab_unique_col(col)
        unique_box: List[int] = self.grab_unique_box(self.convert_pos_to_box(row, col))
        return self.grab_potential(unique_row + unique_col + unique_box)