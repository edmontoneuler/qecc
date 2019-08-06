import sys
import os

sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")
from bash_makers import make_bash_beluga 

f = open('dos.in', 'w+')
f.write(' &DOS\n')
f.write("    prefix = 'GS'\n")
f.write("    outdir = './'\n")
f.write("    filband = 'dos.dat'\n")
f.write("    Emin=-10, Emax = 30.0, DeltaE =0.02\n")
f.write(' /') 
f.close()

os.system('dos2unix dos.in')

make_bash_beluga('dos.sh',executable = 'dos.x', qe_inputfile = 'dos.in', qe_outputfile = 'dos.out', job_name = 'get_Si_dos', time = '00:30:00')
os.system('sbatch dos.sh')



