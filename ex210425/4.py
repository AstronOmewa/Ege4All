from string import *

ascii = [chr(i) for i in range(10000)]

with open('4.txt') as f:
    s = f.readline()
    l = 0
    mlen = 0
    str = []

    for r in range(1,len(s)):
        if s[r]<s[r-1]:
            mlen = max(mlen, r - l + 1)
        else:
            str.append(s[l:r])
            l = r
    print([x for x in str if len(x)==6])
    print((max(str, key=len)))