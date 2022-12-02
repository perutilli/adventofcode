"""
A, X -> rock
B, Y -> paper
C, Z -> scissors

PART 1

A beats Z loses to Y
B beats X loses to Z
C beats Y loses to X
"""
points = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

eq = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

def turn_points(p1: str, p2: str) -> int:
    if eq[p1] == p2:
        return points[p2] + 3
    if p1 == "A" and p2 == "Z" or p1 == "B" and p2 == "X" or p1 == "C" and p2 == "Y": # p1 wins
        return points[p2]
    if p1 == "A" and p2 == "Y" or p1 == "B" and p2 == "Z" or p1 == "C" and p2 == "X": # p2 wins
        return points[p2] + 6
    raise Exception("Invalid input")

total = 0

with open("input.txt", "r") as file_in:
    for line in file_in.readlines():
        total += turn_points(line[0], line[2])

print(total)

"""
PART 2

X means p2 wins
Y means draw
Z means p1 wins

points are calculated from p2's perspective:
X = 6 + 1 for p2 = rock, 6 + 2 for p2 = paper, 6 + 3 for p2 = scissors
Y = 3 + 1 for p2 = rock, 3 + 2 for p2 = paper, 3 + 3 for p2 = scissors
Z = 0 + 1 for p2 = rock, 0 + 2 for p2 = paper, 0 + 3 for p2 = scissors
"""

points = {
    "A X": 8, # p1 = rock, p2 = paper
    "B X": 9, # p1 = paper, p2 = scissors
    "C X": 7, # p1 = scissors, p2 = rock
    "A Y": 4, # p1 = rock, p2 = rock
    "B Y": 5, # p1 = paper, p2 = paper
    "C Y": 6, # p1 = scissors, p2 = scissors
    "A Z": 3, # p1 = rock, p2 = scissors
    "B Z": 1, # p1 = paper, p2 = rock
    "C Z": 2, # p1 = scissors, p2 = paper
}

# added because I was too lazy to change the code
translations = {
    "X": "Z",
    "Y": "Y",
    "Z": "X"
}

total = 0

with open("input.txt", "r") as file_in:
    for line in file_in.readlines():
        total += points[line[0] + " " + translations[line[2]]]

print(total)
