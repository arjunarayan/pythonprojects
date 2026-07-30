import sys
sys.stdin =open("maximizingProductivity.in", "r")
sys.stdout =open("maximizingProductivity.out", "w")

import sys

data = sys.stdin.buffer.read().split()
idx = 0

n = int(data[idx])
q = int(data[idx + 1])
idx += 2

c = []
for _ in range(n):
    c.append(int(data[idx]))
    idx += 1

t = []
for _ in range(n):
    t.append(int(data[idx]))
    idx += 1

limits = []

for i in range(n):
    limits.append(c[i] - t[i])

limits.sort(reverse=True)

out = []

for _ in range(q):
    V = int(data[idx])
    S = int(data[idx + 1])
    idx += 2

    if limits[V - 1] > S:
        out.append("YES")
    else:
        out.append("NO")

print("\n".join(out))
