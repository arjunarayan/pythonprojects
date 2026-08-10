import sys
sys.stdin = open("bb.in", "r")
sys.stdout = open("bb.out", "w")

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

area = (x2 - x1) * (y2 - y1)

covered = 0

corners = [
    (x1, y1),
    (x1, y2),
    (x2, y1),
    (x2, y2)
]

for x, y in corners:
    if x3 <= x <= x4 and y3 <= y <= y4:
        covered += 1

if covered <= 1:
    print(area)

elif covered == 4:
    print(0)

else:
    overlap_width = min(x2, x4) - max(x1, x3)
    overlap_height = min(y2, y4) - max(y1, y3)

    overlap_area = overlap_width * overlap_height

    print(area - overlap_area)