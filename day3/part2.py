from aocd import get_data

data = get_data(day=3, year=2022)
data = data.splitlines()

result = 0


def getPriority(letter):
    if (letter.isupper()):
        return ord(letter) - 38
    else:
        return ord(letter) - 96


for index in range(0, len(data) - 2, 3):
    currentItem = data[index]
    for letter in currentItem:
        if (letter in data[index+1] and letter in data[index+2]):
            result += getPriority(letter)
            break


print(result)
