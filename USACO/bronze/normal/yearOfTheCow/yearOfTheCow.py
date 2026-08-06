import sys
sys.stdin = open("yearOfTheCow.in", "r")
sys.stdout = open("yearOfTheCow.out", "w")

n = int(input())
zodiac = [
    "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse",
    "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"
]

years = {}
years["Bessie"] = 0
for _ in range(n):
    words = input().split()

    cow = words[0]
    direction = words[3]
    animal = words[4]
    other_cow = words[7]
    other_year = years[other_cow]

    if direction == "previous":
        new_year = other_year - 1

        while zodiac[new_year % 12] != animal:
            new_year -= 1

    else:
        new_year = other_year + 1

        while zodiac[new_year % 12] != animal:
            new_year += 1

    years[cow] = new_year
print(abs(years["Elsie"]))