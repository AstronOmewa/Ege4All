import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

from math import dist

# def center(k):
#     m = 10**9
#     pmin = ()
#     for pt in k:
#         dcur = 0
#         for pt1 in k:
#             mcur+=dist(pt,pt1)
#         if m>dcur:
#             m = dcur
#             pmin = p

#     return (m, pmin)

# c = []

# for k in k1:
#     c += [center(k)[1]]

# print(c)


##DBSCAN

with open('27.8057_a.txt') as f:
    a = [tuple(map(float, x.replace(',','.').split())) for x in f]
    clusters = []

    while a:
        clusters.append([a.pop(0)])
        for p in clusters[-1]:
            for p1 in a:
                if dist(p,p1) <= 0.5:
                    clusters[-1].append(p1)
                    a.remove(p1)