def game(s1,s2,m,strict = True):

    """
    
    """
    if m<0: return 0
    if s1+s2 >= 131: return (m)%2==0

    h = [game(s1+2,s2,m-1), game(s1*2,s2,m-1),game(s1,s2+2,m-1),game(s1,s2*2,m-1)]

    if m%2==0:
        return all(h) if strict else any(h)
    else:
        return any(h)
    
print(min([s2 for s2 in range(120) if game(11,s2,2,strict=False)]))
print(sorted([s2 for s2 in range(120) if not game(11,s2,1) and game(11,s2,3)][:2]))
print(min([s2 for s2 in range(120) if not game(11,s2,2) and game(11,s2,4)]))