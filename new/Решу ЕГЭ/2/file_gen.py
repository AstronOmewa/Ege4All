import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

num = input()
is_data_required = input()
is_data_required = is_data_required == 'True' or is_data_required == '1'
q, s = open(f'Q_{num}.txt','a'), open(f'S_{num}.py','a')
s.write("import os\n\
\n\
os.chdir(os.path.dirname(os.path.abspath(__file__)))\n")

if is_data_required: dat = open(f'{os.path.dirname(os.path.abspath(__file__)).split('\\')[-1]}.{num}.txt','a')
