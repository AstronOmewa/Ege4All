import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def tr(x):
    a = ''
    while x>0:
        a+=str(x%3)
        x//=3
    return a[::-1]

print(tr(81**18-(81**8-1)*(9**8+1)//8-8).count('1'))