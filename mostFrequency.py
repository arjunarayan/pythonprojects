def checkMostFrequency(input_str):
    count = {}
    for char in str:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    