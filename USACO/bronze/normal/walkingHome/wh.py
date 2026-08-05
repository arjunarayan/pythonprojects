import sys
sys.stdin = open("wh.in", "r")
sys.stdout = open("wh.out", "w")

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    grid = []
    for _ in range(n):
        grid.append(input().strip())

    memo = {}

    def dfs(r, c, direction, turns):
        if r >= n or c >= n:
            return 0

        if grid[r][c] == "H":
            return 0

        if r == n - 1 and c == n - 1:
            return 1
        key = (r, c, direction, turns)

        if key in memo:
            return memo[key]

        total = 0

        next_turns = turns
        if direction == "D":
            next_turns += 1

        if next_turns <= k:
            total += dfs(r, c + 1, "R", next_turns)

        next_turns = turns
        if direction == "R":
            next_turns += 1

        if next_turns <= k:
            total += dfs(r + 1, c, "D", next_turns)

        memo[key] = total
        return total

    print(dfs(0, 0, "", 0))