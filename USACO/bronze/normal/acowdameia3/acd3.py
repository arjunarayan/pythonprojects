import sys
sys.stdin = open("acd.in", "r")
sys.stdout = open("acd.out", "w")
input = sys.stdin.readline

n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(input().strip())

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

pairs = set()
answer = 0

for r in range(n):
    for c in range(m):
        if grid[r][c] == "G":
            cows = []

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "C":
                    cows.append((nr, nc))

            if len(cows) > 2:
                answer += 1

            elif len(cows) == 2:
                cows.sort()
                pairs.add((cows[0], cows[1]))

print(answer + len(pairs))