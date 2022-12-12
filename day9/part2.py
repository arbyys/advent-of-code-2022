from aocd import get_data

data = get_data(day=9, year=2022)
data = data.splitlines()

with open("template/input.txt") as file:
    data = [line.rstrip("\n") for line in file]


def vis(i, j):
    for x in range(6):
        for y in range(6):
            found = False
            for z in range(len(i)):
                if (i[z] == x and j[z] == y):
                    if (z == 0):
                        print("H", end="")
                    else:
                        print(z, end="")
                    found = True
                    break
            if (not found):
                print(".", end="")
        print()
    print("\n\n")


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


i = [5] * 10
j = [0] * 10


visited = [[i[9], j[9]]]
lastDirection = ""

for instruction in data:
    direction, length = instruction.split(" ")
    for current in range(int(length)):
        i[0], j[0] = move(i[0], j[0], direction)
        for index in range(1, 10):
            if (i[index] == i[index-1] and j[index] == j[index-1]):
                continue
            if (not isAdjacent(i[index-1], j[index-1], i[index], j[index])):
                i[index], j[index] = follow(i[index], j[index], lastDirection)
                if (index == 9 and [i[index], j[index]] not in visited):
                    visited.append([i[index], j[index]])

            else:
                if (index == 1):
                    lastDirection = getCurrentAdjacent(
                        i[index-1], j[index-1], i[index], j[index])
                    print("1changing to: ", lastDirection)
        if (index == 1 and isAdjacent(i[index-1], j[index-1], i[index], j[index])):
            lastDirection = getCurrentAdjacent(
                i[index-1], j[index-1], i[index], j[index])
            print("2changing to: ", lastDirection)
        vis(i, j)


print(visited)
print(len(visited))
