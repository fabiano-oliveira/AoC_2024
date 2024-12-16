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

        diff = abs(row[index] - row[index + 1])
        if diff > 3 or diff < 1:
            return False

    return is_increasing or is_decreasing   

def is_safe_ignoring_one(row: List[str]) -> bool:
    """
    Checks if the row is safe by removing one element at a time
    """
    for index in range(len(row)):
        new_row = row[:index] + row[index + 1:]
        if is_safe(new_row):
            return True
    return False

def select_safe_rows(rows: List[List[str]]) -> List[List[str]]:
    return [row for row in rows if is_safe(row) or is_safe_ignoring_one(row)]


print(select_safe_rows([
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [1, 2, 7, 3, 4],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]))


filename = './src/day2-input.csv'
rows = read_data(filename)

safe_rows = select_safe_rows(rows)
print("Safe rows: {}".format(len(safe_rows)))
