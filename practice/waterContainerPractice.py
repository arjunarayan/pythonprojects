def maxAreaWaterContainer(numList):
    x = 0
    y = len(numList) - 1
    area = 0
    maxArea = 0
    while x < y:
        minHeight = min(numList[x], numList[y])
        width = y - x
        area = minHeight * width
        maxArea = max(maxArea, area)
        if numList[x] < numList[y]:
            x += 1
        else:
            y -= 1
    return maxArea



print(maxAreaWaterContainer([1, 4, 6, 3, 9, 9, 4, 8]))