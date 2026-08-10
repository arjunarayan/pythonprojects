import sys
sys.stdin = open("ga.in", "r")
sys.stdout = open("ga.out", "w")

n = int(input())

animals = []

for _ in range(n):
    line = input().split()
    characteristics = set(line[2:])
    animals.append(characteristics)

answer = 0

for i in range(n):
    for j in range(i + 1, n):
        shared = 0

        for trait in animals[i]:
            if trait in animals[j]:
                shared += 1

        answer = max(answer, shared + 1)

print(answer)