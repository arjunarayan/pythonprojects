"""
    Find the character with most frequency and return character
"""


def most_frequent_letter(inputString):
    letterCount = {} # Initializing empty dictionary to count each letter


    for letter in inputString:
        if letter in letterCount:
            letterCount[letter] += 1
        else:
            letterCount[letter] = 1
    maxCount = 0
    result = ""
    for letter in inputString:
        if letterCount[letter] > maxCount:
            maxCount = letterCount[letter]
            result = letter
    return result

print(most_frequent_letter("Mississippi"))
