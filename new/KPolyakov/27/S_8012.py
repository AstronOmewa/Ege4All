import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from math import *

def diam(cl):
    return max([dist(p1,p2) for p1 in cl for p2 in cl if p1!=p2])

with open('27.8012_b.txt') as f:
    points = [tuple(map(float, p.replace(',','.').split())) for p in f.readlines()]
    clusters = []

    while points:
        clusters.append([points.pop(0)])
        for p in clusters[-1]:
            for p1 in points:
                if dist(p,p1) < 0.33:
                    clusters[-1].append(p1)
                    points.remove(p1)
    
    # clusters = [cluster for cluster in clusters if len(clusters)>0]
    print(
        int(min(diam(cluster) for cluster in clusters) * 100000),
        int(sum([diam(cluster) for cluster in clusters])/len(clusters) * 100000)
    )