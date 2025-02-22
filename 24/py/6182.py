s = open('D:\\egeAll\\24\\6182.txt').readline()
l = 0

r = m = 0

for r in range(len(s)):
    if s[r] == 'А' or s[r] == 'D':
        if s[l] == 'A' and s[r] == 'D' or s[r] == 'A' and s[l] == 'D':
            m = max(m, r - l + 1)
        l = r
print(m)