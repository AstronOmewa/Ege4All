import os

os.chdir(os.path.dirname(__file__))

from string import *

ascii = [chr(i) for i in range(10000)]

with open('4.txt') as f:
    s = f.readline()
    l = 0
    mlen = 0
    str = []

    for r in range(1,len(s)):
        if s[r]<s[r-1]:
            mlen = max(mlen, r - l)
            str.append(s[l:r])
        else:
            
            l = r
    print([x for x in str ])
    print((max(str, key=len)), mlen)