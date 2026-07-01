import sys
sys.stdin = open("triangles.in", "r")
sys.stdout = open("triangles.out", "w")


n = int(input())
points = []

for _ in range(n):
    points.append(list(map(int, input().split())))

answer = 0

for corner in points:
    x, y = corner
    for horizontal_point in points:
        for vertical_point in points:
            if horizontal_point[1] == y and vertical_point[0] == x:
                horizontal = abs(horizontal_point[0] - x)
                vertical = abs(vertical_point[1] - y)
                answer = max(answer, horizontal * vertical)
print(answer)