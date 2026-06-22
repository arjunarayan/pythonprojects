def find_missing_number(nums):
    n = len(nums)
    all_nums = set(range(n + 1))
    nums_set = set(nums)
    missing = all_nums - nums_set
    for number in missing:
        return number

print(find_missing_number([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 2223]))

