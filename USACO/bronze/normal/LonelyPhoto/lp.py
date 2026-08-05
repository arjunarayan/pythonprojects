import sys
sys.stdin = open("lp.in", "r")
sys.stdout = open("lp.out", "w")

n = int(input())
s = input().strip()


answer = 0

for i in range(n):
    left = 0
    left_pos = i - 1

    while left_pos >= 0 and s[left_pos] != s[i]:
        left += 1
        left_pos -= 1


    right = 0
    right_pos = i + 1

    while right_pos < n and s[right_pos] != s[i]:
        right += 1
        right_pos += 1
    answer += left * right + max(0, left - 1) + max(0, right - 1)

print(answer)