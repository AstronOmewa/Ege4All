import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

num = input()
is_data_required = input()
q, s = open(f'Q_{num}.txt','a'), open(f'S_{num}.py','a')
s.write("import os\n\
\n\
os.chdir(os.path.dirname(os.path.abspath(__file__)))\n")
if is_data_required: dat = open(f'26.{num}.txt','a')
