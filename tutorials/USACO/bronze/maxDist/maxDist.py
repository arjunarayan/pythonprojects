import math
import sys
sys.stdin = open("maxDist.in", "r")
sys.stdout = open("maxDist.out", "w")
n = int(input())
x = list(map(int, input().split(" ")))
y = list(map(int, input().split(" ")))
ms = 0
for i in range(n):
    for j in range(i+1, n):
        dx = x[i] - x[j]
        dy = y[i] - y[j]
        squared = dx ** 2 + dy ** 2
        squareRoot = math.sqrt(squared)
        ms = max(ms, squareRoot)
print(ms)