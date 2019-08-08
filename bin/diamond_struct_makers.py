import numpy as np
import sys 
import random

def make_diamond(struc_filename, a = 3.567):
    
    v1 = [0, a/2, a/2]
    v2 = [a/2, 0, a/2]
    v3 = [a/2, a/2, 0]
    
    f = open(struc_filename, 'w+')
    
    f.write('ATOMIC_SPECIES\n')
    f.write('C 12.0107 C.pbe-n-kjpaw_psl.1.0.0.UPF\n')
    f.write('\n')
    
    f.write('CELL_PARAMETERS (angstrom)\n')
    f.write('   ' +str(v1[0]) + '  ' + str(v1[1]) + '  ' + str(v1[2])+ '\n')
    f.write('   ' +str(v2[0]) + '  ' + str(v2[1]) + '  ' + str(v2[2])+ '\n')
    f.write('   ' +str(v3[0]) + '   ' +str(v3[1])+  '   ' + str(v3[2])+ '\n')
    f.write('\n')

    f.write('ATOMIC_POSITIONS (crystal)\n')
    f.write('C   0.1250000  0.1250000 0.1250000\n')
    f.write('C   -0.1250000  -0.1250000 -0.1250000\n')

    f.close()

def make_bulk_Si(struc_filename, a = 5.431, rand_disp=0, Si1_coords = np.array([0.125, 0.125, 0.125]), Si2_coords = np.array([-0.125, -0.125, -0.125])):
    
    v1 = [0, a/2, a/2]
    v2 = [a/2, 0, a/2]
    v3 = [a/2, a/2, 0]
    
    f = open(struc_filename, 'w+')
    
    f.write('ATOMIC_SPECIES\n')
    f.write('Si 28.0855 Si.pbe-n-kjpaw_psl.1.0.0.UPF\n')
    f.write('\n')
    
    f.write('CELL_PARAMETERS (angstrom)\n')
    f.write('   ' +str(v1[0]) + '  ' + str(v1[1]) + '  ' + str(v1[2])+ '\n')
    f.write('   ' +str(v2[0]) + '  ' + str(v2[1]) + '  ' + str(v2[2])+ '\n')
    f.write('   ' +str(v3[0]) + '   ' +str(v3[1])+  '   ' + str(v3[2])+ '\n')
    f.write('\n')

    #Randomly displace atoms (for relaxation calculations)
    Si1_coords  = Si1_coords + rand_disp*np.array([random.uniform(0,1) for k in range(3)]) 
    Si2_coords  = Si2_coords + rand_disp*np.array([random.uniform(0,1) for k in range(3)]) 
    
    f.write('ATOMIC_POSITIONS (crystal)\n')
    f.write('Si   ' + str(Si1_coords[0]) + ' ' + str(Si1_coords[1]) + ' ' + str(Si1_coords[2]) + ' \n')
    f.write('Si   ' + str(Si2_coords[0]) + ' ' + str(Si2_coords[1]) + ' ' + str(Si2_coords[2]) + ' \n')
    
    f.close()

def make_bulk_Ge(struc_filename, a = 5.658):
    
    v1 = [0, a/2, a/2]
    v2 = [a/2, 0, a/2]
    v3 = [a/2, a/2, 0]
    
    f = open(struc_filename, 'w+')
    
    f.write('ATOMIC_SPECIES\n')
    f.write('Ge 72.6400 Ge.rel-pbe-dn-kjpaw_psl.1.0.0.UPF\n')
    f.write('\n')
    
    f.write('CELL_PARAMETERS (angstrom)\n')
    f.write('   ' +str(v1[0]) + '  ' + str(v1[1]) + '  ' + str(v1[2])+ '\n')
    f.write('   ' +str(v2[0]) + '  ' + str(v2[1]) + '  ' + str(v2[2])+ '\n')
    f.write('   ' +str(v3[0]) + '   ' +str(v3[1])+  '   ' + str(v3[2])+ '\n')
    f.write('\n')

    f.write('ATOMIC_POSITIONS (crystal)\n')
    f.write('Ge   0.1250000  0.1250000 0.1250000\n')
    f.write('Ge   -0.1250000  -0.1250000 -0.1250000\n')

    f.close()



if __name__ == "__main__":
    filename = sys.argv[1]
    make_diamond(filename)
