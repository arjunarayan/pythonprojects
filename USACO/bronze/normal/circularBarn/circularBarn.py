import sys
sys.stdin = open("circularBarn.in", "r")
sys.stdout = open("circularBarn.out", "w")


n = int(input())
rooms = []

for _ in range(n):
    rooms.append(int(input()))


best_cost = float("inf")

for door in range(n):
    cost = 0
    for distance in range(n):
        room_index = (door+distance) % n
        cost += rooms[room_index] * distance
    best_cost = min(cost, best_cost)
print(best_cost)
