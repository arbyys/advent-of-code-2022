from aocd import get_data

data = get_data(day=1, year=2022)
data = data.splitlines()
#data = [*map(int, data)]

# with open("template/input.txt") as file:
#    data = [line.rstrip() for line in file]

print(data)
