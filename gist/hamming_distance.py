a = int('11101', base=2)
b = int('10111', base=2)
print(a, b)
print(a ^ b)


def hamming_distance(x1, x2):
    x = x1 ^ x2
    n = 0
    while x:
        x &= x - 1
        n += 1
    return n


print(hamming_distance(a, b))
