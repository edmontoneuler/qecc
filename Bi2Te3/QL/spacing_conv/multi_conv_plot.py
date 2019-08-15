import numpy as np
import matplotlib.pyplot as plt
import sys

def load_data(datafile):
    npz = np.load(datafile)
    D1_values = npz['D1_values']
    D2_values = npz['D2_values']
    total_E  = npz['total_E']

    return D1_values, D2_values, total_E

def plot_data(D1_values, D2_values, total_E, material_name):
    legend_entries = []
    
    plt.figure()
    for k in range(len(D2_values)):
        D2 = D2_values[k]
        line = total_E[:, k]
        legend_entries.append('D2 = ' + str(D2))
        plt.plot(D1_values, line)

    plt.xlabel('D1')
    plt.ylabel('Total Energy')
    plt.title(material_name)
    plt.legend(legend_entries)
    plt.show()


if __name__ == "__main__":
    datafile = sys.argv[1]
    material_name = sys.argv[2]
    D1_values, D2_values, total_E = load_data(datafile)
    plot_data(D1_values, D2_values, total_E, material_name)
