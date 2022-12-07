from dataclasses import dataclass

from aocd import get_data

data = get_data(day=7, year=2022)
data = data.splitlines()

MINIMAL_SIZE = 100000
total = 0


class Directory:
    def __init__(self, parent=None):
        self.items = {}
        self.totalSize = 0
        self.parent = parent
        pass

    def addItem(self, name, item):
        self.items[name] = item

    def calculateSize(self):
        global total
        for key, value in self.items.items():
            if (isinstance(value, Directory)):
                value.calculateSize()
                if (value.totalSize <= MINIMAL_SIZE):
                    total += value.totalSize
                self.totalSize += value.totalSize
            else:
                self.totalSize += int(value)


root = Directory()
current = root
del data[0]

for index, line in enumerate(data):
    if (line.startswith("$")):
        command = line.lstrip("$ ").split(" ")
        if (command[0] == "cd"):
            if (command[1] == ".."):
                current = current.parent
            else:
                current = current.items[command[1]]
    else:
        file = line.split(" ")
        if (file[0] == "dir"):
            current.addItem(file[1], Directory(current))
        else:
            current.addItem(file[1], file[0])

root.calculateSize()
print(total)
