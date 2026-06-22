def checkNumOfVowels(str):
    str_lower = str.lower()

    vowelCount = {}
    vowels = "aeiou"
    for char in str_lower:
        if char in vowels:
            if char in vowelCount:
                vowelCount[char] += 1
            else:
                vowelCount[char] = 1
    return vowelCount

print(checkNumOfVowels("Aaeiou"))
