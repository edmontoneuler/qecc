import sys
import os
sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")

from QL_struct_makers import make_Bi2Te3_QL
from kpts_makers import make_auto_kpts
from param_makers import make_scf_param
from bash_makers import make_bash_beluga 

values = [4.283 + 0.025*k for k in range(8)] #Lattice Parameter Values

make_auto_kpts('KPTS', grid = [11, 11, 1, 0, 0, 0])
make_scf_param('PARAMS', pseudo_dir = '../../PP/', ecutwfc = 90, ecutrho=1080, nat = 5, ntyp = 2, nbnd = 82)

for k in range(len(values)):
    iteration = 'alat' + str(values[k])
    os.system('mkdir ' + iteration)
    make_Bi2Te3_QL('STRUCT', a=values[k])
    os.system('cat PARAMS STRUCT KPTS >> scf.in')
    os.system('dos2unix scf.in')
    os.system('mv scf.in  ' + iteration)

    make_bash_beluga('scf.sh', job_name = 'Bi2Te3_QL_' + iteration, time = '00:30:00')
    os.system('mv scf.sh ' + iteration)

    os.chdir(iteration)
    os.system('sbatch scf.sh')
    os.chdir('..')

os.system('rm -f PARAMS STRUCT KPTS')


