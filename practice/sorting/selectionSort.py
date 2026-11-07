def swap(arr, k, l):
    temp = arr[k]
    arr[k] = arr[l]
    arr[l] = temp

def selectionSortAsc(arr):
    n = len(arr)
    for i in range(n):
      minIndex = i
      for j in range(i+1, n):
          if arr[j] < arr[minIndex]:
              minIndex = j
      swap(arr, i, minIndex)
    return arr

def selectionSortDesc(arr):
    n = len(arr)
    for i in range(n):
      maxIndex = i
      for j in range(i+1, n):
          if arr[j] > arr[maxIndex]:
              maxIndex = j
      swap(arr, i, maxIndex)
    return arr


print(selectionSortDesc([5, 4, 2, 1, 3]))