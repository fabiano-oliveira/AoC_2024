from shared import read_all_lines
from typing import List, Tuple, Dict
from collections import namedtuple

Point = namedtuple("Point", ["row", "column"])


class AntennaMap:
    def __init__(self, map_limit: Point):
        self.__map_limit = map_limit
        self.__antennas: Dict[str, List[Point]] = {}
        self.__antinodes: Dict[str, List[Point]] = {}

    @property
    def Antennas(self):
        return self.__antennas

    @property
    def Antinodes(self):
        return self.__antinodes

    def get_unique_antinodes(self) -> set[Point]:
        return set(point for points in self.__antinodes.values() for point in points)

    def add_antenna(self, antenna: str, point: Point):
        if antenna not in self.__antennas:
            self.__antennas[antenna] = []
        self.__add_antinodes_for(antenna, point)
        self.__antennas[antenna].append(point)

    def __add_antinodes_for(self, antenna: str, point: Point):
        for other_point in self.__antennas[antenna]:
            self.__add_antinode(antenna, point, other_point)
            self.__add_antinode(antenna, other_point, point)

    def __add_antinode(self, antenna: str, source: Point, target: Point):
        if antenna not in self.__antinodes:
            self.__antinodes[antenna] = set()

        if self.__distance(source, target) < 2:
            return

        opposite_point = self.__opposite_point(source, target)
        if not self.is_point_in_map(opposite_point):
            return

        self.__antinodes[antenna].add(opposite_point)

    def __distance(self, source: Point, target: Point):
        return abs(source.row - target.row) + abs(source.column - target.column)    

    def __opposite_point(self, source: Point, target: Point):
        delta_row = target.row - source.row
        delta_column = target.column - source.column

        return Point(source.row - delta_row, source.column - delta_column)

    def is_point_in_map(self, point: Point) -> bool:
        return 0 <= point.row < self.__map_limit.row and \
            0 <= point.column < self.__map_limit.column


def find_all_antennas(data: List[str]) -> AntennaMap:
    map = AntennaMap(Point(len(data), len(data[0])))

    for row, line in enumerate(data):
        for column, char in enumerate(line):
            if char != ".":
                map.add_antenna(char, Point(row, column))

    return map

def main():
    data = read_all_lines("./src/day8-input.txt")
    map = find_all_antennas(data)
    antinodes = len(map.get_unique_antinodes())
    print(f"There is {antinodes} antinodes")

if __name__ == "__main__":
    main()  