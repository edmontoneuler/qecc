import numpy as np
import sys 
import random

def make_Bi2Te3_QL(struc_filename, a = 4.383, vac_layer = 15, D1 = 1.70, D2 = 2.05, rand_disp = 0):
    c = vac_layer + 2*D1 + 2*D2
    IL1 = D1/c
    IL2 = D2/c

    #Atomic coordinates (x-y fixed by hex symmetries)
    Te2a_coords = np.array([2/3, 1/3, IL1+IL2])
    Bi1a_coords = np.array([1/3, 2/3, IL1])
    Te1_coords = np.array([0, 0, 0])
    Bi1b_coords = np.array([2/3, 1/3, -IL1])
    Te2b_coords = np.array([1/3, 2/3, -IL1 - IL2])

    #Randomly displace atomic coordinates
    Te2a_coords = Te2a_coords + rand_disp*np.array([random.uniform(0,1) for k in range(3)])
    Bi1a_coords = Bi1a_coords+ rand_disp*np.array([random.uniform(0,1) for k in range(3)])
    Te1_coords = Te1_coords #+ rand_disp*np.array([random.uniform(0,1) for k in range(3)])
    Bi1b_coords = Bi1b_coords + rand_disp*np.array([random.uniform(0,1) for k in range(3)])
    Te2b_coords = Te2b_coords + rand_disp*np.array([random.uniform(0,1) for k in range(3)])

    #Lattice vectors (Hexagonal)
    v1 = [a, 0, 0]
    v2 = [-0.5*a, 0.5*np.sqrt(3)*a, 0]
    v3 = [0, 0, c]
    
    f = open(struc_filename, 'w+')
    
    f.write('ATOMIC_SPECIES\n')
    f.write('Bi 208.9804 Bi.rel-pbe-dn-kjpaw_psl.1.0.0.UPF\n')
    f.write('Te 127.600 Te.rel-pbe-dn-kjpaw_psl.1.0.0.UPF\n')
    f.write('\n')
    
    f.write('CELL_PARAMETERS (angstrom)\n')
    f.write('  ' +str(v1[0]) + '  ' + str(v1[1]) + '  ' + str(v1[2])+ '\n')
    f.write('   ' +str(v2[0]) + '  ' + str(v2[1]) + '  ' + str(v2[2])+ '\n')
    f.write('   0.000000'+ '  0.000000' + '  ' + str(v3[2])+ '\n')
    f.write('\n')

    f.write('ATOMIC_POSITIONS (crystal)\n')
    f.write('Te    ' + str(Te2a_coords[0]) + ' ' +  str(Te2a_coords[1]) +  ' ' +  str(Te2a_coords[2]) +'\n')
    f.write('Bi    ' + str(Bi1a_coords[0]) + ' ' +  str(Bi1a_coords[1]) +  ' ' +  str(Bi1a_coords[2]) +'\n')
    f.write('Te    ' + str(Te1_coords[0]) + ' ' +  str(Te1_coords[1]) +  ' ' +  str(Te1_coords[2]) +'\n')
    f.write('Bi    ' + str(Bi1b_coords[0]) + ' ' +  str(Bi1b_coords[1]) +  ' ' +  str(Bi1b_coords[2]) +'\n')
    f.write('Te    ' + str(Te2b_coords[0]) + ' ' +  str(Te2b_coords[1]) +  ' ' +  str(Te2b_coords[2]) +'\n')

    f.close()

def make_Sb2Te3_QL(struc_filename, a = 4.25, vac_layer = 15, D1 = 1.70, D2 = 2.05, rand_disp=0):

    c = vac_layer + 2*D1 + 2*D2
    IL1 = D1/c
    IL2 = D2/c
    
    #Atomic coordinates (x-y fixed by hex symmetries)
    Te2a_coords = np.array([2/3, 1/3, IL1+IL2])
    Sb1a_coords = np.array([1/3, 2/3, IL1])
    Te1_coords = np.array([0, 0, 0])
    Sb1b_coords = np.array([2/3, 1/3, -IL1])
    Te2b_coords = np.array([1/3, 2/3, -IL1 - IL2])

    #Randomly displace atomic coordinates
    Te2a_coords = Te2a_coords + rand_disp*np.array([random.uniform(0,1) for k in range(3)])
    Sb1a_coords = Sb1a_coords+ rand_disp*np.array([random.uniform(0,1) for k in range(3)])
    Te1_coords = Te1_coords #+ rand_disp*np.array([random.uniform(0,1) for k in range(3)])
    Sb1b_coords = Sb1b_coords + rand_disp*np.array([random.uniform(0,1) for k in range(3)])
    Te2b_coords = Te2b_coords + rand_disp*np.array([random.uniform(0,1) for k in range(3)])

    #Lattice vectors (Hexagonal)
    v1 = [a, 0, 0]
    v2 = [-0.5*a, 0.5*np.sqrt(3)*a, 0]
    v3 = [0, 0, c]
    
    f = open(struc_filename, 'w+')
    
    f.write('ATOMIC_SPECIES\n')
    f.write('Sb 121.7600 Sb.rel-pbe-n-kjpaw_psl.1.0.0.UPF\n')
    f.write('Te 127.6000 Te.rel-pbe-dn-kjpaw_psl.1.0.0.UPF\n')
    f.write('\n')
    
    f.write('CELL_PARAMETERS (angstrom)\n')
    f.write('  ' +str(v1[0]) + '  ' + str(v1[1]) + '  ' + str(v1[2])+ '\n')
    f.write('   ' +str(v2[0]) + '  ' + str(v2[1]) + '  ' + str(v2[2])+ '\n')
    f.write('   0.000000'+ '  0.000000' + '  ' + str(v3[2])+ '\n')
    f.write('\n')

    f.write('ATOMIC_POSITIONS (crystal)\n')
    f.write('Te    ' + str(Te2a_coords[0]) + ' ' +  str(Te2a_coords[1]) +  ' ' +  str(Te2a_coords[2]) +'\n')
    f.write('Sb    ' + str(Sb1a_coords[0]) + ' ' +  str(Sb1a_coords[1]) +  ' ' +  str(Sb1a_coords[2]) +'\n')
    f.write('Te    ' + str(Te1_coords[0]) + ' ' +  str(Te1_coords[1]) +  ' ' +  str(Te1_coords[2]) +'\n')
    f.write('Sb    ' + str(Sb1b_coords[0]) + ' ' +  str(Sb1b_coords[1]) +  ' ' +  str(Sb1b_coords[2]) +'\n')
    f.write('Te    ' + str(Te2b_coords[0]) + ' ' +  str(Te2b_coords[1]) +  ' ' +  str(Te2b_coords[2]) +'\n')

    #f.write('ATOMIC_POSITIONS (crystal)\n')
    #f.write('Te  0.0000000  0.0000000 0.0000000\n')
    #f.write('Sb  0.6666667  0.3333333 ' +str(IL1) +'\n')
    #f.write('Te  0.3333333  0.6666667 ' +str(IL1 +IL2) +'\n')
    #f.write('Sb  0.0000000  0.0000000 ' +str(IL1 +2*IL2) +'\n')
    #f.write('Te  0.6666667  0.3333333 ' +str(2*IL1 +2*IL2) +'\n')

    f.close()


def make_Bi2Se3_QL(struc_filename, a = 4.138, vac_layer = 15, D1 = 1.78, D2 =1.90 ):
    c = vac_layer + 2*D1 + 2*D2
    IL1 = D1/c
    IL2 = D2/c
    
    #Atomic coordinates (x-y fixed by hex symmetries)
    Se2a_coords = np.array([2/3, 1/3, IL1+IL2])
    Bi1a_coords = np.array([1/3, 2/3, IL1])
    Se1_coords = np.array([0, 0, 0])
    Bi1b_coords = np.array([2/3, 1/3, -IL1])
    Se2b_coords = np.array([1/3, 2/3, -IL1 - IL2])

    #Randomly displace atomic coordinates
    Se2a_coords = Te2a_coords + rand_disp*np.array([random.uniform(0,1) for k in range(3)])
    Bi1a_coords = Bi1a_coords+ rand_disp*np.array([random.uniform(0,1) for k in range(3)])
    Se1_coords = Te1_coords #+ rand_disp*np.array([random.uniform(0,1) for k in range(3)])
    Bi1b_coords = Bi1b_coords + rand_disp*np.array([random.uniform(0,1) for k in range(3)])
    Se2b_coords = Te2b_coords + rand_disp*np.array([random.uniform(0,1) for k in range(3)])

    #Lattice vectors (Hexagonal)
    v1 = [a, 0, 0]
    v2 = [-0.5*a, 0.5*np.sqrt(3)*a, 0]
    v3 = [0, 0, c]
    
    f = open(struc_filename, 'w+')
    
    f.write('ATOMIC_SPECIES\n')
    f.write('Bi 208.9804 Bi.rel-pbe-dn-kjpaw_psl.1.0.0.UPF\n')
    f.write('Se  78.9600 Se.rel-pbe-dn-kjpaw_psl.1.0.0.UPF\n')
    f.write('\n')
    
    f.write('CELL_PARAMETERS (angstrom)\n')
    f.write('  ' +str(v1[0]) + '  ' + str(v1[1]) + '  ' + str(v1[2])+ '\n')
    f.write('   ' +str(v2[0]) + '  ' + str(v2[1]) + '  ' + str(v2[2])+ '\n')
    f.write('   0.000000'+ '  0.000000' + '  ' + str(v3[2])+ '\n')
    f.write('\n')

    f.write('ATOMIC_POSITIONS (crystal)\n')
    f.write('Se    ' + str(Se2a_coords[0]) + ' ' +  str(Se2a_coords[1]) +  ' ' +  str(Se2a_coords[2]) +'\n')
    f.write('Bi    ' + str(Bi1a_coords[0]) + ' ' +  str(Bi1a_coords[1]) +  ' ' +  str(Bi1a_coords[2]) +'\n')
    f.write('Se    ' + str(Se1_coords[0])  + ' ' +  str(Se1_coords[1])  +  ' ' +  str(Se1_coords[2]) +'\n')
    f.write('Bi    ' + str(Bi1b_coords[0]) + ' ' +  str(Bi1b_coords[1]) +  ' ' +  str(Bi1b_coords[2]) +'\n')
    f.write('Se    ' + str(Se2b_coords[0]) + ' ' +  str(Se2b_coords[1]) +  ' ' +  str(Se2b_coords[2]) +'\n')

    #f.write('Se  0.0000000  0.0000000 0.007052886\n')
    #f.write('Bi  0.6666667  0.3333333 0.078510187\n')
    #f.write('Se  0.3333333  0.6666667 0.164579713\n')
    #f.write('Bi  0.0000000  0.0000000 0.250648663\n')
    #f.write('Se  0.6666667  0.3333333 0.322106583\n')

    f.close()

if __name__ == "__main__":
    filename = sys.argv[1]
    make_Bi2Te3_QL(filename)
