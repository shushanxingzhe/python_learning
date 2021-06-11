import time


def brutal_force(haystack, needle):
    n = len(haystack)
    m = len(needle)
    i = j = 0
    counter = 0
    while i < n and j < m:
        counter += 1
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            i -= j - 1
            j = 0
    if j == m:
        return i-j, counter
    else:
        return -1, counter


def build_next(needle):
    m = len(needle)
    next_arr = [0] * m
    j = 0
    t = next_arr[0] = -1
    while j < m - 1:
        if 0 > t or needle[j] == needle[t]:
            j += 1
            t += 1
            next_arr[j] = t if needle[j] != needle[t] else next_arr[t]
        else:
            t = next_arr[t]
    return next_arr


def kmp(haystack, needle):
    n = len(haystack)
    m = len(needle)
    i = j = 0
    counter = 0
    next_arr = build_next(needle)

    while i < n and j < m:
        counter += 1
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            j = next_arr[j]
            if j == -1:
                i += 1
                j += 1

    if j == m:
        return i-j, counter
    else:
        return -1, counter


def build_bc(needle):
    bc = {}
    for i in range(len(needle)):
        bc[needle[i]] = i
    return bc


def build_ss(needle):
    m = len(needle)
    ss = [0] * m
    ss[m - 1] = m
    lo = hi = m - 1
    i = lo - 1

    while i >= 0:
        if i > lo and ss[m - hi + i - 1] < i - lo:
            ss[i] = ss[m - hi + i - 1]
        else:
            hi = i
            lo = min(hi, lo)
            while lo >= 0 and needle[lo] == needle[m - hi + lo - 1]:
                lo -= 1
            ss[i] = hi - lo
        i -= 1

    return ss


def build_gs(needle):
    ss = build_ss(needle)
    m = len(needle)
    gs = [m] * m

    i = 0
    for j in range(m-1, -1, -1):
        if j + 1 == ss[j]:
            while i < m - j - 1:
                gs[i] = m - j - 1
                i += 1

    for j in range(m-1):
        gs[m - ss[j] - 1] = m - j - 1

    return gs


def bm_bc(haystack, needle):
    n = len(haystack)
    m = len(needle)
    bc = build_bc(needle)
    gs = build_gs(needle)
    i = 0
    j = m - 1
    counter = 0
    while i < n-m+1 and j > -1:
        counter += 1
        if haystack[i + j] == needle[j]:
            j -= 1
        else:
            if haystack[i + j] not in bc:
                i += m + 1
                j = m - 1
            else:
                i += max(j - bc[haystack[i+j]], gs[j])
                j = m - 1

    if j == -1:
        return i, counter
    else:
        return -1, counter


text = '''WASHINGTON -- The rich really are different from you and me: They’re better at dodging the tax man.
Amazon founder Jeff Bezos paid no income tax in 2007 and 2011. Tesla founder Elon Musk’s income tax bill was zero in 2018.
 And financier George Soros went three straight years without paying federal income tax, 
 according to a report Tuesday from the nonprofit investigative journalism organization ProPublica.
Overall, the richest 25 Americans pay less in tax — an average of 15.8% of adjusted gross income — than many ordinary workers do,
once you include taxes for Social Security and Medicare, ProPublica found.
 Its findings are likely to heighten a national debate over the vast and widening inequality between the very wealthiest Americans and everyone else.'''

find = 'inequality'


start_time = time.time()
for _ in range(10000):
    brutal_force(text, find)
print('brutal_force: ', brutal_force(text, find), time.time()-start_time)

start_time = time.time()
print(build_next(find))
for _ in range(10000):
    kmp(text, find)
print('kmp: ', kmp(text, find), time.time()-start_time)

start_time = time.time()
for _ in range(10000):
    bm_bc(text, find)
print('bm_bc: ', bm_bc(text, find), time.time()-start_time)
