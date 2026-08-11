import sys
sys.stdin = open("ac.in", "r")
sys.stdout = open("ac.out", "w")

n = int(input())
p = list(map(int, input().split()))
t = list(map(int, input().split()))


d = [p[i] - t[i] for i in range(n)]

d.append(0)
d.insert(0, 0)

diffs = 0

for i in range(len(d)-1):
    diffs += abs(d[i] - d[i + 1])
print(diffs//2)