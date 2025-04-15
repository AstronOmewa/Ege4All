import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('26.3.txt') as f:
    k = int(f.readline())
    winds = dict()

    for x in f.readlines():
        t1, dt, w = map(int, x.split())
        if w not in winds.keys():
            winds[w] = [(t1,dt)]
        else:
            winds[w] += [(t1,dt)]

    for w in winds.keys():
        winds[w].sort()

    counts = dict(zip(winds.keys(),[0]*len(winds.keys())))
    left = 0

    for w in winds.keys():
        endtime = 0
        for t, dt in winds[w]:

            if t>=endtime:
                endtime = t+dt
                counts[w]+=1
            else:
                if endtime - t <=40:
                    endtime+=dt
                    counts[w]+=1
                else:
                    left += 1
            
    print(max(counts.values()), left)