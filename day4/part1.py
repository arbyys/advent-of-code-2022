from aocd import get_data

data = get_data(day=4, year=2022)
data = data.splitlines()

counter = 0
for i in data:
    pair1 = [*map(int, i.split(",")[0].split("-"))]
    pair2 = [*map(int, i.split(",")[1].split("-"))]
    if ((pair1[0] <= pair2[0] and pair1[1] >= pair2[1]) or (pair1[0] >= pair2[0] and pair1[1] <= pair2[1])):
        counter += 1

print(counter)
