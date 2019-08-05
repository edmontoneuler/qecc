import numpy as np
import matplotlib.pyplot as plt
from scipy.io import savemat
import nltk
import sys

def get_dos_data(dat_file):
    """
    Parses the output of a Quantum Espresso
    dos.x calculation, returning a Numpy array
    containing the energy resolved DOS data.
    """
    file = open(dat_file)
    lines = file.readlines()
    fermi = float(nltk.word_tokenize(lines[0])[-2])
    num_lines = len(lines)
    
    dos_data = np.zeros((num_lines-1, 2))
    for k in range(1, num_lines):
        dos_data[k-1,0] = float(nltk.word_tokenize(lines[k])[0]) -fermi
        dos_data[k-1, 1] = float(nltk.word_tokenize(lines[k])[1])
        
    return dos_data

input_file = sys.argv[1]
material_name = sys.argv[2]

if __name__ == "__main__":
    dos_data = get_dos_data(input_file)
    savemat(material_name +'_DOS', {'DOS':dos_data})
    plt.plot(dos_data[:,0], dos_data[:,1])
    plt.xlabel('Energy (eV)')
    plt.ylabel('Density of States')
    plt.title(material_name)
    plt.show() 
