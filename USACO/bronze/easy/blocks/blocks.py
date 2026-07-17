import sys
import itertools
sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")

n = int(input())

blocks = []
for _ in range(4):
    blocks.append(input().strip())

for _ in range(n):
    word = input().strip()
    possible = False

    for order in itertools.permutations([0, 1, 2, 3]):
        works = True

        for i in range(len(word)):
            block_index = order[i]

            if word[i] not in blocks[block_index]:
                works = False
                break
        if works:
            possible = True
            break
    if possible:
        print("YES")
    else:
        print("NO")