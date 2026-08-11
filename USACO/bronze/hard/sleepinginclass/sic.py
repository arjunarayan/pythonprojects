import sys
sys.stdin = open("sic.in", "r")
sys.stdout = open("sic.out", "w")

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(a)
    if total == 0:
        print(0)
        continue
    for target in range(1, total + 1):
        if total % target != 0:
            continue
        curr_sum = 0
        possible = True
        for x in a:
            curr_sum += x
            if curr_sum == target:
                curr_sum = 0
            elif curr_sum > target:
                possible = False
                break
        if possible:
            groups = total // target
            print(n-groups)
            break