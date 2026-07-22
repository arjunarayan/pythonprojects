import sys
sys.stdin = open("madScientist.in", "r")
sys.stdout = open("madScientist.out", "w")


n = int(input())
a = input().strip()
b = input().strip()

answer = 0

for i in range(n):
    if a[i] != b[i]:
        if i == 0 or a[i - 1] == b[i - 1]:
            answer += 1

print(answer)