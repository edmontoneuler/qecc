import sys
import os
import numpy as np

sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")
from scf_scrape import get_scf_dict


values = [4.283 + 0.025*k for k in range(8)] #Lattice Parameter Values
total_energies = []

for k in range(len(values)):
    iteration = 'alat' + str(values[k])
    os.chdir(iteration)
    scf_dict = get_scf_dict('scf.out', iteration + '_pickle') #Saves data to pickle
    total_energies.append(scf_dict['total_energy'])
    os.chdir('..')

print('values = ', values)
print('Total Energies =', total_energies)

alat_test_data = np.column_stack((values, total_energies))
np.savetxt('alat_test_data', alat_test_data)


