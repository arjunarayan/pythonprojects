import sys
sys.stdin = open("lb.in", "r")
sys.stdout = open("lb.out", "w")

n, B = map(int, input().split())

cows = []

for _ in range(n):
    x, y = map(int, input().split())
    cows.append([x, y])




x_fences = []
y_fences = []

for x, y in cows:
    x_fences.append(x + 1)
    y_fences.append(y + 1)

answer = n

for a in x_fences:
    for b in y_fences:
        top_left = 0
        top_right = 0
        bottom_left = 0
        bottom_right = 0
        for x, y in cows:
            if x < a and y < b:
                bottom_left += 1
            elif x < a and y > b:
                top_left += 1
            elif x > a and y < b:
                bottom_right += 1
            else:
                top_right += 1
        worst = max(top_left, top_right, bottom_left, bottom_right)
        answer = min(answer, worst)

print(answer)
