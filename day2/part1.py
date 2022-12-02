from aocd import get_data

data = get_data(day=2, year=2022)
data = data.splitlines()

def rps(me, opponent):
    if((me == "X" and opponent == "C") or (me == "Y" and opponent == "A") or (me == "Z" and opponent == "B")):
        return True
    elif((me == "X" and opponent == "A") or (me == "Y" and opponent == "B") or (me == "Z" and opponent == "C")):
        return None
    return False

scores = {"X": 1, "Y": 2, "Z": 3}
scores2 = {True: 6, None: 3, False: 0}

total = 0
for item in data:
    item = item.split(" ")
    me = item[1]
    opponent = item[0]
    total += scores[me]

    result = rps(me, opponent)
    total += scores2[result]

print(total)
