def romanToInt(s):
    if s == "":
        return 0
    valueDict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    output = 0
    for i in range(0, len(s)):
        currValue = valueDict[s[i]]
        if i+1 < len(s):
            nextRoman = s[i+1]
            nextValue = valueDict[nextRoman]
            if nextValue > currValue:
                output -= currValue
            else:
                output += currValue
        else:
            output += currValue
    return output



print(romanToInt("CDLIV"))