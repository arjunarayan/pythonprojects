import sys
sys.stdin = open("drought.in", "r")
sys.stdout = open("drought.out", "w")

t = int(input())

for _ in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    bags = 0

    for i in range(n - 1):

        if h[i + 1] > h[i]:
            diff = h[i + 1] - h[i]

            if i + 2 >= n:
                bags = -1
                break

            h[i + 1] -= diff
            h[i + 2] -= diff
            bags += 2 * diff
            if h[i + 2] < 0:
                bags = -1
                break

        elif h[i] > h[i + 1]:

            if i % 2 == 0:
                bags = -1
                break
            diff = h[i] - h[i + 1]
            bags += (i + 1) * diff
    print(bags)