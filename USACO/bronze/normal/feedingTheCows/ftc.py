import sys
sys.stdin = open("ftc.in", "r")
sys.stdout = open("ftc.out", "w")

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    cows = input().strip()

    patches = ["."] * n

    g_cover = -1
    h_cover = -1

    answer = 0

    for i in range(n):
        if cows[i] == "G":
            if i <= g_cover:
                continue

            place = min(i + k, n - 1)

            while patches[place] != ".":
                place -= 1

            patches[place] = "G"
            g_cover = place + k
            answer += 1

        else:
            if i <= h_cover:
                continue

            place = min(i + k, n - 1)

            while patches[place] != ".":
                place -= 1

            patches[place] = "H"
            h_cover = place + k
            answer += 1
    print(answer)
    print("".join(patches))