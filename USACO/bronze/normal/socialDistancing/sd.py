import sys
sys.stdin = open("sd.in", "r")
sys.stdout = open("sd.out", "w")

n = int(input())
stalls = input().strip()

ones = []

for i in range(n):
    if stalls[i] == "1":
        ones.append(i)

if len(ones) == 0:
    print(n - 1)
    exit()
current_min = n

for i in range(len(ones) - 1):
    distance = ones[i + 1] - ones[i]
    current_min = min(current_min, distance)

single_scores = []

single_scores.append(ones[0])

for i in range(len(ones) - 1):
    distance = ones[i + 1] - ones[i]
    single_scores.append(distance // 2)

single_scores.append(n - 1 - ones[-1])

single_scores.sort(reverse=True)

best_two_different_gaps = single_scores[1]

best_same_gap = 0

best_same_gap = max(best_same_gap, ones[0] // 2)

for i in range(len(ones) - 1):
    distance = ones[i + 1] - ones[i]
    best_same_gap = max(best_same_gap, distance // 3)

best_same_gap = max(best_same_gap, (n - 1 - ones[-1]) // 2)

best_new = max(best_two_different_gaps, best_same_gap)

answer = min(current_min, best_new)

print(answer)