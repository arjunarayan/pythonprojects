import sys
sys.stdin = open('milkMix.in', 'r')
sys.stdout = open('milkMix.out', 'w')
lines = sys.stdin.readlines()

n = len(lines)
c = []
m = []
for i in range(n):
    ci, mi = map(int, lines[i].split())
    c.append(ci)
    m.append(mi)

for i in range(0, 100):
    bucket1 = i % n
    bucket2 = (i + 1) % n
    amt = min(m[bucket1], c[bucket2] - m[bucket2])
    m[bucket1] -= amt
    m[bucket2] += amt

for i in range(n):
    print(m[i])