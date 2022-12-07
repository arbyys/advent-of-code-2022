from aocd import get_data

DISTINCT_LENGTH = 14

data = get_data(day=6, year=2022)

for index in range(DISTINCT_LENGTH, len(data)):
    current = data[index-DISTINCT_LENGTH:index]
    if (len(current) == len(set(current))):
        print(index)
        break
