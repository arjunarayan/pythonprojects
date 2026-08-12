import sys
sys.stdin = open("ss.in", "r")
sys.stdout = open("ss.out", "w")

n, k = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

cows = []

for i in range(n):
    cows.append(i + 1)

cows[a1 - 1:a2] = cows[a1 - 1:a2][::-1]
cows[b1 - 1:b2] = cows[b1 - 1:b2][::-1]

next_pos = [0] * (n + 1)

for i in range(n):
    next_pos[cows[i]] = i + 1

answer = [0] * (n + 1)

visited = [False] * (n + 1)

for start in range(1, n + 1):
    if visited[start]:
        continue

    cycle = []
    current = start

    while not visited[current]:
        visited[current] = True
        cycle.append(current)
        current = next_pos[current]

    steps = k % len(cycle)

    for j in range(len(cycle)):
        new_position = cycle[(j + steps) % len(cycle)]
        cow = cycle[j]
        answer[new_position] = cow

for i in range(1, n + 1):
    print(answer[i])