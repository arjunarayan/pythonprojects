"""
Two Sum:
You are given a list of numbers and a target. Your goal is to find the two numbers in the list that add up to the target,
then return the indices of these numbers in the list.
"""

def twoSumUsingNestedLoops(numList, target):
    for i in range(0, len(numList)):
        for j in range(i+1, len(numList)):
            if numList[i] + numList[j] == target:
                return i, j
    return None


def twoSumUsingDictionary(numList, target):
    numDict = {}
    for i in range(0, len(numList)):
        num = numList[i]
        diff = target - num
        if diff in numDict:
            return numDict[diff], i
        else:
            numDict = [i]
    return None

print("This is the Nested Loops solution.")
print(twoSumUsingNestedLoops([3, 5, 6, 2, 1], 11))
print("This is the Dictionary solution.")
print(twoSumUsingDictionary([3, 5, 6, 2, 1], 11))