from shared import read_all_lines
from typing import List, Tuple, Dict


class Room:

    def __init__(self, data: List[str]):
        self.data = [list(line) for line in data]
        self.guard_position = self.find_guard_position()

    def find_guard_position(self) -> Tuple[int, int]:
        for row, line in enumerate(self.data):
            for column, value in enumerate(line):
                if value in ["^", ">", "<", "v", "V"]:
                    return row, column
        return -1, -1

    def still_on_map(self, row: int, column: int) -> bool:
        return row >= 0 and column >= 0 and row < len(self.data) and column < len(self.data[row])

    def has_obstacle_on_top(self) -> bool:
        new_row = self.guard_position[0] - 1    
        return self.still_on_map(new_row, self.guard_position[1]) and self.data[new_row][self.guard_position[1]] == "#"

    def has_obstacle_on_bottom(self) -> bool:
        new_row = self.guard_position[0] + 1    
        return self.still_on_map(new_row, self.guard_position[1]) and self.data[new_row][self.guard_position[1]] == "#"

    def has_obstacle_on_left(self) -> bool:
        new_column = self.guard_position[1] - 1    
        return self.still_on_map(self.guard_position[0], new_column) and self.data[self.guard_position[0]][new_column] == "#"   

    def has_obstacle_on_right(self) -> bool:
        new_column = self.guard_position[1] + 1    
        return self.still_on_map(self.guard_position[0], new_column) and self.data[self.guard_position[0]][new_column] == "#"

    def set_guard_on(self, direction: str, row: int, column: int):
        if self.still_on_map(row, column):
            self.data[row][column] = direction
            self.guard_position = row, column
            return True
        else:
            return False

    def move_guard(self) -> bool:
        row = self.guard_position[0]
        column = self.guard_position[1]

        if row < 0 or column < 0 or row >= len(self.data) or column >= len(self.data[row]):
            return False

        direction = self.data[row][column]
        self.data[row][column] = "X"

        match direction:
            case "^":
                if not self.has_obstacle_on_top():
                    row -= 1
                elif not self.has_obstacle_on_right():
                    column += 1
                    direction = ">"
                elif not self.has_obstacle_on_bottom():
                    row += 1
                    direction = "v"
                elif self.has_obstacle_on_left():
                    return False
                else:
                    column -= 1
                    direction = "<"
            case ">":
                if not self.has_obstacle_on_right():
                    column += 1
                elif not self.has_obstacle_on_bottom():
                    row += 1
                    direction = "v"
                elif not self.has_obstacle_on_left():
                    column -= 1
                    direction = "<"
                elif self.has_obstacle_on_top():
                    return False
                else:
                    row -= 1
                    direction = "^"
            case "<":
                if not self.has_obstacle_on_left():
                    column -= 1
                elif not self.has_obstacle_on_top():
                    row -= 1
                    direction = "^"
                elif not self.has_obstacle_on_right():
                    column += 1
                    direction = ">"
                elif self.has_obstacle_on_top():
                    return False
                else:
                    row += 1
                    direction = "v"
            case "v" | "V":
                if not self.has_obstacle_on_bottom():
                    row += 1
                elif not self.has_obstacle_on_left():
                    column -= 1
                    direction = "<"
                elif not self.has_obstacle_on_top():
                    row -= 1
                    direction = "^"
                elif self.has_obstacle_on_right():
                    return False
                else:
                    column += 1
                    direction = ">"

        if self.set_guard_on(direction, row, column):
            return True
        else:
            return False
        
    def count_visits(self) -> int:
        return sum(line.count("X") for line in self.data)

def main():
    data = read_all_lines("./src/day6-input.txt")
    room = Room(data)
    guard_position = room.find_guard_position()

    while room.move_guard():
        pass

    print("Visits: ", room.count_visits())
    print(guard_position)

if __name__ == "__main__":
    main()