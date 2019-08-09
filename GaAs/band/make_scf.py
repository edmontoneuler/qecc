import sys
import os

sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")

from zincblende_struct_makers import make_bulk_GaAs
from kpts_makers import make_auto_kpts
from param_makers import make_scf_param
from bash_makers import make_bash_beluga 

make_auto_kpts('KPTS', grid = [11,11,11,0,0,0])
make_bulk_GaAs('STRUCT')
make_scf_param('PARAMS', ecutwfc = 60, ecutrho = 720, nat = 2, ntyp =2, nbnd = 20)
os.system('cat PARAMS STRUCT KPTS >> scf.in')
os.system('dos2unix scf.in')

make_bash_beluga('scf.sh', job_name = 'GaAs_scf_band', time = '01:00:00')
os.system('sbatch scf.sh')

os.system('rm -f PARAMS STRUCT KPTS')


