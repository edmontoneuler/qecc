import sys
import os

sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")

from QL_struct_makers import make_Bi2Te3_QL
from kpts_makers import make_auto_kpts
from param_makers import make_scf_param
from bash_makers import make_bash_beluga 

make_auto_kpts('KPTS', grid = [51, 51, 1, 0, 0, 0])
make_Bi2Te3_QL('STRUCT')
make_scf_param('PARAMS', conv_thr = 1e-10, calculation = 'nscf', ecutwfc = 90, ecutrho = 1080, nat = 5, ntyp =2, nbnd = 82, occupations = 'tetrahedra')
os.system('cat PARAMS STRUCT KPTS >> nscf.in')
os.system('dos2unix nscf.in')

make_bash_beluga('nscf.sh', qe_inputfile = 'nscf.in', qe_outputfile = 'nscf.out', job_name = 'Bi2Te3_QL_nscf_dos', time = '01:00:00')
os.system('sbatch nscf.sh')

os.system('rm -f PARAMS STRUCT KPTS')


