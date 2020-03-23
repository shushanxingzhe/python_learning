def edit_distance(str1, str2):
    distance = [[i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                d = 0
            else:
                d = 1
            distance[i][j] = min(distance[i - 1][j] + 1, distance[i][j - 1] + 1, distance[i - 1][j - 1] + d)
    return distance[len(str1)][len(str2)]


def levenshtein_distance(str1, str2):
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)
    elif str1 == str2:
        return 0

    if str1[-1] == str2[-1]:
        d = 0
    else:
        d = 1

    return min(levenshtein_distance(str1, str2[:-1]) + 1,
               levenshtein_distance(str1[:-1], str2) + 1,
               levenshtein_distance(str1[:-1], str2[:-1]) + d)


print(edit_distance('xiaomi', 'xiami'))
print(edit_distance('hello', 'halle'))
print(edit_distance('distance', 'distinct'))

print(levenshtein_distance('xiaomi', 'xiami'))
print(levenshtein_distance('hello', 'halle'))
print(levenshtein_distance('distance', 'distinct'))
