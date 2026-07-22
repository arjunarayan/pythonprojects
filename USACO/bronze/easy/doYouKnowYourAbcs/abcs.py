import sys
sys.stdin = open("abcs.in", "r")
sys.stdout = open("abcs.out", "w")

numbers = sorted(list(map(int, input().split())))
a = numbers[0]
b = numbers[1]
total = numbers[6]
c = total - a - b
print(a, b, c)