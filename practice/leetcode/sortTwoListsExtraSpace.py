def sortTwoListsUsingExtraSpace(num1:list, num2:list, m:int, n:int):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if num1[i] > num2[j]:
            num1[k] = num1[i]
            i -= 1
        else:
            num1[k] = num2[j]
            j -= 1
        k -= 1

    while i >= 0:
        num1[k] = num1[i]
        k -=1
        i -=1
    while j >= 0:
        num1[k] = num2[j]
        k -=1
        j -=1
    return num1


print(sortTwoListsUsingExtraSpace([1, 3, 5, 0, 0, 0], [2, 4, 6], 3, 3))