def f(s1,s2, m):
    if s1+s2>=73: return (m)%2==0
    if m < 0: return 0

    h = [f(s1+1, s2, m-1), f(s1, s2+1, m-1), f(s1+s2,s2,m-1), f(s1,s1+s2, m-1)]

    if (m-1)%2 == 0: return any(h)
    else: return any(h)


def g(s1,s2, m):
    if s1+s2>=73: return (m)%2==0
    if m <= 0: return 0

    h = [g(s1+1, s2, m-1), g(s1, s2+1, m-1), g(s1+s2,s2,m-1), g(s1,s1+s2, m-1)]

    if (m-1)%2 == 0: return any(h)
    else: return all(h)


print('#19: ', [s for s in range(1,64) if f(9,s,2)])
print('#20: ', [s for s in range(1,64) if not g(9,s,1) and g(9,s,3)])
print('#21: ', [s for s in range(1,64) if g(9,s,4) and not g(9,s,2)])

