s = open('D:\\egeAll\\24\\6147.txt').readline()
l = 0
i = s.find('O')
r = m = kf = 0

for r in range(len(s)):
    if s[r] == 'F': kf += 1
    if s[r] == 'O': k = 0

    while kf>2 and s[r] == 'O':
        if s[l] == 'F': kf -= 1
    l = r

    m = max(m, r-l+1)

print(m)