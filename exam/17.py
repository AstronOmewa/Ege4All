with open('exam//17.txt','r') as f:
    a = [int(x) for x in f.readlines()]
    c = 0
    minsum = 10e10
    for i in range(len(a)-1):
        a1 = a[i]
        a2 = a[i+1]

        max21 = max(x for x in a if x%21 == 0)

        if ((a1>max21) + (a2>max21))>0:

            c+=1
            minsum = min(a1+a2,minsum)
print(c,minsum)