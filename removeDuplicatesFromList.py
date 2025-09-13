def removeDuplicates(nums):
    seen = set()
    index = 0
    result = []
    
    while index < len(nums):
        if nums[index] not in seen:
            seen.add(nums[index])
            result.append(nums[index])
        index += 1

    return result



print(removeDuplicates([1, 2, 1, 3, 4, 5,1,1,1,2,3,4,5,6,6,6,6,7,8,9,10]))