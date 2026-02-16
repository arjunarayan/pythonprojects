def checkIntersections(nums1, nums2):
    nums_dict = {}
    for number in nums1:
        nums_dict[number] = True

    same_numbers = {}

    for number in nums2:
        if number in nums_dict:
            same_numbers[number] = True

    output = []
    for number in same_numbers:
        output.append(number)

    return output

def checkIntersectionsSet(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    output = list(set1 & set2)
    return output


print(checkIntersectionsSet([4, 9, 5], [9, 4, 9, 8, 4]))
print(checkIntersections([4, 9, 5], [9, 4, 9, 8, 4]))