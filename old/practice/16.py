# f = [0] * 3000

# f[1] = 1

# for i in range(2,len(f)):
#     f[i] = (i-1) * f[i-1]
  
# print(
#     (f[2024] + 2 * f[2023])//f[2022]
# )

"""

(№ 3467) Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = n + 1 при n < 3
F(n) = F(n-2) + n - 2, если n ≥ 3 и чётно,
F(n) = F(n+2) + n + 2, если n ≥ 3 и нечётно.
Сколько существует чисел n, для которых значение F(n) определено и будет пятизначным?

"""
# from sys import *
# setrecursionlimit(10000)
# def f(n):
#     if n < 3:
#         return n+1
#     if n%2 == 0:
#         return f(n-2) + n-2
#     else:
#         return f(n+2) + n+2
    
# c = 0
# from time import time

# t = time()
# for i in range(4,9999):
#     try:
#         if len(str(f(i))) == 5:
#             c+=1
#     except RecursionError:
#         continue
# t1 = time()
# for i in range(4,9999,2):
#     # try:
#         if len(str(f(i))) == 5:
#             c+=1
#     # except RecursionError:
#     #     continue
# t2 = time()

# print('tr_ex_time:{} s\nanalytic_time:{} s.\n Difference: {}'.format(t1-t, t2-t1, abs(t1-t-t2+t1)))
# print(c)

"""
(№ 7250) *Обозначим через a%b остаток от деления натурального числа a на натуральное число b, 
а через a//b – целую часть от деления a на b. Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = 1, если n = 0,
F(n) = F(n // 8) · (n % 8), если n > 0 и n нечётно;
F(n) = F(n // 8), если n > 0 и n чётно.
Определите количество значений n, таких что 89 ≤ n ≤ 810, для которых F(n) = 25.
"""

# from itertools import *
# from functools import *

# def mul(a):
#     s = [int(x) for x in a if int(x)%2 != 0]
#     if len(s) > 0:
#         return reduce(lambda x,y: x*y, a)
#     else: return 0

# alf = '012456'
# a = [''.join(x) for x in product(alf,repeat=10) if x[0]!='0' and x.count('5')==2]

# print(len(a))

"""
*Обозначим через a%b остаток от деления натурального числа a на натуральное число b, 
а через a//b – целую часть от деления a на b. Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = 0, если n = 0,
F(n) = F(n // 10) + n % 10, если n > 0 и n нечётно;
F(n) = F(n // 10), если n > 0 и n чётно.
Определите количество значений n, таких что 10**9 ≤ n ≤ 6·10**9, для которых F(n) = 0.
"""
from functools import reduce
from itertools import product

def sum(a):
    s = [int(x) for x in a]
    if len(s)>0:
        return reduce(lambda x,y: x+y, a)
    return 1

alf = "02468"

print(2*5**9+1)