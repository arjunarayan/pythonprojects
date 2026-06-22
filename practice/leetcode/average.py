def findAverage(numList):
    result = 0
    for num in numList:

        result += num
    return result/len(numList)

numbers = [3, 7, 9, 2, 5, 10]
print(f"The average of {numbers} is {findAverage(numbers)}")