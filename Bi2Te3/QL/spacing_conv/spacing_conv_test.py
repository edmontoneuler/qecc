import sys
import os
sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")

from QL_struct_makers import make_Bi2Te3_QL
from kpts_makers import make_auto_kpts
from param_makers import make_scf_param
from bash_makers import make_bash_beluga 

IL1_values = [1.90 + 0.005*k for k in range(4)] #Lattice Parameter Values
IL2_values = [2.05 + 0.005*k for k in range(4)] 

for j in range(len(IL1_values)):
    IL1_iteration = "IL1=" + str(IL1_values[j])
    os.system('mkdir ' + IL1_iteration)
    os.chdir(IL1_iteration)
    
    for k in range(len(IL2_values)):
        IL2_iteration = "IL2=" + str(IL2_values[k])
        os.system('mkdir ' + IL2_iteration)

        make_Bi2Te3_QL('STRUCT', IL1=IL1_values[j], IL2=IL2_values[k])
        make_auto_kpts('KPTS', grid = [11, 11, 11, 0, 0, 0])
        make_scf_param('PARAMS', pseudo_dir = '../../../PP/', ecutwfc = 90, ecutrho=1080, nat = 5, ntyp = 2, nbnd = 82)

        os.system('cat PARAMS STRUCT KPTS >> scf.in')
        os.system('dos2unix scf.in')
        os.system('mv scf.in  ' + c_iteration)

        make_bash_beluga('scf.sh', job_name = 'Bi2Te3_QL_' + IL1_iteration + '_' + IL2_iteration, time = '00:30:00')
        os.system('mv scf.sh ' + c_iteration)

        os.chdir(IL2_iteration)
        os.system('sbatch scf.sh')
        os.chdir('..')

        os.system('rm -f STRUCT PARAMS KPTS')
    
    os.chdir('..')



