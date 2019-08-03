import sys
import os

from bash_makers import make_bash_beluga 

f = open('bands.in', 'w+')
f.write(' &BANDS\n')
f.write("    prefix = 'GS'\n")
f.write("    outdir = './'\n")
f.write("    filband = 'bands.dat'\n")
f.write(' /') 
f.close()

os.system('dos2unix bands.in')

make_bash_beluga('bands.sh',executable = 'bands.x', qe_inputfile = 'bands.in', qe_outputfile = 'bands.out', job_name = 'get_Si_bands', time = '00:30:00')
os.system('sbatch bands.sh')



