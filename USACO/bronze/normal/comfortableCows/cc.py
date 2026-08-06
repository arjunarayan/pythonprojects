import sys
sys.stdin = open("cc.in", "r")
sys.stdout = open("cc.out", "w")

data = sys.stdin.buffer.read().split()
idx = 0

n = int(data[idx])
idx += 1

cows = set()
comfortable = set()

directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]

def is_comfortable(x, y):
    if (x, y) not in cows:
        return False

    count = 0

    for dx, dy in directions:
        if (x + dx, y + dy) in cows:
            count += 1

    return count == 3


out = []

for _ in range(n):
    x = int(data[idx])
    y = int(data[idx + 1])
    idx += 2

    cows.add((x, y))

    check_positions = [(x, y)]

    for dx, dy in directions:
        check_positions.append((x + dx, y + dy))

    for pos in check_positions:
        px, py = pos

        if pos in comfortable:
            comfortable.remove(pos)

        if is_comfortable(px, py):
            comfortable.add(pos)

    out.append(str(len(comfortable)))

print("\n".join(out))