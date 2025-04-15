import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

folder = input('Номер по КИМ:')
num = input("Номер из скобок:")
is_data_required = input("Нужен файл с данными (1/0):")
q, s = open(f'{folder}/Q_{num}.txt','a'), open(f'{folder}/S_{num}.py','a')
s.write("import os\n\
\n\
os.chdir(os.path.dirname(os.path.abspath(__file__)))\n")
if bool(is_data_required): dat = open(f'{folder}/{folder}.{num}.txt','a')
