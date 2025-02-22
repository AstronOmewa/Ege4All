def conv3(x10):
    r = ''
    while x10!=0:
        r += str(x10%3)
        x10//=3

    return r[::-1]

with open("D:\\egeAll\\v52538\\17.txt") as f:
    a = [int(x) for x in f.readlines()]

    abs60 = [abs(x) for x in a if x%60 == 0]

    sum2 = sum(['2' for x in abs60 for y in str(x) if y == '2'])

    c = 0
    maxsum = 0

    for i in range(len(a) - 1):
        if ((a[i] > sum2) + (a[i+1] > sum2) )> 0:
            c += 1
            maxsum = max(maxsum, a[i]+a[i+1])


    print(c, maxsum)
