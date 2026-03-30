import sys
sys.stdin = open("lostCow.in", "r")
sys.stdout = open("lostCow.out", "w")
x, y = map(int, input().split(" "))

if x == y:
    print(0)
    exit()
dir = 1
distance = 0
step_size = 1
curr = x
while True:
    next_pos = curr + (dir * step_size)
    if curr <= y <= next_pos or curr >= y >= next_pos:
        distance += abs(y-curr)
        break

    else:
        distance += abs(next_pos-curr)
        distance += abs(next_pos-x)
        curr = x
        dir *= -1
        step_size *= 2
print(distance)