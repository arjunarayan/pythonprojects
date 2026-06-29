import sys
sys.stdin = open("cowGymnastics.in", "r")
sys.stdout = open("cowGymnastics.out", "w")

K, N = map(int, input().split())
sessions = []
for _ in range(K):
    sessions.append(list(map(int, input().split())))

answer = 0

for cow1 in range(1, N + 1):
    for cow2 in range(cow1 + 1, N + 1):
        cow1_better = True
        cow2_better = True
        for session in sessions:
            if session.index(cow1) > session.index(cow2):
                cow1_better = False

            if session.index(cow2) > session.index(cow1):
                cow2_better = False
        if cow1_better or cow2_better:
            answer += 1

print(answer)
