import sys
sys.stdin = open("th.in", "r")
sys.stdout = open("th.out", "w")

n = int(input())
log = list(map(int, input().split()))

if log[0] > 0:
    print(-1)
else:
    log[0] = 0

bad = False

for i in range(n):
    if log[i] != -1:
        days_since = log[i]

        for back in range(days_since + 1):
            index = i - back
            needed_value = days_since - back

            if index < 0:
                bad = True
            elif log[index] != -1 and log[index] != needed_value:
                bad = True
            else:
                log[index] = needed_value

if bad:
    print(-1)
else:
    min_breakouts = 0
    max_breakouts = 0

    for value in log:
        if value == 0:
            min_breakouts += 1
            max_breakouts += 1
        elif value == -1:
            max_breakouts += 1

    print(min_breakouts, max_breakouts)