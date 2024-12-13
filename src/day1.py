import csv
from typing import List

def insert_sorted(array: List[int], num:int):
    """
    Inserts a number into a sorted array using binary search to find the correct position.

    Parameters:
        array (list): A sorted list of numbers.
        num (int): The number to insert into the array.

    Returns:
        None: The input array is modified in place.
    """
    # Initialize the binary search bounds
    left, right = 0, len(array) - 1

    # Perform binary search to find the insertion point
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    # Insert the number at the correct position
    array.insert(left, num)


filename = './src/day1-input.csv'
left_locations = []
right_locations = []

with open(filename) as data:
    reader = csv.reader(data, delimiter=' ')
    for row in reader:
        insert_sorted(left_locations, int(row[0]))
        insert_sorted(right_locations, int(row[3]))

total_distance = 0
for index in range(len(left_locations)):
    total_distance += abs(right_locations[index] - left_locations[index])

print(total_distance)