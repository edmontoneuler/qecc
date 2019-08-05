import sys
import os

sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")

from diamond_struct_makers import make_bulk_Si
from kpts_makers import make_auto_kpts
from param_makers import make_scf_param
from bash_makers import make_bash_beluga 

make_auto_kpts('KPTS', grid = [11,11,11,0,0,0])
make_bulk_Si('STRUCT')
make_scf_param('PARAMS', ecutwfc = 60, ecutrho = 240, nat = 2, ntyp =1, nbnd = 12)
os.system('cat PARAMS STRUCT KPTS >> scf.in')
os.system('dos2unix scf.in')

make_bash_beluga('scf.sh', job_name = 'Si_scf_dos', time = '00:30:00')
os.system('sbatch scf.sh')

os.system('rm -f PARAMS STRUCT KPTS')


