import sys
sys.stdin = open("reflection.in", "r")
sys.stdout = open("reflection.out", "w")


n, u = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(input().strip()))

def cost(r, c):
    mirror_r = n + 1 - r
    mirror_c = n + 1 - c
    num_hash = 0

    if grid[r - 1][c - 1] == "#":
        num_hash += 1
    if grid[mirror_r - 1][c - 1] == "#":
        num_hash += 1
    if grid[mirror_r - 1][mirror_c - 1] == "#":
        num_hash += 1
    if grid[r - 1][mirror_c - 1] == "#":
        num_hash += 1

    return min(num_hash, 4 - num_hash)

outputs = []

answer = 0
for r in range(1, n // 2 + 1):
    for c in range(n // 2 + 1, n + 1):
        answer += cost(r, c)

outputs.append(str(answer))

for _ in range(u):
    r, c = map(int, input().split())

    rep_r = min(r, n + 1 - r)
    rep_c = max(c, n + 1 - c)

    answer -= cost(rep_r, rep_c)

    if grid[r - 1][c - 1] == "#":
        grid[r - 1][c - 1] = "."
    else:
        grid[r - 1][c - 1] = "#"

    answer += cost(rep_r, rep_c)
    outputs.append(str(answer))

print("\n".join(outputs))