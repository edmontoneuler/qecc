import sys
import os

sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")

from QL_struct_makers import make_Bi2Te3_QL
from param_makers import make_scf_param
from bash_makers import make_bash_beluga 

N = 4 # Number of KPTS files

make_Bi2Te3_QL('STRUCT')
make_scf_param('PARAMS', conv_thr = 1e-10, calculation = 'nscf', ecutwfc = 90, ecutrho = 1080, nat = 5, ntyp =2, nbnd = 90, occupations = 'fixed', pseudo_dir = '../../PP')

for k in range(N):
    os.system('mkdir ' + str(k))
    os.system('cat PARAMS STRUCT KPTS' + str(k) + ' >> nscf.in')
    os.system('dos2unix nscf.in')
    os.system('mv nscf.in ' + str(k))

    os.chdir(str(k))
    make_bash_beluga('nscf.sh', qe_inputfile = 'nscf.in', qe_outputfile = 'nscf.out', job_name = 'Bi2Te3_QL_fullBZ_nscf' + str(k), time = '01:00:00')
    os.system('sbatch nscf.sh')
    os.chdir('..')

os.system('rm -f PARAMS STRUCT')


