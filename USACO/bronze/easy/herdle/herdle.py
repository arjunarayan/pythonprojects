import sys
sys.stdin = open("herdle.in", "r")
sys.stdout = open("herdle.out", "w")

answer = []
guess = []

for _ in range(3):
    answer.append(input().strip())

for _ in range(3):
    guess.append(input().strip())

green = 0
answer_count = [0] * 26
guess_count = [0] * 26

for r in range(3):
    for c in range(3):
        if answer[r][c] == guess[r][c]:
            green += 1
        else:
            answer_index = ord(answer[r][c]) - ord("A")
            guess_index = ord(guess[r][c]) - ord("A")

            answer_count[answer_index] += 1
            guess_count[guess_index] += 1


yellow = 0

for i in range(26):
    yellow += min(answer_count[i], guess_count[i])

print(green)
print(yellow)