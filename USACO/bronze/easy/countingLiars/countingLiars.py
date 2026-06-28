import sys
sys.stdin = open("countingLiars.in", "r")
sys.stdout = open("countingLiars.out", "w")

n = int(input())
statements = []
positions = []
for _ in range(n):
    direction, from_where = input().split()
    from_where = int(from_where)
    statements.append([direction, from_where])
    positions.append(from_where)

answer = n

for bessie_position in positions:
    liars = 0

    for direction, from_where in statements:
        if direction == "G" and bessie_position < from_where:
            liars += 1

        if direction == "L" and bessie_position > from_where:
            liars += 1
    answer = min(answer, liars)

print(answer)