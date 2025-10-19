def findProductExceptCurrent(nums):
    output = []
    product = 1
    for num in nums:
        product *= num
    for num1 in nums:
        output.append(int(product/num1))
    return output


print(findProductExceptCurrent([1, 2, 3, 4]))