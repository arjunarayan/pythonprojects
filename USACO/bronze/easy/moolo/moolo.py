import sys
sys.stdin = open("moolo.in", "r")
sys.stdout = open("moolo.out", "w")

n, k = map(int, input().split())
days = list(map(int, input().split()))

answer = k + 1
for i in range(1, n):
    gap = days[i] - days[i - 1]
    answer += min(gap, k + 1)
print(answer)
