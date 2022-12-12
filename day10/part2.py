from aocd import get_data

data = get_data(day=10, year=2022)
data = data.splitlines()

x = 1
allowed = range(20, 221, 40)

display = [[""]*40 for i in range(6)]


def cycleReport(cycle, x):
    if (cycle > 240):
        return
    global display
    CRT = cycle - 1
    row = CRT // 40
    if (abs(CRT - row*40-x) <= 1):
        display[row][CRT-row*40] = "||"
    else:
        display[row][CRT-row*40] = "  "


cycle = 1
for line in data:
    cycleReport(cycle, x)
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

for i in display:
    for z in i:
        print(z, end="")
    print("")
