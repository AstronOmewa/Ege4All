B = {-42, -10,-8,2,16}
C = {-10,-4,2,15,23}
A = set(range(-500,600))
def f(x, A):
    return ((x in A) <= (x in B)) or (x in C)


for x in range(-500,600):
    if f(x, A) == 0:
        A.remove(x)

print(sum(x for x in A if x>0))

print(len(range(41,64)))