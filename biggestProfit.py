def findBiggestProfit(nums):
    bp = nums[0]
    mp = 0

    for i in range(1, len(nums)):
        cp = nums[i]
        if cp - bp > mp:
            mp = cp - bp
        if cp < bp:
            bp = cp
    return mp


print(findBiggestProfit([1, 3, 4, 2, 5]))