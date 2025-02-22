with open("D:\\egeAll\\24\\py\\24 (1).txt") as f:
    s = f.readline()

    l = 0
    ka = kb = 0
    mx = 0

    for r in range(len(s)):
        if s[r] == 'A': ka+=1
        if s[r] == 'B': kb+=1

        while ka>1 or kb>1:
            if s[l]=='A': ka-=1
            if s[l]=='B': kb-=1
            l+=1
        
        mx = max(mx, r - l + 1)

    print(mx)