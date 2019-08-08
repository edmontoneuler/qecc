import sys
import os

sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")
from bash_makers import make_bash_beluga 

f = open('bands.in', 'w+')
f.write('&bands\n')
f.write("   prefix = 'GS'\n")
f.write("   filband = 'bands.dat'\n")
f.write("/\n") 
f.close()

os.system('dos2unix bands.in')

make_bash_beluga('bands.sh',executable = 'bands.x', qe_inputfile = 'bands.in', qe_outputfile = 'bands.out', job_name = 'get_Bi2Te3_QL_bands', time = '00:30:00')
os.system('sbatch bands.sh')



