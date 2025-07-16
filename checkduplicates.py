def has_duplicates(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = True
    return False


print(has_duplicates([1, 2, 3, 4]))
