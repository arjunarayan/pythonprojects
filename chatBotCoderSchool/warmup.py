import sys
sys.stdout = open("warmup.out", "w")
for num in range(1, 1001):
    if num % 10 == 6 or str(num)[len(str(num))-2] + str(num)[len(str(num))-1] == "12":
        continue
    else:
        print(num)
