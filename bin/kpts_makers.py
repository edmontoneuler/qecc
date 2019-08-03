import numpy as np
import sys

def make_auto_kpts(filename, grid = [11,11,11, 0,0,0]):
    
    f = open(filename, 'w+')
    f.write('K_POINTS   automatic\n')
    f.write('    ' + str(grid[0]) + ' ' + str(grid[1]) + ' ' + str(grid[2]) + ' ' + str(grid[3]) + ' ' + str(grid[4]) + ' ' + str(grid[5]) + ' \n')
    f.close()

def make_diamond_bands(filename, npoints = 70):

    f = open(filename, 'w+')
    f.write('K_POINTS  crystal_b\n')
    f.write('6\n')
    f.write('0.75   0.5    0.25   ' + str(npoints) + ' # W\n') #W point
    f.write('0.5    0.0    0.0    ' + str(npoints) + ' # L\n') #L point
    f.write('0.0    0.0    0.0    ' + str(npoints) + ' # G\n') #Gamma point
    f.write('0.5    0.5    0.0    ' + str(npoints) + ' # X\n')  #X point
    f.write('0.75   0.5    0.25   ' + str(npoints) + ' # W\n') #W point
    f.write('0.75   0.375  0.375   ' + str(npoints) + ' # K\n') #K point
    f.close()

def make_2Dhex_bands(filename, npoints = 100):

    f = open(filename, 'w+')
    f.write('K_POINTS  crystal_b\n')
    f.write('4\n')
    f.write('0.0    0.0    0.0    ' + str(npoints) + ' # G\n') #Gamma point
    f.write('0.3333 0.3333 0.0    ' + str(npoints) + ' # K\n') #K point
    f.write('0.5    0.0    0.0    ' + str(npoints) + ' # M\n') #M point
    f.write('0.0    0.0    0.0    ' + str(npoints) + ' # G\n') #Gamma point
    f.close()


if __name__ == "__main__":
    filename = sys.argv[1]
    make_auto_kpts(filename)

