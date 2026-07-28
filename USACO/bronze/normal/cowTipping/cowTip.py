import sys
sys.stdin = open("cowTip.in", "r")
sys.stdout = open("cowTip.out", "w")

n = int(input())
tipped = []
answer = 0

for _ in range(n):
    tipped.append(list(input().strip()))

for r in range(n - 1, -1, -1):
    for c in range(n - 1, -1, -1):
        if tipped[r][c] == "1":
            answer += 1
            for i in range(r + 1):
                for j in range(c + 1):
                    if tipped[i][j] == "1":
                        tipped[i][j] = "0"
                    else:
                        tipped[i][j] = "1"
print(answer)