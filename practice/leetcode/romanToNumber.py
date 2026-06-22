def convertRomanToNumber(romanNumeral):
    romanNumerals = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    result = 0
    for index in range(0, len(romanNumeral)):
        currLetter = romanNumeral[index].upper()
        if index + 1 < len(romanNumeral):
            nextLetter = romanNumeral[index+1].upper()
            if romanNumerals[nextLetter] > romanNumerals[currLetter]:
                result -= romanNumerals[currLetter]
            else:
                result += romanNumerals[currLetter]
        else:
            result += romanNumerals[currLetter]
    return result


print(convertRomanToNumber("iiii"))