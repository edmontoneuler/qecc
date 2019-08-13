import numpy as np
import matplotlib.pyplot as plt
import sys

def load_data(datafile):
    npz = np.load(datafile)
    a_values = npz['a_values']
    c_values = npz['c_values']
    total_E  = npz['total_E']

    return a_values, c_values, total_E

def plot_data(a_values, c_values, total_E, material_name):
    legend_entries = []
    
    plt.figure()
    for k in range(len(c_values)):
        c = c_values[k]
        line = total_E[:, k]
        legend_entries.append('c = ' + str(c))
        plt.plot(a_values, line)

    plt.xlabel('c')
    plt.ylabel('Total Energy')
    plt.title(material_name)
    plt.legend(legend_entries)
    plt.show()


if __name__ == "__main__":
    datafile = sys.argv[1]
    material_name = sys.argv[2]
    a_values, c_values, total_E = load_data(datafile)
    plot_data(a_values, c_values, total_E, material_name)
