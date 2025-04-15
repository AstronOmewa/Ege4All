import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('26.4.txt') as f:

    k = int(f.readline())

    query = []

    for r in f.readlines():
        ts, te = map(int, r.split())

        query.append((ts, te))

    query.sort()

    samet = [0]*86400

    for q in query:
        ts, te = q
        if te>= 8*3600 and ts<=14*3600:
            for x in range(ts, te): samet[x]+=1

    print(max(samet), samet.count(max(samet)))
        
            
