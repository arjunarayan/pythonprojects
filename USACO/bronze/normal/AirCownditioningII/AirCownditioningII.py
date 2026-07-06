import sys
sys.stdin = open("AirCownditioningII.in", "r")
sys.stdout = open("airCownditioningII.out", "w")


n, m = map(int, input().split())
cows = []
acs = []

for _ in range(n):
    cows.append(list(map(int, input().split())))
for _ in range(m):
    acs.append(list(map(int, input().split())))

answer = float("inf")

for mask in range(2 ** m):
    cooling = [0] * 101
    cost = 0

    for i in range(m):
        if mask & (1 << i):
            start, end, power, ac_cost = acs[i]
            cost += ac_cost
            for stall in range(start, end + 1):
                cooling[stall] += power
    works = True

    for cow_start, cow_end, required in cows:
        for stall in range(cow_start, cow_end + 1):
            if cooling[stall] < required:
                works = False
    if works:
        answer = min(answer, cost)

print(answer)
