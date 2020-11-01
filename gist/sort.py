def bubbleSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(1, length - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


def selectSort(arr):
    length = len(arr)
    for i in range(length):
        minindex = i
        for j in range(i + 1, length):
            if arr[j] < arr[minindex]:
                minindex = j
        if minindex != i:
            arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr


def insertSort(arr):
    length = len(arr)
    for i in range(1,length):
        val, cur = arr[i], i-1
        while cur >= 0 and val < arr[cur]:
            arr[cur+1] = arr[cur]
            cur -= 1
        arr[cur+1] = val
    return arr


def quickSort(arr):
    def partition(arr1, left, right):
        base = left
        while left < right:
            while left < right and arr1[right] >= arr1[base]:
                right -= 1
            while left < right and arr1[left] < arr1[base]:
                left += 1
            arr1[left], arr1[right] = arr1[right], arr1[left]
        arr1[left], arr1[base] = arr1[base], arr1[left]
        return left

    def sort(arr, left, right):
        if left >= right:
            return
        base = partition(arr, left, right)
        sort(arr, left, base - 1)
        sort(arr, base + 1, right)

    sort(arr, 0, len(arr) - 1)
    return arr


def mergeSort(arr):
    def merge(left, right):
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
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)


print(bubbleSort([9, 8, 2, 4, 3, 3, 6, 5, 1]))
print(selectSort([9, 8, 2, 4, 3, 3, 6, 5, 1]))
print(insertSort([9, 8, 2, 4, 3, 3, 6, 5, 1]))
print(quickSort([9, 8, 2, 4, 3, 3, 6, 5, 1]))
print(mergeSort([9, 8, 2, 4, 3, 3, 6, 5, 1]))
