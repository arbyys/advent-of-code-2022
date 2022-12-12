from aocd import get_data

data = get_data(day=10, year=2022)
data = data.splitlines()

x = 1
total = 0
allowed = range(20, 221, 40)


def cycleReport(cycle, x):
    global allowed, total
    if (cycle in allowed):
        total += cycle*x


cycle = 1
for line in data:
    unpack = line.split(" ")
    if (len(unpack) == 1):
        unpack.append(None)
    instruction, value = unpack

    if (value != None):
        cycle += 1
        cycleReport(cycle, x)
        cycle += 1
        x += int(value)
        cycleReport(cycle, x)
    else:
        cycle += 1
        cycleReport(cycle, x)

print(total)
