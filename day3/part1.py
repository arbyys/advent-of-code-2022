from aocd import get_data

data = get_data(day=3, year=2022)
data = data.splitlines()

result = 0


def getPriority(letter):
    if (letter.isupper()):
        return ord(letter) - 38
    else:
        return ord(letter) - 96


for item in data:
    firstHalf = item[:len(item) // 2]
    secondHalf = item[len(item) // 2:]
    for letter in firstHalf:
        if (letter in secondHalf):
            result += getPriority(letter)
            break

print(result)
