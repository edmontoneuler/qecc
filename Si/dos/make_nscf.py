""" make_nscf(): Creates a Quantum Espresso input file for a non self-consistent calculation

"""
import os
import sys
import re
sys.path.insert(0, "/scratch/m/maassenj/cmrudder/bin")
from kpts_makers import make_auto_kpts

def make_nscf(filename, nbnd = 100, tolvrs=1e-8,  kgrid = [51, 51, 51, 0,0,0], scf_inputfile = 'scf.in'):

    make_auto_kpts('KPTS', grid = kgrid)

    with open(scf_inputfile, 'r') as scf_inputfile:
        nscf_inputfile = open(filename, 'w')
        for num, line in enumerate(scf_inputfile, 0):
            if 'K_POINTS' in line:
                break
            if 'calculation' in line:
                nscf_inputfile.write("    calculation = 'nscf' \n")
            elif 'nbnd' in line:
                nscf_inputfile.write("    nbnd = " +str(nbnd) +" \n")
            elif 'tolvrs' in line:
                nscf_inputfile.write("    tolvrs = " +str(tolvrs) +" \n")
            else:
                nscf_inputfile.write(line)
        nscf_inputfile.close()
        scf_inputfile.close()
    
    
    os.system('cat KPTS >>' + filename)
    os.system('dos2unix '+ filename)

if __name__ == "__main__":
    filename = sys.argv[1]
    make_nscf(filename)
