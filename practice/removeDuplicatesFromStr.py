def removeDuplicates(input_string):
    result = ""
    seen = set()
    input_string = input_string.lower()
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result += char
    return result

word = "aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz"

print(f"The word {word} without any duplicates is {removeDuplicates(word)}!!!!!!!")