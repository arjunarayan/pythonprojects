import sys
sys.stdin = open("bovineGenomics.in", "r")
sys.stdout = open("bovineGenomics.out", "w")



n, m = map(int, input().split())
spotty = []
plain = []
for _ in range(n):
    spotty.append(input().strip())
for _ in range(n):
    plain.append(input().strip())

answer = 0

for pos in range(m):
    spotty_letters = set()
    plain_letters = set()
    for cow in spotty:
        spotty_letters.add(cow[pos])
    for cow in plain:
        plain_letters.add(cow[pos])
    if len(spotty_letters.intersection(plain_letters)) == 0:
        answer += 1
print(answer)
