from shared import read_all_lines
from typing import List, Tuple, Dict
from collections import namedtuple


Equation = namedtuple("Equation", ["result", "components", "operations"])
generated_operations_cache = {}

def parse_equation(line: str) -> Equation:
    """
    Parse an equation from a line of text and fill in the operations.
    """
    result, components = line.split(":")
    components = components.strip().split(" ")
    return fill_operations(Equation(int(result), [int(component) for component in components], []))

def parse_equations(data: List[str]) -> List[Equation]:
    """
    Parse a list of equations from a list of lines.
    """
    return [parse_equation(line) for line in data]  

def generate_operations(how_many: int) -> List[str]:
    """
    Generate all possible operations for a given number of components.
    """

    # check the cache before generating operations
    if how_many in generated_operations_cache:
        return generated_operations_cache[how_many]

    # generate operations
    operations = ["+", "*", "||"]
    result = [[op] for op in operations]

    for i in range(how_many - 1):
        result = [
            item + [op] for item in result for op in operations
        ]

    # cache the result
    generated_operations_cache[how_many] = result

    return result

def calculate(accumulated: int, operation: str, next_value: int) -> int:
    """
    Calculate the result of an operation.
    """
    if operation == "+":
        return accumulated + next_value
    elif operation == "*":
        return accumulated * next_value
    elif operation == "||":
        return int(str(accumulated) + str(next_value))

def fill_operations(equation: Equation) -> Equation:
    """
    Fill in the operations for an equation.
    """
    operations_available = list(reversed(generate_operations(len(equation.components) - 1)))
    equation.operations.clear()

    for operation_set in operations_available:
        total = equation.components[0]
        for index in range(len(operation_set)):
            total = calculate(total, operation_set[index], equation.components[index + 1])
            if total > equation.result:
                break

        if total == equation.result:
            equation.operations.append(operation_set)
            break

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