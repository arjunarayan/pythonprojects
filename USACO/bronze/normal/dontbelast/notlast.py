import sys
sys.stdin = open("notlast.in", "r")
sys.stdout = open("notlast.out", "w")

milk = {
    "Bessie": 0,
    "Elsie": 0,
    "Daisy": 0,
    "Gertie": 0,
    "Annabelle": 0,
    "Maggie": 0,
    "Henrietta": 0
}

n = int(input())

for _ in range(n):
    name, milk_amount = input().split()
    milk[name] += int(milk_amount)


amounts = sorted(set(milk.values()))


if len(amounts) == 1:
    print("Tie")
else:
    second_amount = amounts[1]
    second_cows = []

    for name in milk:
        if milk[name] == second_amount:
            second_cows.append(name)
    if len(second_cows) == 1:
        print(second_cows[0])
    else:
        print("Tie")