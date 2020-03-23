import numpy as np
import decimal

N = 200
decimal.getcontext().prec = 200
e = decimal.Decimal(0.0)
i = 0

for i in range(N, 0, -1):
    e = (e + decimal.Decimal(1.0)) / decimal.Decimal(i)

e = e + 1
print(e)

cur = e * 1000000000
print(cur)


def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for d in range(3, int(np.floor(np.sqrt(number))), 2):
        if number % d == 0:
            return False
    return True


while True:
    tmp = cur // 1
    if is_prime(tmp):
        print(tmp)
        break
    else:
        cur %= 10000000000
        cur *= 10
