import sys
import os

sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")
from diamond_struct_makers import make_bulk_Si
from kpts_makers import make_auto_kpts
from param_makers import make_relax_param
from bash_makers import make_bash_beluga 

make_auto_kpts('KPTS', grid = [11,11,11,0,0,0])
make_bulk_Si('STRUCT', rand_disp = 0.001) #Random displacement of atomic coordinates
make_relax_param('PARAMS', ecutwfc = 60, ecutrho = 240, nat = 2, ntyp = 1, nbnd = 12)
os.system('cat PARAMS STRUCT KPTS >> relax.in')
os.system('dos2unix relax.in')

make_bash_beluga('relax.sh',qe_inputfile = 'relax.in',qe_outputfile = 'relax.out', job_name = 'Si_relaxation', time = '00:30:00')
os.system('sbatch relax.sh')

os.system('rm -f PARAMS STRUCT KPTS')


