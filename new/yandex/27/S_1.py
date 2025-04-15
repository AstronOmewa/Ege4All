import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from math import *

def avg(a):
    return sum([x for x in a])/len(a)

def corr(p):
    x = [p[i][0] for i in range(len(p))]
    y = [p[i][1] for i in range(len(p))]
    return sum((x[i]-avg(x))*(y[i]-avg(y))\
                for i in range(len(x)))\
                    /sqrt((sum((x[i]-avg(x))**2 for i in range(len(x)))))\
                    /sqrt((sum((y[i]-avg(y))**2 for i in range(len(y)))))
    
with open('27.1_b.txt') as f:
    points = [tuple(map(float, p.split())) for p in f]
    clusters = []

    while points:
        clusters.append([points.pop(0)])
        for p1 in clusters[-1]:
            for p2 in points:
                if dist(p1, p2) < 5.5:
                    clusters[-1].append(p2)
                    points.remove(p2)

    # print([len(cluster) for cluster in clusters]) 
    c = [corr(cluster) for cluster in clusters if 1>=abs(corr(cluster))>=0.9]
    a = [izm for cluster in clusters for izm in cluster ]
    print(len(a), int(avg(c)*100000))