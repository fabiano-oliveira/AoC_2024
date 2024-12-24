import pytest
from src.day8 import *

map: AntennaMap

@pytest.fixture
def map():
    map = AntennaMap(Point(10, 10))

    yield map

def test_adding_one_antenna(map):
    map.add_antenna("a", Point(1, 1))

    assert "a" in map.Antennas
    assert Point(1, 1) in map.Antennas["a"]
    
    assert len(map.Antinodes) == 0


def test_adding_two_antennas(map):
    map.add_antenna("a", Point(5, 5))
    map.add_antenna("a", Point(7, 6))

    assert "a" in map.Antennas
    assert Point(5, 5) in map.Antennas["a"]
    assert Point(7, 6) in map.Antennas["a"]

    assert len(map.Antinodes["a"]) == 2
    assert Point(3, 4) in map.Antinodes["a"]
    assert Point(9, 7) in map.Antinodes["a"]

def test_get_unique_antinodes(map):
    map.add_antenna("a", Point(5, 5))
    map.add_antenna("a", Point(7, 6))

    assert len(map.get_unique_antinodes()) == 2
    assert Point(3, 4) in map.get_unique_antinodes()
    assert Point(9, 7) in map.get_unique_antinodes()

@pytest.mark.parametrize(
    "point1,point2",
    [
        (Point(5, 5), Point(5, 6)),
        (Point(5, 5), Point(5, 4)),
        (Point(5, 5), Point(4, 5)),
        (Point(5, 5), Point(6, 5)),
    ]
)
def test_should_not_add_antinode_if_distance_is_below_two(map, point1, point2):
    map.add_antenna("a", point1)
    map.add_antenna("a", point2)

    assert len(map.get_unique_antinodes()) == 0

def test_aligned_antinodes(map):
    # arrange
    map.discover_aligned_antinodes = True
    map.add_antenna("T", Point(0,0))
    map.add_antenna("T", Point(1, 3))
    map.add_antenna("T", Point(2, 1))

    # act
    antinodes = map.Antinodes["T"]

    # assert
    assert len(antinodes) == 6
    assert Point(0, 5) in antinodes
    assert Point(2, 6) in antinodes
    assert Point(3, 9) in antinodes
    assert Point(4, 2) in antinodes 
    assert Point(6, 3) in antinodes 
    assert Point(8, 4) in antinodes


def test_count_antinodes_duplicated(map):
    # arrange
    map.discover_aligned_antinodes = True
    map.add_antenna("O", Point(2, 5))
    map.add_antenna("O", Point(3, 7))

    map.add_antenna("A", Point(5, 6))
    map.add_antenna("A", Point(9, 9))

    # act
    antinodes = map.get_all_antinodes()

    # assert
    assert len(antinodes) == 4
    assert Point(0, 1) in antinodes
    assert Point(1, 3) in antinodes 
    assert Point(4, 9) in antinodes
    assert Point(1, 3) in antinodes

def test_is_in_map(map):
    # assert

    assert map.is_point_in_map(Point(0, 0))
    assert map.is_point_in_map(Point(9, 9))
    assert not map.is_point_in_map(Point(10, 10))
    assert not map.is_point_in_map(Point(-1, 5))
    assert not map.is_point_in_map(Point(-1, -1))



def test_is_point_in_map(map):
    assert map.is_point_in_map(Point(5, 5))
    assert map.is_point_in_map(Point(0, 0))
    assert map.is_point_in_map(Point(9, 9))
    assert not map.is_point_in_map(Point(10, 10))
    assert not map.is_point_in_map(Point(-1, 5))
    assert not map.is_point_in_map(Point(5, -1))
