import sys
sys.stdin = open("mf.in", "r")
sys.stdout = open("mf.out", "w")

n = int(input())

has_outgoing = [False] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    has_outgoing[a] = True
answer = -1
count = 0

for station in range(1, n + 1):
    if not has_outgoing[station]:
        answer = station
        count += 1

if count == 1:
    print(answer)
else:
    print(-1)
