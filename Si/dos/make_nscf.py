import sys
import os

sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")

from diamond_struct_makers import make_bulk_Si
from kpts_makers import make_auto_kpts
from param_makers import make_scf_param
from bash_makers import make_bash_beluga 

make_auto_kpts('KPTS', grid = [31, 31, 31, 0, 0, 0])
make_bulk_Si('STRUCT')
make_scf_param('PARAMS', conv_thr = 1e-10, calculation = 'nscf', ecutwfc = 60, ecutrho = 240, nat = 2, ntyp =1, nbnd = 20, occupations = 'tetrahedra')
os.system('cat PARAMS STRUCT KPTS >> nscf.in')
os.system('dos2unix nscf.in')

make_bash_beluga('nscf.sh', qe_inputfile = 'nscf.in', qe_outputfile = 'nscf.out', job_name = 'Si_nscf_dos', time = '00:30:00')
os.system('sbatch nscf.sh')

os.system('rm -f PARAMS STRUCT KPTS')


