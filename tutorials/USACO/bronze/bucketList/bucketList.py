file_in = open("bucketList.in")
data = file_in.read().split("\n")
n = int(data[0])
times = [0] * 1001
for i in range(n):
    s, t, b = map(int, data[i+1].split(" "))
    for j in range(s, t):
        times[j] += b
print(max(times), file=open("bucketList.out", "w"))