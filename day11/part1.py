from enum import Enum

from aocd import get_data

data = get_data(day=11, year=2022)
data = data.splitlines()
# data = [*map(int, data)]

NUMBER_OF_ROUNDS = 20


class Monkey:
    def __init__(self, inventory, operation, divisable, truePass, falsePass):
        self.inventory = inventory
        self.operation = operation
        self.divisable = divisable
        self.truePass = truePass
        self.falsePass = falsePass
        self.inspectCount = 0

    def __str__(self):
        return "Starting items: {}\n\tOperation: {}\n\tTest: divisible by {}\n\t\tIf true: throw to monkey {}\n\t\tIf false: throw to monkey {}".format(
            ", ".join(map(str, self.inventory)), str(self.operation), str(self.divisable), str(self.truePass), str(self.falsePass))

    def inspect(self, old):
        new = eval(self.operation)
        self.inspectCount += 1
        return new

    def whoToPassItemTo(self, value):
        if (value % self.divisable == 0):
            return self.truePass
        else:
            return self.falsePass

    def removeItems(self):
        self.inventory = []

    def addItem(self, value):
        self.inventory.append(value)


group = {}
for index, line in enumerate(data):
    line = line.lstrip(" ").rstrip(" ")
    if ("Starting items" in line):
        startingItems = [*map(int, line.split(": ")[1].split(", "))]
    elif ("Operation" in line):
        operation = line.split("new = ")[1]
    elif ("Test" in line):
        divisable = int(line.split("divisible by ")[1])
    elif ("If true" in line):
        truePass = int(line.split("throw to monkey ")[1])
    elif ("If false" in line):
        falsePass = int(line.split("throw to monkey ")[1])
    elif ("Monkey " in line):
        monkeyNum = int(line.split("Monkey ")[1].rstrip(":"))
    if (line == "" or index == len(data)-1):
        currentMonkey = Monkey(startingItems, operation,
                               divisable, truePass, falsePass)
        group[monkeyNum] = currentMonkey

for round in range(NUMBER_OF_ROUNDS):
    for monkeyNumber, monkey in group.items():
        for item in monkey.inventory:
            worryLevel = monkey.inspect(item) // 3
            newMonkey = monkey.whoToPassItemTo(worryLevel)
            group[newMonkey].addItem(worryLevel)
        monkey.removeItems()

all = []
for key, monkey in group.items():
    all.append(monkey.inspectCount)
    print("Monkey {} inspected items {} times".format(key, monkey.inspectCount))

all.sort(reverse=True)
print(all[0]*all[1])
