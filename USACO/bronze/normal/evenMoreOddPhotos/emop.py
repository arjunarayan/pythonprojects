import sys
sys.stdin = open("emop.in", "r")
sys.stdout = open("emop.out", "w")

n = int(input())
cows = list(map(int, input().split()))

even = 0
odd = 0

for cow in cows:
    if cow % 2 == 0:
        even += 1
    else:
        odd += 1

while odd > even:
    odd -= 2
    even += 1

if even > odd + 1:
    print(2 * odd + 1)
else:
    print(even + odd)