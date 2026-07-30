import sys
sys.stdin = open("cc.in", "r")
sys.stdout = open("cc.out", "w")

n = int(input())
tuition = list(map(int, input().split()))

tuition.sort()

best_money = 0
best_price = 0

for i in range(n):
    price = tuition[i]
    cows_attending = n - i
    money = price * cows_attending

    if money > best_money:
        best_money = money
        best_price = price

print(best_money, best_price)