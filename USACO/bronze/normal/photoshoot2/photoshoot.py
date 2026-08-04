import sys
sys.stdin = open("photoshoot.in", "r")
sys.stdout = open("photoshoot.out", "w")

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

pos_in_b = [0] * (n + 1)

for i in range(n):
    cow = b[i]
    pos_in_b[cow] = i + 1

converted = []

for cow in a:
    converted.append(pos_in_b[cow])

answer = 0
biggest_so_far = 0

for x in converted:
    if x < biggest_so_far:
        answer += 1
    else:
        biggest_so_far = x

print(answer)