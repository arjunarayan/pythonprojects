def teleport(a, b, x, y):
    distance_without_teleporter = abs(a-b)
    distance_one = abs(a-y) + abs(b-x)
    distance_two = abs(a-x) + abs(b-y)
    return min(distance_one, distance_two, distance_without_teleporter)



print(teleport(3, 10, 8, 2))