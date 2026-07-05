import sys
sys.stdin = open("circleCross.in", "r")
sys.stdout = open("circleCross.out", "w")

s = input().strip()
answer = 0

positions = {}

for i in range(len(s)):
    cow = s[i]

    if cow not in positions:
        positions[cow] = []

    positions[cow].append(i)
cows = list(positions.keys())

for i in range(len(cows)):
    for j in range(i + 1, len(cows)):
        cow1 = cows[i]
        cow2 = cows[j]
        a1, a2 = positions[cow1]
        b1, b2 = positions[cow2]
        if a1 < b1 < a2 < b2 or b1 < a1 < b2 < a2:
            answer += 1

print(answer)


