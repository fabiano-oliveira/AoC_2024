import pytest
from src.day7 import parse_equation, parse_equations, fill_operations, generate_operations


def test_parse_equation():
    equation = parse_equation("190: 10 19")
    assert equation.result == 190
    assert equation.components == [10, 19]
    assert equation.operations == []

@pytest.mark.parametrize(
    "how_many,expected",
    [
        (1, [["+"], ["*"]]), 
        (2, [["+", "+"], 
             ["+", "*"], 
             ["*", "+"], 
             ["*", "*"]
            ]),
        (3, [["+", "+", "+"], 
             ["+", "+", "*"], 
             ["+", "*", "+"], 
             ["+", "*", "*"], 
             ["*", "+", "+"], 
             ["*", "+", "*"], 
             ["*", "*", "+"], 
             ["*", "*", "*"]
             ]),
    ]
)
def test_generate_operations(how_many, expected):
    operations = generate_operations(how_many)

    assert len(operations) == len(expected)
    assert operations == expected

@pytest.mark.parametrize(
    "equation,expected",
    [
        ("190: 10 19", [["*"]]),
        ("3267: 81 40 27", [["+", "*"], ["*", "+"]]),
    ]
)
def test_fill_operations(equation, expected):
    equation = parse_equation(equation)
    fill_operations(equation)
    assert equation.operations == expected

def test_fill_operations_with_empty():
    equation = parse_equation("83: 17 5")
    fill_operations(equation)
    assert equation.operations == []
