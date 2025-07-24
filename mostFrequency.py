def most_frequent_letter(inputString):
    count = {}
    for letter in inputString:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    maxCount = 0
    result = ""
    for letter in inputString:
        if count[letter] > maxCount:
            maxCount = count[letter]
            result = letter
    return result

print(most_frequent_letter("Mississippi"))
