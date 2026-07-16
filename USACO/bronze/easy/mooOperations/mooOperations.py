import sys
sys.stdin = open("mooOperations.in", "r")
sys.stdout = open("mooOperations.out", "w")


q = int(input())

for _ in range(q):
    s = input().strip()
    best = float("inf")

    for i in range(len(s) - 2):
        sub = s[i:i + 3]
        if sub[1] == "O":
            changes = 0

            if sub[0] != "M":
                changes += 1

            if sub[2] != "O":
                changes += 1
            total = len(s) - 3 + changes
            best = min(best, total)
    if best == float("inf"):
        print(-1)
    else:
        print(best)