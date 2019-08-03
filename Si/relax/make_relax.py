import sys
import os
sys.path.insert(0, "/scratch/m/maassenj/cmrudder/bin")

from zincblende_struct_makers import make_bulk_GaAs
from kpts_makers import make_auto_kpts
from param_makers import make_relax_param
from bash_makers import make_bash_niagara 

make_auto_kpts('KPTS', grid = [11,11,11,0,0,0])
make_bulk_GaAs('STRUCT')
make_relax_param('PARAMS', ecutwfc = 60, ecutrho = 720, nat = 2, ntyp = 2, nbnd = 16)
os.system('cat PARAMS STRUCT KPTS >> relax.in')
os.system('dos2unix relax.in')

make_bash_niagara('relax.sh',qe_inputfile = 'relax.in',qe_outputfile = 'relax.out', job_name = 'GaAs_relaxation', time = '02:00:00')
os.system('sbatch relax.sh')

os.system('rm -f PARAMS STRUCT KPTS')


