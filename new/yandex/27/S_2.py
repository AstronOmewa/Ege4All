import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from math import *

def maxdst(cl):
    return max([dist(p,p1) for p1 in cl for p in cl])

def avgdst(cl):
    dst = [dst(p, p1) for p in cl for p1 in cl if p!=p1]
    return sum(dst)/len(dst)

with open('27.2_a.txt') as f:
    points = [tuple(map(float, p.replace(',','.').split())) for p in f]
    clusters = []
    
    while points:
        clusters.append([points.pop(0)])
        for p1 in clusters[-1]:
            for p2 in points:
                if dist(p1, p2) < 60:
                    clusters[-1].append(p2)
                    points.remove(p2)
    
    clusters = [cluster for cluster in clusters if len(cluster[0])>1000]
    
    print(10000*int(min([maxdst(cluster)/avgdst(cluster) for cluster in clusters])),\
          10000*int(sum([maxdst(cluster)/avgdst(cluster) for cluster in clusters]))\
        /len([maxdst(cluster)/avgdst(cluster) for cluster in clusters])\
    )