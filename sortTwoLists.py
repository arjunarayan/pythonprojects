def mergeSortedArrays(nums1, nums2):
    # Defining empty output list
    nums3 = []

    # While loop to go through lists and add sorted numbers till end of one list
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):

        if nums1[i] < nums2[j]:
            nums3.append(nums1[i])
            i += 1
        else:
            nums3.append(nums2[j])
            j += 1

    while i < len(nums1):
        nums3.append(nums1[i])
        i += 1

    while j < len(nums2):
        nums3.append(nums2[j])
        j += 1

    return nums3


print(mergeSortedArrays([1, 2, 3, 9], [3, 5, 6, 350]))