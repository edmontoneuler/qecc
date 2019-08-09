import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('kpt_test_data')
Ry2eV = 13.60569562
tolerance = 0.001 # 1 meV

kpt_num = data[:, 0]
total_E = data[:, 1]

delta_E = np.zeros((len(total_E)-1, 1))
for k in range(len(delta_E)):
    delta_E[k] = np.abs(total_E[-1] - total_E[k])

plt.plot(kpt_num[0:-1], Ry2eV*delta_E)
plt.plot((kpt_num[0], kpt_num[-2]), (tolerance, tolerance), 'r--')
plt.xlabel('K-point grid [X, X, X]')
plt.ylabel('Difference in total energy (eV)')
plt.show()
