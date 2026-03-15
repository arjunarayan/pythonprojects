
def helper(num, numDict):

    units = num % 10


    if num < 20:
        return numDict[num]
    elif num < 100:
        tens = int(num/10)*10
        return numDict[tens] + numDict[units]
    elif num < 1000:
        num_of_hundreds = int(num / 100)
        return f"{helper(num_of_hundreds, numDict)} hundred " + helper(num % 100, numDict)
    elif num < 1000000:
        num_of_thousands = int(num / 1000)
        return f"{helper(num_of_thousands, numDict)} thousand " + helper(num % 1000, numDict)
    elif num < 1000000000:
        num_of_millions = int(num / 1000000)
        return f"{helper(num_of_millions, numDict)} million " + helper(num % 1000000, numDict)
    else:
        num_of_billions = int(num / 1000000000)
        return f"{helper(num_of_billions, numDict)} billion " + helper(num % 1000000000, numDict)


def main(num):

    numDict = {
            0 : "",
            1 : "one",
            2 : "two",
            3 : "three",
            4 : "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty ",
            30: "thirty ",
            40: "forty ",
            50: "fifty ",
            60: "sixty ",
            70: "seventy ",
            80: "eighty ",
            90: "ninety ",
            100: "hundred",
            1000: "thousand",
            1000000: "million",
            1000000000: "billion",
            1000000000000: "trillion"
    }
    if num < 0:
        return False
    if num == 1000000000000:
        return numDict[1000000000000]
    if num > 1000000000000:
        return False
    if num == 0:
        return "zero"
    return helper(num, numDict)

print(main(1000012465))
