from shared import read_data
from typing import List


def is_safe(row: List[str]) -> bool:
    """
    Checks if the row is greater than 3 and 
    if the row is increasing or decreasing
    """
    
    is_increasing = is_decreasing = True

    for index in range(len(row) - 1):
        is_increasing = is_increasing and row[index] > row[index + 1]
        is_decreasing = is_decreasing and row[index] < row[index + 1]

        if abs(row[index] - row[index + 1]) > 3:
            return False

    return is_increasing or is_decreasing   



def select_safe_rows(rows: List[List[str]]) -> List[List[str]]:
    return [row for row in rows if is_safe(row)]


filename = './src/day2-input.csv'
rows = read_data(filename)

safe_rows = select_safe_rows(rows)
print("Safe rows: {}".format(len(safe_rows)))
