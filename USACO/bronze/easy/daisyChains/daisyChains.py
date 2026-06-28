import sys
sys.stdin = open("daisyChains.in", "r")
sys.stdout = open("daisyChains.out", "w")

n = int(input())
flowers = list(map(int, input().split()))

answer = 0

for start in range(n):
    for end in range(start, n):
        photo = flowers[start:end + 1]
        total = sum(photo)
        length = len(photo)
        for flower in photo:
            if flower * length == total:
                answer += 1
                break
print(answer)