nums = [3, 7, 8, 11, 19]
numbs = []


def findAverage(numList):
    result = 0

    if len(numList) <= 0:
        return 0
    else:
        for i in numList:
            result += i
        return result / len(numList)


print(f"The average of the list you gave is {findAverage(numbs)}")
