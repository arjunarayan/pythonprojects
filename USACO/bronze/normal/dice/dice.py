import sys
sys.stdin = open("dice.in", "r")
sys.stdout = open("dice.out", "w")
def beats(die1, die2):
    die1_wins = 0
    die2_wins = 0

    for x in die1:
        for y in die2:
            if x > y:
                die1_wins += 1
            elif y > x:
                die2_wins += 1

    return die1_wins > die2_wins


t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))

    A = nums[:4]
    B = nums[4:]

    found = False

    for c1 in range(1, 11):
        for c2 in range(1, 11):
            for c3 in range(1, 11):
                for c4 in range(1, 11):
                    C = [c1, c2, c3, c4]

                    if beats(A, B) and beats(B, C) and beats(C, A):
                        found = True

                    if beats(B, A) and beats(A, C) and beats(C, B):
                        found = True
                    if found:
                        break

    if found:
        print("yes")
    else:
        print("no")