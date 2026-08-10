import sys
sys.stdin = open("ma.in", "r")
sys.stdout = open("ma.out", "w")

n = int(input())

grid = []

for _ in range(n):
    grid.append(input().strip())

visible = set()

for r in range(n):
    for c in range(n):
        color = grid[r][c]

        if color != "0":
            visible.add(color)

cannot_be_first = set()

for color in visible:
    top = n
    bottom = -1
    left = n
    right = -1

    for r in range(n):
        for c in range(n):
            if grid[r][c] == color:
                top = min(top, r)
                bottom = max(bottom, r)
                left = min(left, c)
                right = max(right, c)

    for r in range(top, bottom + 1):
        for c in range(left, right + 1):
            other_color = grid[r][c]

            if other_color != "0" and other_color != color:
                cannot_be_first.add(other_color)

print(len(visible) - len(cannot_be_first))