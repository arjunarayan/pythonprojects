import sys

sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")
m, n = map(int, input().split(" "))
r_limits = []
b_speeds = []


for _ in range(m):
    distance, limit = map(int, input().split(" "))
    for _ in range(distance):
        r_limits.append(limit)

for _ in range(n):
    distance, speed = map(int, input().split(" "))
    for _ in range(distance):
        b_speeds.append(speed)

max_speeding = 0
for i in range(100):
    if b_speeds[i] > r_limits[i]:
        max_speeding = max(max_speeding, b_speeds[i] - r_limits[i])
print(max_speeding)
