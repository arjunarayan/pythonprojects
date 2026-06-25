import sys
sys.stdin = open("mowingTheField.in", "r")
sys.stdout = open("mowingTheField.out", "w")

n=int(input())
x=0
y=0
time=0
visited = {
    (0,0):0
}
answer = float("inf")

for _ in range(n):
    direction, steps = input().split()
    steps = int(steps)
    for _ in range(steps):
        time += 1
        if direction == "W":
            x -= 1
        elif direction == "E":
            x += 1
        elif direction == "S":
            y -= 1
        elif direction == "N":
            y += 1
        if (x, y) in visited:
            gap = time - visited[(x, y)]
            answer = min(answer, gap)
        visited[(x, y)] = time

if answer == float("inf"):
    print(-1)
else:
    print(answer)