import sys
sys.stdin = open("hps.in", "r")
sys.stdout = open("hps.out", "w")
n = int(input())

games = []
for _ in range(n):
    games.append(list(map(int, input().split())))

wins1 = {(1, 2), (2, 3), (3, 1)}

score1 = 0

for game in games:
    first = game[0]
    second = game[1]

    if (first, second) in wins1:
        score1 += 1


wins2 = {(1, 3), (3, 2), (2, 1)}

score2 = 0

for game in games:
    first = game[0]
    second = game[1]

    if (first, second) in wins2:
        score2 += 1


print(max(score1, score2))