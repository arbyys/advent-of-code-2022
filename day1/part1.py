from aocd import get_data

data = get_data(day=1, year=2022)
data = data.splitlines()

max = -1
current = 0
for i in data:
    if (i == ""):
        if (current > max):
            max = current
        current = 0
        continue
    i = int(i)
    current += i

print(max)
