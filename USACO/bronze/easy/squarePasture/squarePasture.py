import sys
sys.stdin = open("squarePasture.in", "r")

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

leftX = min(x1, x3)
rightX = max(x2, x4)

maxLength = rightX - leftX

bottomY = min(y1, y3)
topY = max(y2, y4)

maxHeight = topY - bottomY

print(max(maxLength, maxHeight) ** 2)