from aocd import get_data

data = get_data(day=2, year=2022)
data = data.splitlines()

rps_winner = {"A": "Y", "B": "Z", "C": "X"}
rps_draw = {"A": "X", "B": "Y", "C": "Z"}
rps_loser = {"A": "Z", "B": "X", "C": "Y"}

scores = {"X": 1, "Y": 2, "Z": 3}
scores2 = {"Z": 6, "Y": 3, "X": 0}

def getScore(opponent, designated):
    if(designated == "Y"):
        return scores[rps_draw[opponent]]
    elif(designated == "Z"):
        return scores[rps_winner[opponent]]
    elif(designated == "X"):
        return scores[rps_loser[opponent]]

total = 0
for item in data:
    item = item.split(" ")
    designated = item[1]
    opponent = item[0]
    total += scores2[designated]
    total += getScore(opponent, designated)

print(total)