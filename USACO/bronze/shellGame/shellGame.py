file_in = open("shellGame.in")
data = file_in.read().split("\n")

n = int(data[0])
moves = []
hiScore = 0
for i in range(0, n):
    a, b, g = map(int, data[i+1].split())
    moves.append((a, b, g))
for pebble_pos in range(1, n+1):
    score = 0
    for a, b, g in moves:
        if pebble_pos == a: pebble_pos = b
        elif pebble_pos == b: pebble_pos = a
        if g == pebble_pos: score += 1
    hiScore = max(score, hiScore)
print(hiScore, file=open("shellGame.out", "w"))