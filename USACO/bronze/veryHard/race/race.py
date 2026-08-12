import sys
sys.stdin = open("race.in", "r")
sys.stdout = open("race.out", "w")

input = sys.stdin.readline

k, n = map(int, input().split())


def max_distance(time, x):
    mid = min(time, (x + time) // 2)

    left = mid * (mid + 1) // 2

    count = time - mid
    right = count * (2 * x + count - 1) // 2

    return left + right


for _ in range(n):
    x = int(input())

    low = 1
    high = k

    while low < high:
        mid = (low + high) // 2

        if max_distance(mid, x) >= k:
            high = mid
        else:
            low = mid + 1

    print(low)