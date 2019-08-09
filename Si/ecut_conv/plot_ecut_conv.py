import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('ecut_test_data')
Ry2eV = 13.60569562
tolerance = 0.001 # 1meV

ecutwfc = data[:, 0]
total_E = data[:, 1]

delta_E = np.zeros((len(total_E)-1, 1))
for k in range(len(delta_E)):
    delta_E[k] = np.abs(total_E[-1] - total_E[k])

plt.plot(ecutwfc[0:-1], Ry2eV*delta_E)
plt.plot((ecutwfc[0], ecutwfc[-2]), (tolerance, tolerance), 'r--')
plt.xlabel('ecutwfc (Ry)')
plt.ylabel('Difference in total energy (eV)')
plt.show()


