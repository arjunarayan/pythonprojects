def reverse(word):
    wordList = word.split(" ")
    reverseList = []
    for i in range(len(wordList)-1,-1,-1):
        reverseList.append(wordList[i])
    reverseString = " ".join(reverseList)
    return reverseString

sentence = "The sky is blue"
print(f"Original: {sentence}")
print(f"Reverse: {reverse(sentence)}