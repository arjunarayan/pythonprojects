import sys
sys.stdin = open("missingNumber.in", "r")
sys.stdout = open("missingNumber.out", "w")

numList = set(map(int, input().split(" ")))


def findMissingNum(NumList):
    for i in range(1, len(NumList)):
        if i in numList:
            continue
        else:
            return i
    return len(NumList) + 1

print(findMissingNum(numList))