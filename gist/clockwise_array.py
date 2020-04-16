import numpy as np


def clockwise_array(data):
    height = len(data)
    width = len(data[0])
    result = []
    for i in range(height):
        j = i
        for j in range(i, width - i):
            result.append(data[i][j])
        for k in range(i + 1, height - i):
            result.append(data[k][j])
        r = height - i - 1
        if r != i:
            for j in range(width - i - 1 - 1, i - 1, -1):
                result.append(data[r][j])
            for k in range(r - 1, i, -1):
                result.append(data[k][j])
    return result


n = 6
arr = np.linspace(1, n ** 2, n ** 2, dtype=int).reshape((n, n))
print(arr)
print(clockwise_array(arr))
