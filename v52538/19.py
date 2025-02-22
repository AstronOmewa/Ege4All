def f(s, m):
    if s >= 100:
        return m%2 == 0
    if m == 0:
        return 0
    
    h = [f(s+7, m-1), f(s*2, m-1)]

    if (m-1)%2 == 0:
        return any(h)
    else:
        return all(h)
    
def g(s,m):
    if s >= 100:
        return m%2 == 0
    if m == 0:
        return 0
    
    h = [f(s+7, m-1), f(s*2, m-1)]

    if (m-1)%2 == 0:
        return any(h)
    else:
        return any(h)
    
print([s for s in range(1,100) if f(s, 1) and g(s, 2)])
# print([s for s in range(1,100) if not f(s, 1) and not f(s, 3) and (f(s,2)) and g(s, 3)])
# АНАЛитика


