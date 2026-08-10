import sys
sys.stdin = open("leaders.in", "r")
sys.stdout = open("leaders.out", "w")

n = int(input())
breeds = input().strip()
e = list(map(int, input().split()))

for i in range(n):
    e[i] -= 1

first_G = -1
last_G = -1
first_H = -1
last_H = -1

for i in range(n):
    if breeds[i] == "G":
        if first_G == -1:
            first_G = i
        last_G = i

    else:
        if first_H == -1:
            first_H = i
        last_H = i

first_G_leader = e[first_G] >= last_G
first_H_leader = e[first_H] >= last_H

pairs = set()

if first_G_leader and first_H_leader:
    pairs.add((first_G, first_H))

def can_be_pair(g, h):
    g_ok = False
    h_ok = False

    # G leader condition
    if g == first_G and e[g] >= last_G:
        g_ok = True
    if g <= h and e[g] >= h:
        g_ok = True

    # H leader condition
    if h == first_H and e[h] >= last_H:
        h_ok = True
    if h <= g and e[h] >= g:
        h_ok = True

    return g_ok and h_ok

pairs = set()

# Case 1: G leader is the first G
for h in range(n):
    if breeds[h] == "H":
        if can_be_pair(first_G, h):
            pairs.add((first_G, h))

# Case 2: H leader is the first H
for g in range(n):
    if breeds[g] == "G":
        if can_be_pair(g, first_H):
            pairs.add((g, first_H))

print(len(pairs))