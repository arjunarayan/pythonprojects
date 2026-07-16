import sys
sys.stdin = open("majorityOpinion.in", "r")
sys.stdout = open("majorityOpinion.out", "w")
t = int(input())

for _ in range(t):
    n = int(input())
    hay = list(map(int, input().split()))
    possible = set()

    for i in range(n):
        for j in range(i + 1, min(n, i + 3)):
            if hay[i] == hay[j]:
                possible.add(hay[i])
    if len(possible) == 0:
        print(-1)
    else:
        print(*sorted(possible))