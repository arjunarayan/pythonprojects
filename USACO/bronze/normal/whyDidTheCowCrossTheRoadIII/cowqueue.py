import sys
sys.stdin = open("cowqueue.in", "r")
sys.stdout = open("cowqueue.out", "w")

n = int(input())

cow_details = []

for _ in range(n):
    cow_details.append(list(map(int, input().split())))

cow_details.sort()
current_time = 0
for cow in cow_details:
    arrival = cow[0]
    duration = cow[1]
    if current_time < arrival:
        current_time = arrival
    current_time += duration
print(current_time)