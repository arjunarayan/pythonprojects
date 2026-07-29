import sys
sys.stdin = open("hps1.in", "r")
sys.stdout = open("hps1.out", "w")

n, m = map(int, input().split())

beats = [[False] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = input().strip()

    for j in range(1, i + 1):
        result = row[j - 1]

        if result == "W":
            beats[i][j] = True
        elif result == "L":
            beats[j][i] = True
for _ in range(m):
    s1, s2 = map(int, input().split())

    good = 0

    for symbol in range(1, n + 1):
        if beats[symbol][s1] and beats[symbol][s2]:
            good += 1

    print(n * n - (n - good) * (n - good))