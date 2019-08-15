import sys
import os
sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")

from QL_struct_makers import make_Bi2Te3_QL
from kpts_makers import make_auto_kpts
from param_makers import make_scf_param
from bash_makers import make_bash_beluga 

D1_values = [1.70 + 0.025*k for k in range(8)] # Inter-layer spacing Values
D2_values = [1.95 + 0.025*k for k in range(8)] 

for j in range(len(D1_values)):
    D1_iteration = "D1=" + str(D1_values[j])
    os.system('mkdir ' + D1_iteration)
    os.chdir(D1_iteration)
    
    for k in range(len(D2_values)):
        D2_iteration = "D2=" + str(D2_values[k])
        os.system('mkdir ' + D2_iteration)

        make_Bi2Te3_QL('STRUCT', D1=D1_values[j], D2=D2_values[k], a = 4.365)
        make_auto_kpts('KPTS', grid = [11, 11, 1, 0, 0, 0])
        make_scf_param('PARAMS', pseudo_dir = '../../../PP/', ecutwfc = 90, ecutrho=1080, nat = 5, ntyp = 2, nbnd = 82)

        os.system('cat PARAMS STRUCT KPTS >> scf.in')
        os.system('dos2unix scf.in')
        os.system('mv scf.in  ' + D2_iteration)

        make_bash_beluga('scf.sh', job_name = 'Bi2Te3_QL_' + D1_iteration + '_' + D2_iteration, time = '01:00:00')
        os.system('mv scf.sh ' + D2_iteration)

        os.chdir(D2_iteration)
        os.system('sbatch scf.sh')
        os.chdir('..')

        os.system('rm -f STRUCT PARAMS KPTS')
    
    os.chdir('..')



