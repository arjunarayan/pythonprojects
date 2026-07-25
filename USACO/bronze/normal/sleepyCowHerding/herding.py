import sys
sys.stdin = open("herding.in", "r")
sys.stdout = open("herding.out", "w")
positions = sorted(list(map(int, input().split())))

a = positions[0]
b = positions[1]
c = positions[2]

gap1 = b - a
gap2 = c - b

if gap1 == 1 and gap2 == 1:
    min_moves = 0
elif gap1 == 2 or gap2 == 2:
    min_moves = 1
else:
    min_moves = 2
print(f"{min_moves}\n{max(gap1, gap2)-1}")