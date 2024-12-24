from shared import read_all_lines
from typing import List, Tuple, Dict
from collections import namedtuple

Point = namedtuple("Point", ["row", "column"])


class AntennaMap:
    def __init__(self, map_limit: Point, discover_aligned_antinodes: bool = False):
        self.__map_limit = map_limit
        self.__antennas: Dict[str, List[Point]] = {}
        self.__antinodes: Dict[str, List[Point]] = {}
        self.__discover_aligned_antinodes = discover_aligned_antinodes
    
    @property
    def discover_aligned_antinodes(self) -> bool:
        return self.__discover_aligned_antinodes

    @discover_aligned_antinodes.setter
    def discover_aligned_antinodes(self, value: bool):
        self.__discover_aligned_antinodes = value

    @property
    def Antennas(self):
        return self.__antennas

    @property
    def Antinodes(self):
        return self.__antinodes

    def get_unique_antinodes(self) -> set[Point]:
        return set(point for points in self.__antinodes.values() for point in points)
    
    def get_all_antinodes(self) -> List[Point]:
        return [point for points in self.__antinodes.values() for point in points]  

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

        if self.__distance(source, target) < 2 and not self.__discover_aligned_antinodes:
            return


        if self.__discover_aligned_antinodes:
            self.__antinodes[antenna].update(self.__all_opposite_points(source, target))
        else:
            opposite_point = self.__opposite_point(source, target)
            if not self.is_point_in_map(opposite_point):
                return

            self.__antinodes[antenna].add(opposite_point)

    def __distance(self, source: Point, target: Point):
        return abs(source.row - target.row) + abs(source.column - target.column)    

    def __opposite_point(self, source: Point, target: Point, multiplier: int = 1):
        delta_row = (target.row - source.row) * multiplier
        delta_column = (target.column - source.column) * multiplier

        return Point(source.row - delta_row, source.column - delta_column)
    
    def __all_opposite_points(self, source: Point, target: Point) -> List[Point]:
        multiplier = 1
        points = []

        while True:
            antinode_point = self.__opposite_point(source, target, multiplier)
            if self.is_point_in_map(antinode_point):
               points.append(antinode_point)
            else:
                break
            multiplier += 1

        return points

    def is_point_in_map(self, point: Point) -> bool:
        return 0 <= point.row < self.__map_limit.row and \
            0 <= point.column < self.__map_limit.column

    def __str__(self):
        content = ""
        antennas = {point: antenna for antenna, points in self.__antennas.items() for point in points}
        antinodes = {point: "#" for antenna, points in self.__antinodes.items() for point in points}
        objects_in_map = {**antennas, **antinodes}

        for row in range(self.__map_limit.row):
            for column in range(self.__map_limit.column):
                point = Point(row, column)
                if point in objects_in_map:
                    content += objects_in_map[point]
                else:
                    content += "."
            content += "\n"
        return content

def find_all_antennas(data: List[str]) -> AntennaMap:
    map = AntennaMap(Point(len(data), len(data[0])), discover_aligned_antinodes=True)

    for row, line in enumerate(data):
        for column, char in enumerate(line):
            if char != ".":
                map.add_antenna(char, Point(row, column))

    return map

def main():
    data = read_all_lines("./src/day8-input-sample.txt")
    map = find_all_antennas(data)
    print(map)
    antinodes = len(map.get_all_antinodes())
    print(f"There is {antinodes} antinodes")

if __name__ == "__main__":
    main()  