import sys


sys.stdin = open("rounding.in", "r")
sys.stdout = open("rounding.out", "w")
read_line = sys.stdin.readline

t = int(read_line())
outputs = []

for _ in range(t):
    n = int(input())
    answer = 0

    low = 45
    high = 49

    while low <= n:
        answer += min(n, high) - low + 1

        low = low * 10 - 5
        high = high * 10 + 9

    outputs.append(str(answer))

print("\n".join(outputs))