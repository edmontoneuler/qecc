#band_plotter.py
#
#Generates bandstructure plot from QE output data. 
#Must be run in the same folder as bands.dat.gnu (data), 
#bands.out (location of high symmetry points) and scf.out (Fermi energy)
#
#Syntax is python band_plotter.py material_name bz_path
# e.g      python band_plotter.py Silicon diamond
#

import numpy as np 
import matplotlib.pyplot as plt
import nltk
#nltk.download('punkt')
import sys

def get_sym_locs():
    """
    Returns the x-coordinates the high-symmetry points desribing the BZ path
    """
    sym_lines = []
    sym_locs = []
    with open('bands.out') as file:
        for num, line in enumerate(file,0):
            if 'high-symmetry point' in line:
                sym_lines.append(num)
        
        file = open('bands.out')
        lines = file.readlines()
        for k in sym_lines:
            sym_locs.append(float(nltk.word_tokenize(lines[k])[-1]))
    
    return sym_locs

def get_fermi_level():
    """
    Returns the Fermi level of the bandstructure as given in in the SCF output file
    """
    with open('scf.out') as file:
        for num, line in enumerate(file,0):
            if 'lowest' in line:
                fermi_line = num

        file = open('scf.out')
        lines = file.readlines()

        fermi_level = float(nltk.word_tokenize(lines[fermi_line])[-2])

    return fermi_level
    
def plot_bands(datafile= 'bands.dat.gnu',material_name = 'Si', bz_path = 'diamond'):

    sym_locs = get_sym_locs()
    fermi_level = get_fermi_level()
    my_data = np.genfromtxt(datafile)
    if bz_path == 'diamond':
        sym_labels = ['W', 'L', '$\Gamma$', 'X', 'W', 'K']
    elif bz_path == '2D_hex':
        sym_labels = ['$\Gamma$', 'K', 'M', '$\Gamma$']
    elif bz_path == 'rhombo':
        sym_labels = ['$\Gamma$', 'Z', 'F', '$\Gamma$', 'L']
    else: 
        print('Bandstructure path not recognized.')
        print('Omitting high-symmetry point labels.')
        sym_labels = [' ' for k in range(len(sym_locs))]
   
    x=[]
    y=[]

    for k in range(my_data.shape[0]):
        x.append(my_data[k][0])
        y.append(my_data[k][1]-fermi_level) #Shift values by Fermi energy
    
    plt.figure()
    plt.plot(x,y,'.')
    for k in sym_locs:
        plt.axvline(x=k, color='k')
    plt.axhline(0, color = 'r', linestyle='--')
    plt.xticks(sym_locs, sym_labels)
    plt.ylabel('Energy (eV)')
    plt.title(material_name + ' Bandstructure')
    plt.show()

if __name__ == "__main__":
    material_name = sys.argv[1]
    bz_path = sys.argv[2]
    plot_bands(material_name = material_name, bz_path = bz_path)

