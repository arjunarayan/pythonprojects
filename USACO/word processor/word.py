file_in = open("word.in")
data = file_in.read().strip().split("\n")
n, k = map(int, data[0].split())
essay = data[1]

essayList = essay.split(" ")

currLength = 0
currLine = ""
for word in essayList:
    if currLength + len(word) <= k:
        currLine += f"{word} "
        currLength += len(word)
    else:
        print(currLine.rstrip(), file=open("word.out", "a"))
        currLine = f"{word} "
        currLength = len(word)
print(currLine.rstrip(), file=open("word.out", "a"))
