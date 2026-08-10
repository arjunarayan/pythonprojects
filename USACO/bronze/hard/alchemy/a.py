import sys
sys.stdin = open("a.in", "r")
sys.stdout = open("a.out", "w")
n = int(input())
metals = list(map(int, input().split()))

k = int(input())

recipes = [[] for _ in range(n)]

for _ in range(k):
    line = list(map(int, input().split()))
    metal = line[0] - 1
    ingredients = line[2:]

    for i in range(len(ingredients)):
        ingredients[i] -= 1

    recipes[metal] = ingredients

def make(metal):
    if metals[metal] > 0:
        metals[metal] -= 1
        return True

    if len(recipes[metal]) == 0:
        return False

    for ingredient in recipes[metal]:
        if not make(ingredient):
            return False

    return True
answer = 0

while make(n - 1):
    answer += 1

print(answer)