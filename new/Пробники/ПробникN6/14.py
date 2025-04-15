for p in range(10,100):
    for x in range(1,p):
        for y in range(1,p):
            if ((8*p**3 + 9*p**2+x*p) + (x*p**3+6*p**2+x*p+4)) == (1*p**4+y*p**3+y*p**2+1*p+4):
                print(y*p**3+x*p**2+y*p**1+x)
                break