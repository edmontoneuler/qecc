import numpy as np
import sys 

def make_Bi2Te3_QL(struc_filename, a = 4.383, vac_layer = 15, D1 = 1.70, D2 = 2.05):
    c = vac_layer + 2*D1 + 2*D2
    IL1 = D1/c
    IL2 = D2/c
    
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
    #f.write('Te  0.0000000  0.0000000 0.0000000\n')
    #f.write('Bi  0.6666667  0.3333333 ' +str(IL1) +'\n')
    #f.write('Te  0.3333333  0.6666667 ' +str(IL1 +IL2) +'\n')
    #f.write('Bi  0.0000000  0.0000000 ' +str(IL1 +2*IL2) +'\n')
    #f.write('Te  0.6666667  0.3333333 ' +str(2*IL1 +2*IL2) +'\n')

    f.write('Te  0.0000000  0.0000000 -0.002538209\n')
    f.write('Bi  0.6666667  0.3333333  0.075469618\n')
    f.write('Te  0.3333333  0.6666667  0.166666667\n')
    f.write('Bi  0.0000000  0.0000000  0.257863715\n')
    f.write('Te  0.6666667  0.3333333  0.335871542\n')


    f.close()

def make_Sb2Te3_QL(struc_filename, a = 4.25, vac_layer = 15, D1 = 1.70, D2 = 2.05):
    c = vac_layer + 2*D1 + 2*D2
    IL1 = D1/c
    IL2 = D2/c
    
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
    #f.write('Te  0.0000000  0.0000000 0.0000000\n')
    #f.write('Sb  0.6666667  0.3333333 ' +str(IL1) +'\n')
    #f.write('Te  0.3333333  0.6666667 ' +str(IL1 +IL2) +'\n')
    #f.write('Sb  0.0000000  0.0000000 ' +str(IL1 +2*IL2) +'\n')
    #f.write('Te  0.6666667  0.3333333 ' +str(2*IL1 +2*IL2) +'\n')

    f.write('Te  0.0000000  0.0000000 0.002090906\n')
    f.write('Sb  0.6666667  0.3333333 0.078599523\n')
    f.write('Te  0.3333333  0.6666667 0.166666667\n')
    f.write('Sb  0.0000000  0.0000000 0.254733810\n')
    f.write('Te  0.6666667  0.3333333 0.331242427\n')


    f.close()


def make_Bi2Se3_QL(struc_filename, a = 4.138, vac_layer = 15, D1 = 1.78, D2 =1.90 ):
    c = vac_layer + 2*D1 + 2*D2
    IL1 = D1/c
    IL2 = D2/c
    
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
    #f.write('Se  0.0000000  0.0000000 0.0000000\n')
    #f.write('Bi  0.6666667  0.3333333 ' +str(IL1) +'\n')
    #f.write('Se  0.3333333  0.6666667 ' +str(IL1 +IL2) +'\n')
    #f.write('Bi  0.0000000  0.0000000 ' +str(IL1 +2*IL2) +'\n')
    #f.write('Se  0.6666667  0.3333333 ' +str(2*IL1 +2*IL2) +'\n')

    f.write('Se  0.0000000  0.0000000 0.007052886\n')
    f.write('Bi  0.6666667  0.3333333 0.078510187\n')
    f.write('Se  0.3333333  0.6666667 0.164579713\n')
    f.write('Bi  0.0000000  0.0000000 0.250648663\n')
    f.write('Se  0.6666667  0.3333333 0.322106583\n')


    f.close()

if __name__ == "__main__":
    filename = sys.argv[1]
    make_Bi2Te3_QL(filename)
