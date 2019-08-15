import sys
import os
import numpy as np

sys.path.insert(0, "/home/cmrudder/scratch/qecc/bin")
from scf_scrape import get_scf_dict

D1_values = [1.70 + 0.025*k for k in range(8)] # Inter-layer spacing Values
D2_values = [1.95 + 0.025*k for k in range(8)] 

total_E = np.zeros((len(D1_values), len(D2_values)))

for j in range(len(D1_values)):
    D1_iteration = "D1=" + str(D1_values[j])
    os.chdir(D1_iteration)

    for k in range(len(D2_values)):
        D2_iteration = "D2=" + str(D2_values[k])
        os.chdir(D2_iteration)
        scf_dict = get_scf_dict('scf.out', D1_iteration + D2_iteration + '_pickle') #Saves data to pickle
   
        total_E[j, k] = scf_dict['total_energy']
        os.chdir('..')

    os.chdir('..')


D1_values = np.array(D1_values)
D2_values = np.array(D2_values)

np.savez('spacing_conv_data.npz', D1_values=D1_values, D2_values=D2_values, total_E=total_E)

