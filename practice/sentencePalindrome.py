def checkSentencePalindrome(sentenceInput):
    sentenceInputArray = sentenceInput.lower().split(" ")

    i = 0
    j = len(sentenceInputArray)-1
    while i < j:
        if sentenceInputArray[i] == sentenceInputArray[j]:
            i += 1
            j -= 1
        else:
            return False
    return True


print(checkSentencePalindrome("Hello world hello"))