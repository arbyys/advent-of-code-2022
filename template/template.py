from aocd import get_data

data = get_data(day=1, year=2022)
data = data.splitlines()
#data = [*map(int, data)]

print(data)
