import numpy as np

'''
一组二极管有七个，能表示0-9十个数，现在有n组二极管，每组二极管中有一些亮，有一些灭，灭可能是因为坏了也可能是因为不需要亮。要求出这n组二极管能显示的所有数字的组合
输入：二维数组，每行代表一组二极管，每行七个，0代表灭，1代表亮
输出：所有可以显示的数字组合
例：现在两组二极管，显示的是23，那输出23，83，88，28
'''


def led_possible_display(number):
    possible_map = {
        0: [0, 8],
        1: [1, 3, 4, 7, 8, 9],
        2: [2, 8],
        3: [3, 8],
        4: [4, 8, 9],
        5: [5, 6, 8, 9],
        6: [6, 8],
        7: [3, 7, 8, 9],
        8: [8],
        9: [8, 9]
    }
    res = np.array([0])
    digit = len(str(number))
    for i in range(digit - 1, -1, -1):
        cur = (number // 10 ** i) % 10
        res = res * 10 + np.array([possible_map[cur]]).T
        res = res.reshape(1, -1)
    return list(res)


print(led_possible_display(234))
