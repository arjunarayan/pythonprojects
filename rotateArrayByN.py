def rotateByN(n, inputList):

        if n < 0:
            return None
        length = len(inputList)
        if n > length:
            n = n % length
        i = n
        output = []
        while i < length:
            output.append(inputList[i])
            i += 1
        i = 0
        while i < n:
            output.append(inputList[i])
            i += 1

        return output


rotatedList = rotateByN(1000001, [1, 2, 3, 4, 5])

if rotatedList is None:
    print("Error! Negative Number!")
else:
    print(rotatedList)
