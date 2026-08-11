import sys
sys.stdin = open("photoshoot.in", "r")
sys.stdout = open("photoshoot.out", "w")

n = int(input())
cows = input().strip()
flips = 0
for i in range(n - 2, -1, -2):
    pair = cows[i:i+2]
    if pair[0] == pair[1]:
        continue
    if flips % 2 == 0:
        if pair == "GH":
            flips += 1
    else:
        if pair == "HG":
            flips += 1

print(flips)