import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('24.6526.txt') as f:
    s = f.readline()

    s = s.replace('TAA', 'TAA A').replace('TGA', ' A').replace('TAG', " ")
    a = [(x) for x in s.split() if x[-3:] == 'TAA']
    m = 0
    for x in a:
        i = x.find('ATG')
        if i>=0:
            m = max(m, len(x[i:]))
    
    print(m)