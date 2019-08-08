import sys
import os

sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")
from tetradymite_struct_makers import make_bulk_Bi2Te3
from kpts_makers import make_rhombo_bands
from param_makers import make_scf_param
from bash_makers import make_bash_beluga 

make_rhombo_bands('KPTS')
make_bulk_Bi2Te3('STRUCT')
make_scf_param('PARAMS', conv_thr = 1e-10,calculation = 'bands', ecutwfc = 90, ecutrho = 1080, nat = 5, ntyp =2, nbnd = 90)
os.system('cat PARAMS STRUCT KPTS >> band.in')
os.system('dos2unix band.in')

make_bash_beluga('band.sh', qe_inputfile = 'band.in', qe_outputfile = 'band.out', job_name = 'Bi2Te3_bulk_band', time = '08:00:00')
os.system('sbatch band.sh')

os.system('rm -f PARAMS STRUCT KPTS')


