from enum import Enum

from aocd import get_data


class Direction(Enum):
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 4


data = get_data(day=8, year=2022)
data = data.splitlines()
for index, i in enumerate(data):
    data[index] = [*map(int, i)]


def goInDirection(start_i, start_j, direction: Direction):
    global data
    current_i = start_i
    current_j = start_j
    startElement = data[current_i][current_j]

    match direction:
        case Direction.TOP:
            while (current_i > 0):
                current_i -= 1
                if (data[current_i][current_j] >= startElement):
                    return False
        case Direction.RIGHT:
            while (current_j < len(data[0])-1):
                current_j += 1
                if (data[current_i][current_j] >= startElement):
                    return False
        case Direction.BOTTOM:
            while (current_i < len(data)-1):
                current_i += 1
                if (data[current_i][current_j] >= startElement):
                    return False
        case Direction.LEFT:
            while (current_j > 0):
                current_j -= 1
                if (data[current_i][current_j] >= startElement):
                    return False
    return True


total = 0
for i, row in enumerate(data):
    for j, col in enumerate(row):
        currentItem = data[i][j]
        if (i in [0, len(data)-1] or j in [0, len(row)-1]):
            total += 1
            continue

        for direction in Direction:
            if (goInDirection(i, j, direction)):
                total += 1
                break

print(total)
