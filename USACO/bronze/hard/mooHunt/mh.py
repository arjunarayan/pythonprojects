import sys
sys.stdin = open("mh.in", "r")
sys.stdout = open("mh.out", "w")

n, k = map(int, input().split())

size = 1 << n
score = [0] * size

for _ in range(k):
    x, y, z = map(int, input().split())

    x -= 1
    y -= 1
    z -= 1

    x_mask = 1 << x
    xy_mask = (1 << x) | (1 << y)
    xz_mask = (1 << x) | (1 << z)
    xyz_mask = (1 << x) | (1 << y) | (1 << z)

    score[x_mask] += 1
    score[xy_mask] -= 1
    score[xz_mask] -= 1
    score[xyz_mask] += 1

for bit in range(n):
    for mask in range(size):
        if mask & (1 << bit):
            score[mask] += score[mask ^ (1 << bit)]

best_score = max(score)
count = 0

for value in score:
    if value == best_score:
        count += 1

print(best_score, count)

