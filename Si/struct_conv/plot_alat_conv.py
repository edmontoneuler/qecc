import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('alat_test_data')

alat= data[:, 0]
total_E = data[:, 1]


plt.plot(alat, total_E, 'ko')
plt.plot(alat, total_E, 'k--')
plt.xlabel('Lattice Parameter')
plt.ylabel('Total Energy (Ry)')
plt.show()
