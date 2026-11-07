def createPrefixArr(arr):
    sz = len(arr)
    pre = [0] * (sz + 1)
    j = 1
    for i in range(sz):
        if j > 0:
            pre[j] = pre[j-1] + arr[i]
        j += 1
    return pre

def fetchSumRange(l, r, arr):
    pref = createPrefixArr(arr)
    return pref[r+1] - pref[l]

print(fetchSumRange(2, 5,[1, 6, 4, 2, 5, 3]))