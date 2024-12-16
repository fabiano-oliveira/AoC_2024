from shared import read_all
import re
from typing import List





def parse_data(data: str) -> List[List[int]]:
    look_for = r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))"
    is_enabled = True
    instructions = []

    for match in re.finditer(look_for, data):
        if match.group(1).startswith("mul") and is_enabled:
            instructions.append((int(match.group(2)), int(match.group(3))))
        elif match.group(1) == "do()":
            is_enabled = True
        elif match.group(1) == "don't()":
            is_enabled = False

    return instructions

def multiply_elements(elements: List[List[int]]) -> List[int]:
    return [
        parameters[0] * parameters[1]
        for parameters
        in elements
    ]

filename = './src/day3-input.txt'
data = read_all(filename)

parsed_data = parse_data(data)
result = sum(multiply_elements(parsed_data))

print("Adding all: {}".format(result))
