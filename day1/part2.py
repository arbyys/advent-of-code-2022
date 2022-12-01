from aocd import get_data

data = get_data(day=1, year=2022)
data = data.splitlines()

max = -1
result = []
current = 0
for i in data:
    if (i == ""):
        result.append(current)
        current = 0
        continue
    i = int(i)
    current += i

result.sort(reverse=True)
print(result[0] + result[1] + result[2])
