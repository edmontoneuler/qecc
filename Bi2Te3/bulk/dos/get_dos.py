import sys
import os

sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")
from bash_makers import make_bash_beluga 

f = open('dos.in', 'w+')
f.write('&DOS\n')
f.write("prefix = 'GS'\n")
f.write("fildos = 'dos.dat'\n")
f.write('/\n') 
f.close()

os.system('dos2unix dos.in')

make_bash_beluga('dos.sh',executable = 'dos.x', qe_inputfile = 'dos.in', qe_outputfile = 'dos.out', job_name = 'get_Bi2Te3_bulk_dos', time = '04:00:00')
os.system('sbatch dos.sh')



