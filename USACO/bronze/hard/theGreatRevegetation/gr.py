import sys
sys.stdin = open("gr.in", "r")
sys.stdout = open("gr.out", "w")

n, m = map(int, input().split())

neighbors = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    neighbors[a].append(b)
    neighbors[b].append(a)


grass = [0] * (n + 1)

for pasture in range(1, n + 1):
    for grass_type in range(1, 5):
        ok = True

        for neighbor in neighbors[pasture]:
            if grass[neighbor] == grass_type:
                ok = False

        if ok:
            grass[pasture] = grass_type
            break

answer = ""

for pasture in range(1, n + 1):
    answer += str(grass[pasture])

print(answer)