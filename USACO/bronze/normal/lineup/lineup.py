import sys
sys.stdin = open("lineup.in", "r")
sys.stdout = open("lineup.out", "w")
from itertools import permutations
cows = [
    "Beatrice",
    "Belinda",
    "Bella",
    "Bessie",
    "Betsy",
    "Blue",
    "Buttercup",
    "Sue"
]
n = int(input())
rules = []

for _ in range(n):
    words = input().split()
    rules.append([words[0], words[5]])

for order in permutations(cows):
    works = True

    for cow1, cow2 in rules:
        position1 = order.index(cow1)
        position2 = order.index(cow2)
        if abs(position1 - position2) != 1:
            works = False
    if works:
        for cow in order:
            print(cow)
        break