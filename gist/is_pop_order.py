def isPopOrder(pushV, popV):
    if len(pushV) == 0 or len(pushV) != len(popV):
        return False
    stack = []
    j = 0
    for v in pushV:
        stack.append(v)
        if stack[-1] == popV[j]:
            stack.pop()
            j += 1
    while stack:
        if stack.pop() == popV[j]:
            j += 1
        else:
            return False
    return True


def isPopOrder1(pushV, popV):
    if len(pushV) == 0 or len(pushV) != len(popV):
        return False
    stack = []
    j = 0
    for v in pushV:
        stack.append(v)
        while stack and stack[-1] == popV[j]:
            stack.pop()
            j += 1
    if stack:
        return False
    else:
        return True


data = [1, 2, 3, 4, 5]
right = [4, 5, 3, 2, 1]
wrong = [4, 3, 5, 1, 2]
print(isPopOrder(data, right))
print(isPopOrder(data, wrong))
print(isPopOrder1(data, right))
print(isPopOrder1(data, wrong))
