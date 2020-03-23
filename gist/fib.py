def fib1(n):
    if n < 3:
        return 1
    return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    f1 = 1
    f2 = 1
    if n == 1:
        return 1
    for i in range(1, n - 1):
        f2 = f2 + f1
        f1 = f2 - f1
    return f2


import time

start = time.time()
print(fib1(30))
print(time.time() - start)
start = time.time()
print(fib2(30))
print(time.time() - start)
print(fib2(1))
print(fib2(2))
print(fib2(3))
print(fib2(4))
print(fib2(5))
