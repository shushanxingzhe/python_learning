def bubbleSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(1, length - i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr


def selectSort(arr):
    length = len(arr)
    for i in range(length):
        minindex = i
        for j in range(i+1, length):
            if arr[j] < arr[minindex]:
                minindex = j
        if minindex != i:
            arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr


def insertSort(arr):
    length = len(arr)
    for i in range(length):
        cur,preindex = arr[i],i
        while preindex > 0 and cur > arr[preindex]:
            preindex -= 1
        arr[i], arr[preindex] = arr[preindex], arr[i]
    return arr


def quickSort(arr):

    def partition(arr,left,right):
        base = left
        while left < right:
            while left < right and arr[right] >= arr[base]:
                right -= 1
            while left < right and arr[left] < arr[base]:
                left += 1
            arr[left], arr[right] = arr[right], arr[left]
        arr[left], arr[base] = arr[base], arr[left]
        return left

    def sort(arr,left,right):
        if left >= right:
            return
        base = partition(arr,left,right)
        sort(arr,left,base-1)
        sort(arr,base+1,right)
    sort(arr,0,len(arr)-1)
    return arr


def mergeSort(arr):
    def merge(left,right):
        result = []
        i = j = 0
        left_len = len(left)
        right_len = len(right)
        while i < left_len and j < right_len:
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        return result + left[i:] + right[j:]
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(left,right)

data = [9, 8, 2, 4, 3, 3, 6, 5 ,1]
print(bubbleSort(data))
print(selectSort(data))
print(insertSort(data))
print(quickSort(data))
print(mergeSort(data))