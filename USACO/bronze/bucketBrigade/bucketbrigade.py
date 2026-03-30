import sys
sys.stdin = open("bucketbrigade.in", "r")

bx, by , rx, ry , lx, ly = 0,0,0,0,0,0

for y in range(0,10):
    row = input()
    for x in range(0,10):
        if row[x] == "B":
            bx=x
            by = y
        if row[x] == "R":
            rx = x
            ry = y
        if row[x] == "L":
            lx = x
            ly = y
steps = abs(lx-bx) + abs(ly-by)
if ry == by == ly and (bx < rx < lx or bx > rx > lx):
    steps += 2
elif rx == bx == lx and (by < ry < ly or by > ry > ly):
    steps += 2
print(steps - 1, file=open("bucketBrigade.out", "w"))