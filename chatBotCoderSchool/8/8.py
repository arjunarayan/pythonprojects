import sys


sys.stdout = open("8.out", "w")

numList = []
while True:
    number = input()
    if number == "stop":
        break
    numList.append(int(number))


print(f"{min(numList)} {max(numList)} {float(sum(numList, 0) / len(numList))}")