import sys
import os

sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")

from QL_struct_makers import make_Bi2Te3_QL
from kpts_makers import make_auto_kpts
from param_makers import make_scf_param
from bash_makers import make_bash_beluga 

make_auto_kpts('KPTS', grid = [11,11,1,0,0,0])
make_Bi2Te3_QL('STRUCT')
make_scf_param('PARAMS', ecutwfc = 90, ecutrho = 1080, nat = 5, ntyp =2, nbnd = 82)
os.system('cat PARAMS STRUCT KPTS >> scf.in')
os.system('dos2unix scf.in')

make_bash_beluga('scf.sh', job_name = 'Bi2Te3_QL_scf_band', time = '00:30:00')
os.system('sbatch scf.sh')

os.system('rm -f PARAMS STRUCT KPTS')


