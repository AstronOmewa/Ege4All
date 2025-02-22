from random import shuffle
m = 0
for i in range(1000):
    s = [x for x in '2'*17 + '0' * 19 + '1'*13]
    
    shuffle(s)
    s = ''.join(s)
    # s = '2'*17 + '10'*13+'0'*6
    while ('10' in s) or ('20' in s):
        if '20' in s: s = s.replace('20', '00', 1)
        else: s = s.replace('10','200',1)
    
    m = max(s.count('0'),m)

print(m)
