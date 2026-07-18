import sys
sys.stdin = open("justStalling.in", "r")
sys.stdout = open("justStalling.out", "w")

n = int(input())
cow_heights = list(map(int, input().split()))
stall_heights = list(map(int, input().split()))

cow_heights.sort(reverse=True)
stall_heights.sort()

answer = 1

for i in range(n):
    cow = cow_heights[i]
    can_fit = 0

    for stall in stall_heights:
        if stall >= cow:
            can_fit += 1
    choices = can_fit - i
    answer *= choices
print(answer)