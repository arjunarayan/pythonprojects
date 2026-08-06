import sys
sys.stdin = open("cf.in", "r")
sys.stdout = open("cf.out", "r")

t = int(input())

for _ in range(t):
    path = input().strip()

    x = 0
    y = 0
    area = 0
    for move in path:
        new_x = x
        new_y = y

        if move == "N":
            new_y += 1
        elif move == "S":
            new_y -= 1
        elif move == "E":
            new_x += 1
        elif move == "W":
            new_x -= 1

        area += x * new_y - y * new_x

        x = new_x
        y = new_y
    if area < 0:
        print("CW")
    else:
        print("CCW")
