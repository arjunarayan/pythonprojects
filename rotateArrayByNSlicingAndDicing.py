def rotateByN(n, inputList):
    if n < 0:
        return None
    if n > len(inputList):
        n = n % len(inputList)
    return inputList[n: ] + inputList[0:n]

rotatedList = rotateByN(-900, [1, 2, 3, 4, 5])

if rotatedList is None:
    print("Error! Negative Number!")
else:
    print(rotatedList)