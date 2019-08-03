import numpy as np
import sys 

def make_graphene(struc_filename, a = 2.460, vac_layer = 15):
    
    #Lattice vectors (Hexagonal)
    v1 = [a, 0, 0]
    v2 = [-0.5*a, 0.5*np.sqrt(3)*a, 0]
    v3 = [0, 0, vac_layer]
    
    f = open(struc_filename, 'w+')
    
    f.write('ATOMIC_SPECIES\n')
    f.write('C 12.0107 C.rel-pbesol-n-rrkjus_psl.1.0.0.UPF\n')
    f.write('\n')
    
    f.write('CELL_PARAMETERS (angstrom)\n')
    f.write('  ' +str(v1[0]) + '  ' + str(v1[1]) + '  ' + str(v1[2])+ '\n')
    f.write('   ' +str(v2[0]) + '  ' + str(v2[1]) + '  ' + str(v2[2])+ '\n')
    f.write('   0.000000'+ '  0.000000' + '  ' + str(v3[2])+ '\n')
    f.write('\n')

    f.write('ATOMIC_POSITIONS (crystal)\n')
    f.write('C  0.0000000  0.0000000 0.0000000\n')
    f.write('C  0.3333333  0.6666667 0.0000000\n')

    f.close()

def make_nitrogene(struc_filename, a = 2.270, vac_layer = 15, buckling = 0.7):
    
    #Lattice vectors (Hexagonal)
    v1 = [a, 0, 0]
    v2 = [-0.5*a, 0.5*np.sqrt(3)*a, 0]
    v3 = [0, 0, vac_layer]
    
    f = open(struc_filename, 'w+')
    
    f.write('ATOMIC_SPECIES\n')
    f.write('N 14.0067 N.pbe-n-kjpaw_psl.1.0.0.UPF\n')
    f.write('\n')
    
    f.write('CELL_PARAMETERS (angstrom)\n')
    f.write('  ' +str(v1[0]) + '  ' + str(v1[1]) + '  ' + str(v1[2])+ '\n')
    f.write('   ' +str(v2[0]) + '  ' + str(v2[1]) + '  ' + str(v2[2])+ '\n')
    f.write('   0.000000'+ '  0.000000' + '  ' + str(v3[2])+ '\n')
    f.write('\n')

    f.write('ATOMIC_POSITIONS (crystal)\n')
    f.write('N  0.3333333  0.6666667 0.5000000\n')
    f.write('N  0.6666667  0.3333333 ' + str(0.5+(buckling/vac_layer)) + '\n')
    f.close()

def make_bulk_Bi2Te3(struc_filename, d1 = 1.666, d2 =2.032 , d3 =2.764, a = 4.383, c = 30.487 ):
    
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
    f.write('Te  0.0000000  0.0000000 0.0000000\n')
    f.write('Bi  0.3333333  0.6666667 ' + str(d2/c) + '\n')
    f.write('Te  0.6666667  0.3333333 ' + str( (d1+d2)/c ) + '\n')
    
    f.write('Te  0.0000000  0.0000000 ' + str( (d1 + d2 + d3)/c) + '\n')
    f.write('Bi  0.3333333  0.6666667 ' + str( (2*d1 + d2 + d3)/c ) + '\n')
    f.write('Te  0.6666667  0.3333333 ' + str( (2*d1 + 2*d2 + d3)/c ) + '\n')
    f.write('Bi  0.0000000  0.0000000 ' + str( (2*d1 + 3*d2 + d3)/c ) + '\n')
    f.write('Te  0.3333333  0.6666667 ' + str( (3*d1 + 3*d2 + d3)/c ) + '\n')
    
    f.write('Te  0.6666667  0.3333333 ' + str( (3*d1 + 3*d2 + 2*d3)/c ) + '\n')
    f.write('Bi  0.0000000  0.0000000 ' + str( (4*d1 + 3*d2 + 2*d3)/c ) + '\n')
    f.write('Te  0.3333333  0.6666667 ' + str( (4*d1 + 4*d2 + 2*d3)/c ) + '\n')
    f.write('Bi  0.6666667  0.3333333 ' + str( (4*d1 + 5*d2 + 2*d3)/c ) + '\n')
    f.write('Te  0.0000000  0.0000000 ' + str( (5*d1 + 5*d2 + 2*d3)/c ) + '\n')
    
    f.write('Te  0.3333333  0.6666667 ' + str( (5*d1 + 5*d2 + 3*d3)/c ) + '\n')
    f.write('Bi  0.6666667  0.3333333 ' + str( (6*d1 + 5*d2 + 3*d3)/c ) + '\n')
    
    f.close()


if __name__ == "__main__":
    filename = sys.argv[1]
    make_nitrogene(filename)
