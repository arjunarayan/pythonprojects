def findSumPairsFromList(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print([nums[i], nums[j]])

def findSumPairsFromList1(nums, target):
    numbers = set()
    result = []
    resultHash = set()
    for num in nums:
        diff = target - num
        if diff in numbers:
            output = [diff, num]
            outputHash = hash(f"{output}")
            if outputHash not in resultHash:
                result.append(output)
                resultHash.add(outputHash)
        elif num not in numbers:
            numbers.add(num)

    print(result)


#indSumPairsFromList1([1, 2, 3, 2, 4, 5, 6], 6)
#findSumPairsFromList1([3,3,3], 6)


