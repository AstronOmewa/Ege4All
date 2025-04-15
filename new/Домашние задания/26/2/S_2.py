import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('26.2.txt') as f:
    n = int(f.readline())
    a = [int(x) for x in f.readlines()]
    ch = [int(x) for x in a if (int(x)%2) == 0]
    nch = [int(x) for x in a if (int(x)%2) != 0] 
    
    c, maxs = 0, 0

    for i in range(len(ch)):
        for j in range(len(nch)):
            if ((ch[i]+nch[j]) in nch):
                c+=1 
                maxs = max(maxs, ch[i]+nch[j])
    
    print(c, maxs)