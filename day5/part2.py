import re

from aocd import get_data

data = get_data(day=5, year=2022)
data = data.splitlines()


def normalizeListElements(arr):
    for index, item in enumerate(arr):
        if (index >= 3 and item == "" and arr[index-1] == "" and arr[index-2] == "" and arr[index-3] == ""):
            del arr[index-1], arr[index-2], arr[index-3]
    return arr


def splitData(data):
    for index, item in enumerate(data):
        if (item == ""):
            setup = data[:index-1]
            input = data[index+1:]
            break
    return setup, input


setup, input = splitData(data)

for index, line in enumerate(setup):
    normalized = normalizeListElements(line.split(" "))
    if (index == 0):
        stacks = [[] for i in range(len(normalized))]
    for j_index, item in enumerate(normalized):
        if (item != ""):
            stacks[j_index].insert(0, item)

for line in input:
    nums = [*map(int, re.findall(r'\d+', line))]
    tempArray = []
    for i in range(nums[0]):
        retrieved = stacks[nums[1]-1].pop()
        tempArray.insert(0, retrieved)
    for item in tempArray:
        stacks[nums[2]-1].append(item)


message = ""
for i in stacks:
    message += list(i.pop())[1]
print(message)
