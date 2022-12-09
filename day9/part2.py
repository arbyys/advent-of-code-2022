from aocd import get_data

data = get_data(day=9, year=2022)
data = data.splitlines()


def isAdjacent(head_i, head_j, tail_i, tail_j):
    i = abs(head_i - tail_i)
    j = abs(head_j - tail_j)
    return (i <= 1 and j <= 1)


def move(i, j, direction):
    if ("U" == direction or "D" == direction):
        i += 1 if "D" == direction else -1
    elif ("R" == direction or "L" == direction):
        j += 1 if "R" == direction else -1
    return i, j


def follow(i, j, direction):
    if ("U" == direction or "D" == direction):
        i += -1 if "D" == direction else +1
    elif ("R" == direction or "L" == direction):
        j += -1 if "R" == direction else 1

    elif ("UR" == direction or "LD" == direction):
        i += -1 if "LD" == direction else 1
        j += 1 if "LD" == direction else -1
    elif ("RD" == direction or "UL" == direction):
        i += -1 if "RD" == direction else 1
        j += -1 if "RD" == direction else 1
    return i, j


def getCurrentAdjacent(head_i, head_j, tail_i, tail_j):
    if (tail_i - head_i == 1 and head_j == tail_j):
        return "D"
    elif (tail_i == head_i and tail_j - head_j == 1):
        return "R"
    elif (tail_i - head_i == -1 and head_j == tail_j):
        return "U"
    elif (tail_i == head_i and tail_j - head_j == -1):
        return "L"
    elif (tail_i - head_i == -1 and tail_j - head_j == 1):
        return "UR"
    elif (tail_i - head_i == 1 and tail_j - head_j == 1):
        return "RD"
    elif (tail_i - head_i == 1 and tail_j - head_j == -1):
        return "LD"
    elif (tail_i - head_i == -1 and tail_j - head_j == -1):
        return "UL"


head_i = 0
head_j = 0

tail_i = 0
tail_j = 0

visited = [[tail_i, tail_j]]
lastDirection = ""

for instruction in data:
    direction, length = instruction.split(" ")
    for i in range(int(length)):
        head_i, head_j = move(head_i, head_j, direction)
        if (not isAdjacent(head_i, head_j, tail_i, tail_j)):
            tail_i, tail_j = follow(tail_i, tail_j, lastDirection)
            if ([tail_i, tail_j] not in visited):
                visited.append([tail_i, tail_j])
            if (isAdjacent(head_i, head_j, tail_i, tail_j)):
                lastDirection = getCurrentAdjacent(
                    head_i, head_j, tail_i, tail_j)

        else:
            lastDirection = getCurrentAdjacent(head_i, head_j, tail_i, tail_j)


print(len(visited))
