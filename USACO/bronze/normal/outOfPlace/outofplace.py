import sys
sys.stdin = open("outofplace.in", "r")
sys.stdout = open("outofplace.out", "w")

n = int(input())

heights = []

for _ in range(n):
    heights.append(int(input()))

correct = sorted(heights)

different = 0

for i in range(n):
    if heights[i] != correct[i]:
        different += 1

print(different-1)