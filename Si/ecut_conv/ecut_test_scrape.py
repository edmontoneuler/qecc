import sys
import os
import numpy as np
sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")

from scf_scrape import get_scf_dict

values = [5*k +30 for k in range(8)]

total_energies = []
N = len(values)

for k in range(N):
    iteration = 'ecutwfc' + str(values[k])
    
    os.chdir(iteration)
    scf_dict = get_scf_dict('scf.out', iteration + '_pickle') 
    total_energies.append(scf_dict['total_energy'])
    
    os.chdir('..')


ecut_test_data = np.column_stack((values, total_energies))
np.savetxt('ecut_test_data', ecut_test_data)

print('ecutwfc values = ', values)
print('Total energies = ', total_energies)
