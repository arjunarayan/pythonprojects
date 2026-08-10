import sys
sys.stdin = open("mo.in", "r")
sys.stdout = open("mo.out", "w")

n, m, k = map(int, input().split())

hierarchy = list(map(int, input().split()))

order = [0] * (n + 1)
fixed_position = {}

for _ in range(k):
    cow, pos = map(int, input().split())
    order[pos] = cow
    fixed_position[cow] = pos


if 1 in fixed_position:
    print(fixed_position[1])

elif 1 in hierarchy:
    pos = 1

    for cow in hierarchy:
        if cow in fixed_position:
            pos = fixed_position[cow] + 1

        else:
            while order[pos] != 0:
                pos += 1

            order[pos] = cow
            pos += 1

    for pos in range(1, n + 1):
        if order[pos] == 1:
            print(pos)
            break

else:
    pos = n

    for i in range(m - 1, -1, -1):
        cow = hierarchy[i]

        if cow in fixed_position:
            pos = fixed_position[cow] - 1

        else:
            while order[pos] != 0:
                pos -= 1

            order[pos] = cow
            pos -= 1

    for pos in range(1, n + 1):
        if order[pos] == 0:
            print(pos)
            break

