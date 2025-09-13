def calculateMaxAndSecondMax(nums):
    max = 0
    for num in nums:
        if num > max:
            max = num
    second_max = 0
    print(max)
    for num2 in nums:
        if second_max < num2 < max:
            second_max = num2
            print(second_max)
    return f"The highest number is: {max}. The second highest number is {second_max}"


print(calculateMaxAndSecondMax([0, 1, 2, 3, 4, 9, 8, 1500, 78, 100, 90000]))