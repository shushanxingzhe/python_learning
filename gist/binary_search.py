def binary_search(arr, val):
    def search(data, value, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if value == data[mid]:
            return mid
        elif value < data[mid]:
            return search(data, value, left, mid - 1)
        else:
            return search(data, value, mid + 1, right)

    return search(arr, val, 0, len(arr) - 1)


a = [i * 2 for i in range(1, 100)]
print(binary_search(a, 30))
print(binary_search(a, 37))
print(binary_search(a, 70))
