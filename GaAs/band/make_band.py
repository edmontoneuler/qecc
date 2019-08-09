import sys
import os

sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")
from zincblende_struct_makers import make_bulk_GaAs
from kpts_makers import make_diamond_bands
from param_makers import make_scf_param
from bash_makers import make_bash_beluga 

make_diamond_bands('KPTS', npoints = 200)
make_bulk_GaAs('STRUCT')
make_scf_param('PARAMS', conv_thr = 1e-10,calculation = 'bands', ecutwfc = 60, ecutrho = 720, nat = 2, ntyp =2, nbnd = 24)
os.system('cat PARAMS STRUCT KPTS >> band.in')
os.system('dos2unix band.in')

make_bash_beluga('band.sh', qe_inputfile = 'band.in', qe_outputfile = 'band.out', job_name = 'GaAs_band', time = '00:30:00')
os.system('sbatch band.sh')

os.system('rm -f PARAMS STRUCT KPTS')


