import sys
sys.stdin = open("scs.in", "r")
sys.stdout = open("scs.out", "w")

n = int(input())
cows = list(map(int, input().split()))

answer = 0

for i in range(n - 1, 0, -1):
    if cows[i - 1] > cows[i]:
        answer = i
        break

print(answer)