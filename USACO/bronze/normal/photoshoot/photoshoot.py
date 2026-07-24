import sys
sys.stdin = open("photoshoot.in", "r")
sys.stdout = open("photoshoot.out", "w")

n = int(input())
b = list(map(int, input().split()))
for first in range(1, n + 1):
    a = [first]
    for i in range(n - 1):
        next_num = b[i] - a[i]
        a.append(next_num)

    valid = True
    seen = set()

    for num in a:
        if num < 1 or num > n:
            valid = False

        if num in seen:
            valid = False

        seen.add(num)

    if valid:
        print(*a)
        break