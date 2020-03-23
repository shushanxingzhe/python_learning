def ring(arr, k):
    ret = []
    idx = 0
    while arr:
        idx = (idx + k - 1) % len(arr)
        ret.append(arr.pop(idx))
    return ret


def ring_last(n, k):
    if n < 1 or k < 1:
        return -1
    if n == 1:
        return 0
    value = 0
    for index in range(2, n + 1):
        value = (value + k) % index
    return value


data = list(range(0, 10))
print(ring(data, 3))

print(ring_last(10, 3))
