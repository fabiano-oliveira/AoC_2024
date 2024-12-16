import csv
from typing import List

def read_data(filename):
    with open(filename) as data:
        reader = csv.reader(data, delimiter=' ')
        return [[int(element) for element in row] for row in reader]


def read_all(filename: str) -> str:
    with open(filename) as data:
        return data.read()

def read_all_lines(filename: str) -> List[str]:
    with open(filename) as data:
        return data.readlines()
