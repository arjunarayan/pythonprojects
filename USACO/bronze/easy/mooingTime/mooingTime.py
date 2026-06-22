import sys



sys.stdin = open("mooingTime.in", "r")
sys.stdout = open("mooingTime.out", "w")

def is_moo(Inputword) -> bool:
    if len(Inputword) != 3:
        return False
    elif Inputword[0] != Inputword[1] and Inputword[1] == Inputword[2]:
        return True
    return False

n, f = map(int, input().split(" "))
moos = list(input())
answers = set()
for i in range(n):
    originalLetter = moos[i]
    for ch in list("abcdefghijklmnopqrstuvwxyz"):
         if originalLetter == ch:
             continue
         moos[i] = ch
         freq = {}
         for j in range(n-2):
             word = moos[j] + moos[j+1] + moos[j+2]
             if is_moo(word):
                 if word in freq:
                    freq[word] += 1
                 else:
                     freq[word] = 1
         for word in freq:
            if freq[word] >= f:
                answers.add(word)
         moos[i] = originalLetter

sortedList = sorted(answers)
print(len(answers))
for word in sortedList: print(word)
