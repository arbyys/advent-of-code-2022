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
    trees = 0

    match direction:
        case Direction.TOP:
            while(current_i > 0):
                trees += 1
                current_i -= 1
                if(data[current_i][current_j] >= startElement):
                    return trees
        case Direction.RIGHT:
            while(current_j < len(data[0])-1):
                trees += 1
                current_j += 1
                if(data[current_i][current_j] >= startElement):
                    return trees
        case Direction.BOTTOM:
            while(current_i < len(data)-1):
                trees += 1
                current_i += 1
                if(data[current_i][current_j] >= startElement):
                    return trees
        case Direction.LEFT:
            while(current_j > 0):
                trees += 1
                current_j -= 1
                if(data[current_i][current_j] >= startElement):
                    return trees
    return trees


def calculateScenic(i, j):
    total = 1
    for direction in Direction:
        treesUntilBlock = goInDirection(i, j, direction)
        total *= treesUntilBlock
    return total


best = -1

for i, row in enumerate(data):
    for j, col in enumerate(row):
        currentItem = data[i][j]

        for direction in Direction:
            result = calculateScenic(i, j)
            if (result > best):
                best = result

print(best)
