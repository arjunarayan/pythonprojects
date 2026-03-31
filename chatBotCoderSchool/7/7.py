letterSet = set()

while input() != "stop":
    letter = input()
    if letter in letterSet:
        break
    else:
        set.add(letter)
print(letterSet)