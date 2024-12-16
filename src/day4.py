from shared import read_all_lines
from typing import List


class WordCounter:
    def __init__(self, data: List[str]):
        self.data = data
 
    def has_xmas_in_this_direction(self, look_for: str, row: int, column: int, row_step: int, column_step: int) -> bool:
        current_row = row 
        current_column = column 

        for index in range(len(look_for)):
            if current_row < 0 or current_column < 0:
                return False

            if current_row < len(self.data) and current_column < len(self.data[current_row]):
                if self.data[current_row][current_column] != look_for[index]:
                    return False
            else:
                return False
            current_column += column_step
            current_row += row_step
        return index == len(look_for) - 1

    def count_xmas(self) -> int:
        count = row = column = 0

        while row < len(self.data):
            while column < len(self.data[row]):
                if self.data[row][column] == "X":
                    count += 1 if self.has_xmas_in_this_direction("XMAS", row, column, 0, 1) else 0
                    count += 1 if self.has_xmas_in_this_direction("XMAS", row, column, 0, -1) else 0
                    count += 1 if self.has_xmas_in_this_direction("XMAS", row, column, 1, 0) else 0
                    count += 1 if self.has_xmas_in_this_direction("XMAS", row, column, -1, 0) else 0
                    count += 1 if self.has_xmas_in_this_direction("XMAS", row, column, 1, 1) else 0
                    count += 1 if self.has_xmas_in_this_direction("XMAS", row, column, -1, -1) else 0
                    count += 1 if self.has_xmas_in_this_direction("XMAS", row, column, -1, 1) else 0
                    count += 1 if self.has_xmas_in_this_direction("XMAS", row, column, -1, -1) else 0
                column += 1
            row += 1
            column = 0
        return count

    def is_x_mas(self, center_row: int, center_column: int) -> bool:
        return (
            self.has_xmas_in_this_direction("MAS", center_row - 1, center_column - 1, 1, 1) or
            self.has_xmas_in_this_direction("MAS", center_row + 1, center_column + 1, -1, -1)
        ) and (
            self.has_xmas_in_this_direction("MAS", center_row - 1, center_column + 1, 1, -1) or
            self.has_xmas_in_this_direction("MAS", center_row + 1, center_column - 1, -1, 1)
        )
 
    def count_x_mas(self) -> int:
        count = row = column = 0

        while row < len(self.data):
            while column < len(self.data[row]):
                if self.data[row][column] == "A":
                    count += 1 if self.is_x_mas(row, column) else 0
                column += 1
            
            row += 1
            column = 0

        return count

def main():
    data = read_all_lines("./src/day4-input.txt")
    counter = WordCounter(data)

    count = counter.count_x_mas()
    print("Count of X-MAS: {}".format(count))
    count = counter.count_xmas()
    print("Count of XMAS: {}".format(count))

if __name__ == "__main__":
    main()  