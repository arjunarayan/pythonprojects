import sys
sys.stdin = open("as.in", "r")
sys.stdout = open("as.out", "w")
input1 = sys.stdin.readline

t = int(input1())

for _ in range(t):
    n, A, B = map(int, input1().split())

    grid = []
    for _ in range(n):
        grid.append(input1().strip())

    has_star = [[False] * n for _ in range(n)]
    bad = False

    for r in range(n):
        for c in range(n):
            if grid[r][c] == "B":
                prev_r = r - B
                prev_c = c - A

                if prev_r < 0 or prev_c < 0:
                    bad = True
                else:
                    has_star[r][c] = True
                    has_star[prev_r][prev_c] = True

    for r in range(n):
        for c in range(n):
            if grid[r][c] == "W":
                if has_star[r][c]:
                    bad = True

            elif grid[r][c] == "G":
                if has_star[r][c]:
                    continue

                prev_r = r - B
                prev_c = c - A

                if prev_r >= 0 and prev_c >= 0 and has_star[prev_r][prev_c]:
                    continue

                has_star[r][c] = True

    if bad:
        print(-1)
    else:
        answer = 0

        for r in range(n):
            for c in range(n):
                if has_star[r][c]:
                    answer += 1

        print(answer)

