import sys
import os
sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")

from tetradymite_struct_makers import make_bulk_Bi2Te3
from kpts_makers import make_auto_kpts
from param_makers import make_scf_param
from bash_makers import make_bash_beluga 

a_values = [4.283 + 0.05*k for k in range(4)] #Lattice Parameter Values
c_values = [30.387 + 0.05*k for k in range(4)] 

for j in range(len(a_values)):
    a_iteration = "a=" + str(a_values[j])
    os.system('mkdir ' + a_iteration)
    os.chdir(a_iteration)
    
    for k in range(len(c_values)):
        c_iteration = "c=" + str(c_values[k])
        os.system('mkdir ' + c_iteration)

        make_bulk_Bi2Te3('STRUCT', a=a_values[j], c=c_values[k])
        make_auto_kpts('KPTS', grid = [11, 11, 11, 0, 0, 0])
        make_scf_param('PARAMS', pseudo_dir = '../../../PP/', ecutwfc = 90, ecutrho=1080, nat = 5, ntyp = 2, nbnd = 82)

        os.system('cat PARAMS STRUCT KPTS >> scf.in')
        os.system('dos2unix scf.in')
        os.system('mv scf.in  ' + c_iteration)

        make_bash_beluga('scf.sh', job_name = 'Bi2Te3_bulk_' + a_iteration + '_' + c_iteration, time = '04:00:00')
        os.system('mv scf.sh ' + c_iteration)

        os.chdir(c_iteration)
        os.system('sbatch scf.sh')
        os.chdir('..')

        os.system('rm -f STRUCT PARAMS KPTS')
    
    os.chdir('..')



