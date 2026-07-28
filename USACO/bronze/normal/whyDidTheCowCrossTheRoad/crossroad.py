import sys
sys.stdin = open("crossroad.in", "r")
sys.stdout = open("crossroad.out", "w")

n = int(input())

last_side = [-1] * 11
crossings = 0

for _ in range(n):
    cow, side = map(int, input().split())
    if last_side[cow] == -1:
        last_side[cow] = side
    else:
        if last_side[cow] != side:
            crossings += 1
            last_side[cow] = side
print(crossings)
