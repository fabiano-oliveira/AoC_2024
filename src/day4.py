from shared import read_all_lines
from typing import List


class WordCounter:
    def __init__(self, data: List[str], look_for: str = "XMAS"):
        self.data = data
        self.look_for = look_for
        self.row = 0
        self.column = 0
 
    def has_xmas_in_this_direction(self, row_step: int, column_step: int) -> bool:
        current_row = self.row + row_step
        current_column = self.column + column_step

        for index in range(1, len(self.look_for)):
            if current_row < 0 or current_column < 0:
                return False

            if current_row < len(self.data) and current_column < len(self.data[current_row]):
                if self.data[current_row][current_column] != self.look_for[index]:
                    return False
            else:
                return False
            current_column += column_step
            current_row += row_step
        return True and index == len(self.look_for) - 1

    def count_xmas(self) -> int:
        count = self.row = self.column = 0

        while self.row < len(self.data):
            while self.column < len(self.data[self.row]):
                if self.data[self.row][self.column] == self.look_for[0]:
                    count += 1 if self.has_xmas_in_this_direction(0, 1) else 0
                    count += 1 if self.has_xmas_in_this_direction(0, -1) else 0
                    count += 1 if self.has_xmas_in_this_direction(1, 0) else 0
                    count += 1 if self.has_xmas_in_this_direction(-1, 0) else 0
                    count += 1 if self.has_xmas_in_this_direction(1, 1) else 0
                    count += 1 if self.has_xmas_in_this_direction(1, -1) else 0
                    count += 1 if self.has_xmas_in_this_direction(-1, 1) else 0
                    count += 1 if self.has_xmas_in_this_direction(-1, -1) else 0
                self.column += 1
            self.row += 1
            self.column = 0
        return count



def main():
    data = read_all_lines("./src/day4-input.txt")
    counter = WordCounter(data)
    count = counter.count_xmas()
    print("Count of XMAS: {}".format(count))

if __name__ == "__main__":
    main()  