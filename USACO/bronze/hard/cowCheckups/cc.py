import sys
sys.stdin = open("cc.in", "r")
sys.stdout = open("cc.out", "w")

import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

base = 0

for i in range(n):
    if a[i] == b[i]:
        base += 1

answer = [0] * (n + 1)

answer[base] += n

for center in range(n):
    current = base
    left = center - 1
    right = center + 1

    while left >= 0 and right < n:
        if a[left] == b[left]:
            current -= 1
        if a[right] == b[right]:
            current -= 1

        if a[left] == b[right]:
            current += 1
        if a[right] == b[left]:
            current += 1

        answer[current] += 1

        left -= 1
        right += 1

for center in range(n - 1):
    current = base
    left = center
    right = center + 1

    while left >= 0 and right < n:
        if a[left] == b[left]:
            current -= 1
        if a[right] == b[right]:
            current -= 1

        if a[left] == b[right]:
            current += 1
        if a[right] == b[left]:
            current += 1

        answer[current] += 1

        left -= 1
        right += 1

print("\n".join(map(str, answer)))