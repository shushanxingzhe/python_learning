"""
给你六种面额 1、5、10、20、50、100 元的纸币，假设每种币值的数量都足够多，编写程序求组成N元（N为0~1000的非负整数）的不同组合的个数
"""


def count(n):
    """
    使用前i+1中钱币表示总面额为k的方案数 = 使用前i种钱币表示总面额为k的方案数 + 使用前i+1种钱币表示总面额为k-coins[i]的方案数
    :param n:
    :return:
    """
    coins = [1, 5, 10, 50, 100]
    ret = [0] * (n + 1)
    ret[0] = 1
    for c in coins:
        for k in range(c, n + 1):
            ret[k] += ret[k - c]
    return ret[n]


print(count(2))
print(count(10))
print(count(20))
print(count(200))
