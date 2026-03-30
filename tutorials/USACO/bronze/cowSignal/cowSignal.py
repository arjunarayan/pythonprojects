import sys
sys.stdin = open("cowSignal.in", "r")
sys.stdout = open("cowSignal.out", "w")

m, n, k = map(int, input().split(" "))

for _ in range(m):
    curr = ""
    line = input()
    for char in line:
        curr += char * k
    for _ in range(k):
        print(curr)