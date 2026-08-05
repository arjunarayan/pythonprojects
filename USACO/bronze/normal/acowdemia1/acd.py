import sys
sys.stdin = open("acd.in", "r")
sys.stdout = open("acd.out", "w")

n, L = map(int, input().split())
citations = list(map(int, input().split()))

citations.sort(reverse=True)

h = 0

for i in range(n):
    if citations[i] >= i + 1:
        h = i + 1
target = h + 1

if target <= n:
    needed = 0

    for i in range(target):
        if citations[i] < target:
            needed += 1

    if needed <= L and citations[target - 1] >= target - 1:
        h = target
print(h)