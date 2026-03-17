file_in = open("whereami.in")
# reading the data in the input file
data = file_in.read().strip().split("\n")

n = int(data[0])
mailboxes = data[1]

for k in range(1, n+1):
    seen = set()
    unique = True
    for i in range(n - k + 1):
        part = mailboxes[i:i+k]
        if part in seen:
            unique = False
            break
        seen.add(part)
    if unique:
        print(k, file=open("whereami.out", "w"))
        break