def swap(arr, k, l):
    temp = arr[k]
    arr[k] = arr[l]
    arr[l] = temp
def bubbleSort(arr, dir=1):
    temp = 0
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1):
            if dir == 1:
                if arr[j] > arr[j+1]:
                    swap(arr, j, j+1)
            else:
                if arr[j] < arr[j+1]:
                    swap(arr, j, j+1)
    print(arr)

bubbleSort([5, 2, 4, 1, 3])