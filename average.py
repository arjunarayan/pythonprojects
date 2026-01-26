def findAverage(numList):
    result = 0
    for num in numList:

        result += num
    return result/len(numList)


print(f"The average of the list you gave is {findAverage(numbs)}")
