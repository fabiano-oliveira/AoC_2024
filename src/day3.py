from shared import read_all
import re
from typing import List



def parse_data(data: str) -> List[List[int]]:
    look_for = r"mul\((\d{1,3}),(\d{1,3})\)"
    return [
        [int(match.group(1)), int(match.group(2))] 
        for match 
        in re.finditer(look_for, data)
    ]

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
