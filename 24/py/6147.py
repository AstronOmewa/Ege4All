s = open('D:\\egeAll\\24\\6147.txt').readline()
l = 0

r = m = k = 0

for r in range(len(s)):
    if s[r] == '.': k+=1

    while k > 7:
        if s[l] == '.': k -= 1
        l += 1

print(m)