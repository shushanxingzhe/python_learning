def replace(s, old, new):
    dest = []
    old_len = len(old)
    i = 0
    while i < len(s):
        if s[i:i + old_len] == old:
            dest.append(new)
            i += old_len
        else:
            dest.append(s[i])
            i += 1
    return ''.join(dest)


print(replace('We are together', ' ', '%20'))
print(replace('We are together', 're', 'er'))
