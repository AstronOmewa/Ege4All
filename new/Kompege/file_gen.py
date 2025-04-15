import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

folder = input('Номер по КИМ:')
num = input("Номер из скобок:")
names = input("Нужен файл с данными (1/0):")
q, s = open(f'{os.path.dirname(os.path.abspath(__file__))}/{folder}/Q_{num}.txt','w'), open(f'{folder}/S_{num}.py','w')

s.write("import os\n\
\n\
os.chdir(os.path.dirname(os.path.abspath(__file__)))\n")
if names=='1': dat = open(f'{folder}/{folder}.{num}.txt','w')
elif (names!='0'): dat = [open(f'{folder}/{folder}.{num}_{name}.txt','w') for name in names.split()]


