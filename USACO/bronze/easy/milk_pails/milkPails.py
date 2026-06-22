import sys
sys.stdin = open("milkPails.in", "r")
sys.stdout = open("milkPails.out", "w")

x, y, m = map(int, input().split())

maxTotal = 0
xCount = m // x
yCount = m // y

for i in range(xCount+1):
    for j in range(yCount+1):
        total = i * x + y * j
        if total <= m:
            maxTotal = max(maxTotal, total)
print(maxTotal)