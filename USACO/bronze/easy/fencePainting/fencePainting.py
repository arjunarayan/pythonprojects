import sys
sys.stdin = open("fencePainting.in", "r")
sys.stdout = open("fencePainting.out", "w")

a, b = map(int, input().split())
c, d = map(int, input().split())

length1 = b - a
length2 = d - c

overlap_start = max(a, c)
overlap_end = min(b, d)

if overlap_start < overlap_end:
    overlap = overlap_end - overlap_start
else:
    overlap = 0
answer = length1 + length2 - overlap
print(answer)