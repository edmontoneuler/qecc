import sys
import os

sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")
from scf_scrape import get_scf_dict

values = [5,7,9,11,13]# Numbers defining kpt grids used

total_energies = []
num_kpoints = []

for k in range(len(values)):
    iteration = 'k' + str(values[k])
    os.chdir(iteration)
    scf_dict = get_scf_dict('scf.out', iteration + '_pickle') #Saves data to pickle
    total_energies.append(scf_dict['total_energy'])
    #num_kpoints.append(scf_dict['nkpt'])
    os.chdir('..')

print('values = ', values)
print('Total Energies =', total_energies)
