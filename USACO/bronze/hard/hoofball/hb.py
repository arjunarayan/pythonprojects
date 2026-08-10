import sys
sys.stdin = open("hb.in", "r")
sys.stdout = open("hb.out", "w")

n = int(input())
positions = list(map(int, input().split()))

positions.sort()

target = [-1] * n
incoming = [0] * n

for i in range(n):
    if i == 0:
        target[i] = 1

    elif i == n - 1:
        target[i] = n - 2

    else:
        left_dist = positions[i] - positions[i - 1]
        right_dist = positions[i + 1] - positions[i]

        if left_dist <= right_dist:
            target[i] = i - 1
        else:
            target[i] = i + 1

    incoming[target[i]] += 1
answer = 0

for i in range(n):
    if incoming[i] == 0:
        answer += 1

for i in range(n):
    j = target[i]

    if i < j and target[j] == i:
        if incoming[i] == 1 and incoming[j] == 1:
            answer += 1

print(answer)