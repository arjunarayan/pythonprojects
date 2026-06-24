import sys
sys.stdin = open("blockGame.in", "r")
sys.stdout = open("blockGame.out", "w")

n = int(input())

answer = [0] * 26
for _ in range(n):
    word1, word2 = input().split()
    word_1_count = [0] * 26
    word_2_count = [0] * 26

    for letter in word1:
        word_1_count[ord(letter) - ord("a")] += 1


    for letter in word2:
        word_2_count[ord(letter) - ord("a")] += 1
    for i in range(26):
        answer[i] += max(word_1_count[i], word_2_count[i])

for i in range(26):
    print(answer[i])
