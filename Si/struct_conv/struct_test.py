import sys
import os
sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")

from diamond_struct_makers import make_bulk_Si
from kpts_makers import make_auto_kpts
from param_makers import make_scf_param
from bash_makers import make_bash_beluga 

values = [5.331 + 0.025*k for k in range(8)] #Lattice Parameter Values

make_auto_kpts('KPTS', grid = [11, 11, 11, 0, 0, 0])
make_scf_param('PARAMS', pseudo_dir = '../../PP/', ecutwfc = 60, ecutrho=240, nat = 2, ntyp = 1, nbnd = 16)

for k in range(len(values)):
    iteration = 'alat' + str(values[k])
    os.system('mkdir ' + iteration)
    make_bulk_Si('STRUCT', a=values[k])
    os.system('cat PARAMS STRUCT KPTS >> scf.in')
    os.system('dos2unix scf.in')
    os.system('mv scf.in  ' + iteration)

    make_bash_beluga('scf.sh', job_name = 'Bulk_Si_' + iteration, time = '00:20:00')
    os.system('mv scf.sh ' + iteration)

    os.chdir(iteration)
    os.system('sbatch scf.sh')
    os.chdir('..')

os.system('rm -f PARAMS STRUCT KPTS')


