import sys
sys.stdin = open("ac.in", "r")
sys.stdout = open("ac.out", "w")

n = int(input())

bales = []

for _ in range(n):
    bales.append(int(input()))

bales.sort()

def explode_left(start):
    power = 1
    current = start

    while True:
        next_bale = current

        while next_bale > 0 and bales[current] - bales[next_bale - 1] <= power:
            next_bale -= 1

        if next_bale == current:
            break

        current = next_bale
        power += 1

    return start - current

def explode_right(start):
    power = 1
    current = start

    while True:
        next_bale = current

        while next_bale < n - 1 and bales[next_bale + 1] - bales[current] <= power:
            next_bale += 1

        if next_bale == current:
            break

        current = next_bale
        power += 1

    return current - start
answer = 0

for start in range(n):
    total = explode_left(start) + 1 + explode_right(start)
    answer = max(answer, total)

print(answer)