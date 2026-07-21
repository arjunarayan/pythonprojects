import sys
sys.stdin = open("uddered.in", "r")
sys.stdout = open("uddered.out", "w")

cowphabet = input().strip()
heard = input().strip()

position = [0] * 26

for i in range(26):
    letter = cowphabet[i]
    index = ord(letter) - ord("a")
    position[index] = i

answer = 1

for i in range(1, len(heard)):
    previous = heard[i - 1]
    current = heard[i]

    previous_pos = position[ord(previous) - ord("a")]
    current_pos = position[ord(current) - ord("a")]

    if current_pos <= previous_pos:
        answer += 1
print(answer)