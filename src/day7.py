from .shared import read_all_lines
from typing import List, Tuple, Dict
from collections import namedtuple


Equation = namedtuple("Equation", ["result", "components", "operations"])


def parse_equation(line: str) -> Equation:
    result, components = line.split(":")
    components = components.strip().split(" ")
    return fill_operations(Equation(int(result), [int(component) for component in components], []))

def parse_equations(data: List[str]) -> List[Equation]:
    return [parse_equation(line) for line in data]  

def generate_operations(how_many: int) -> List[str]:
    operations = ["+", "*"]
    result = [[op] for op in operations]

    while how_many > 1:
        how_many -= 1
        result = [
            item + [op] for item in result for op in operations
        ]    

    return result

def calculate(accumulated: int, operation: str, next_value: int) -> int:
    if operation == "+":
        return accumulated + next_value
    elif operation == "*":
        return accumulated * next_value

def fill_operations(equation: Equation) -> Equation:
    operations_available = generate_operations(len(equation.components) - 1)

    for operation_set in operations_available:
        total = equation.components[0]
        for index in range(len(operation_set)):
            total = calculate(total, operation_set[index], equation.components[index + 1])

        if total == equation.result:
            equation.operations.append(operation_set)

    return equation

def select_non_empty_operations(equations: List[Equation]) -> List[Equation]:
    return [equation for equation in equations if len(equation.operations) > 0]

def main():
    data = read_all_lines("./src/day7-input.txt")
    equations = parse_equations(data)
    valid_equations = select_non_empty_operations(equations)
    total = sum(equation.result for equation in valid_equations)
    print("Sum of valid equations:", total)

if __name__ == "__main__":
    main()