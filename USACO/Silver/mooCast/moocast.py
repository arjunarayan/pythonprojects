import sys
sys.stdin = open("moocast.in", "r")
sys.stdout = open("moocast.out", "w")

n = int(input())

cows = []

for _ in range(n):
    x, y, power = map(int, input().split())
    cows.append((x, y, power))

graph = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue

        dx = cows[i][0] - cows[j][0]
        dy = cows[i][1] - cows[j][1]

        if dx * dx + dy * dy <= cows[i][2] * cows[i][2]:
            graph[i].append(j)


def dfs(start):
    visited = [False] * n
    stack = [start]
    visited[start] = True
    count = 0

    while stack:
        current = stack.pop()
        count += 1

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

    return count


best = 0

for start in range(n):
    best = max(best, dfs(start))

print(best)