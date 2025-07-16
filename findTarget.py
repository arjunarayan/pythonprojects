nums = [2, 12, 9, 8, 10]


def findNumber(target):
    for elem in nums:
        if elem == target:
            return True

    return False

def findNumberUsingIndex(target):
    for index in range(0, len(nums)):
        if nums[index] == target:
            return True

    return False

def findNumberUsingWhile(target):
    index = 0
    while index < len(nums):
        if nums[index] == target:
            return True
        index += 1
    return False


print(findNumberUsingWhile(12))