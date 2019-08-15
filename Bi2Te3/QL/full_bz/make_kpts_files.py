import numpy as np

#Real space vectors 
a = 4.365
c = 22.65

a1_hex = np.array([a, 0, 0])
a2_hex = np.array([-a/2, np.sqrt(3)*a/2, 0])
a3_hex = np.array([0, 0, c])

A_hex = np.zeros((3,3))
A_hex[:, 0] = a1_hex
A_hex[:, 1] = a2_hex
A_hex[:, 2] = a3_hex

a1_cart = np.array([a, 0, 0])
a2_cart = np.array([0, np.sqrt(3)*a, 0])
a3_cart = np.array([0, 0, c])

A_cart = np.zeros((3,3))
A_cart[:, 0] = a1_cart
A_cart[:, 1] = a2_cart
A_cart[:, 2] = a3_cart
                    
    
def get_recip_vecs(A):
    a1 = A[:, 0]
    a2 = A[:, 1]
    a3 = A[:, 2]

    volume = np.dot(a1, np.cross(a2, a3))
    
    b1 = 2*np.pi*np.cross(a2, a3)/volume
    b2 = 2*np.pi*np.cross(a3, a1)/volume
    b3 = 2*np.pi*np.cross(a1, a2)/volume
    
    B = np.zeros((3,3))
    B[:,0] = b1
    B[:,1] = b2
    B[:,2] = b3
    return B

def get_distance(v1, v2):
    # Returns distance between two points in reciprocal space
    diff = v1-v2
    return np.sqrt(diff[0]**2 + diff[1]**2 + diff[2]**2)

def get_magnitude(v1):
    # Returns magnitude of a reciprocal space vector
    return np.sqrt(v1[0]**2 + v1[1]**2 + v1[2]**2)

def get_volume(A):
    a1 = A[:,0]
    a2 = A[:,1]
    a3 = A[:,2]

    vol = np.dot(a1, np.cross(a2, a3))
    return vol

def point_in_BZ(test_point, neighbors, tolerance = 1e-12):
    distances = []
    mag = get_magnitude(test_point)
    
    for k in neighbors:
        distances.append(mag-get_distance(test_point, k)) # Positive if point lies outside BZ (i.e is closer to neighbor than to test point)
    
    if max(distances) >= tolerance:
        return False
    else:
        return True   


def get_BZ_neighbors(B):
    b1 = B[:,0]
    b2 = B[:,1]
    b3 = B[:,2]

    neighbors = []
    coeffs = [-1, 0, 1] #Are higher numbers needed for large volume ratios?

    for i in coeffs:
        for j in coeffs:
            for k in coeffs:
                if i == j == k ==0:
                    pass # Gamma point should not be included
                else:
                    neighbor = i*b1 + j*b2 + k*b3
                    neighbors.append(neighbor)
    
    return neighbors #List of nearest lattice points


def get_kpts_files(A_hex, A_cart, nkx, nky, nkz, kpts_per_file):
    B_hex = get_recip_vecs(A_hex)
    B_cart = get_recip_vecs(A_cart)
    cart2hex = np.linalg.inv(B_hex) #Change of basis matrix

    hex_BZ_vol =  get_volume(B_hex)
    cart_BZ_vol = get_volume(B_cart)
    vol_ratio = int(hex_BZ_vol/cart_BZ_vol) #Determines number of mappings to perform

    neighbors = get_BZ_neighbors(B_hex)
    mapping_vectors = get_BZ_neighbors(B_cart)

    #Form base Cartesian grid
    kx_max = B_cart[0,0]/2
    ky_max = B_cart[1,1]/2
    kz_max = B_cart[2,2]/2

    kx = np.linspace(-kx_max, kx_max, nkx)
    
    if nky ==1:
        ky = np.array([0])
    else:
        ky = np.linspace(-ky_max, ky_max, nky)
    
    if nkz ==1:
        kz = np.array([0])
    else:
        kz = np.linspace(-kz_max, kz_max, nkz)

    gamma_cell = []
    folded_cell = []

    for i in kx:
        for j in ky:
            for k in kz:
                kpoint = np.array([i, j, k]) #Point in first (Cartesian) BZ
                gamma_cell.append(kpoint)

                count = 1
                for mapvec in mapping_vectors:
                    test_point = kpoint + mapvec
                    if point_in_BZ(test_point, neighbors) and count < vol_ratio:
                        folded_cell.append(test_point)
                        count +=1
                
                if count < vol_ratio:
                    print('Point could not be mapped the requisite number of times, ', vol_ratio)


    print(len(gamma_cell))
    print(len(folded_cell))

    #Determine number of files needed
    full_bz = np.concatenate((gamma_cell, folded_cell))
    num_points = len(full_bz)
    num_files = np.ceil(num_points/kpts_per_file)

    #Write KPTS to file(s)
    for k in range(int(num_files)-1):
        filename = 'KPTS' + str(k)
        f = open(filename, 'w+')
        f.write('K_POINTS  crystal_b\n')
        f.write(str(kpts_per_file)+'\n')
        for n in range(kpts_per_file):
            kpoint = np.dot(cart2hex, full_bz[k*kpts_per_file + n])
            f.write(str(kpoint[0]) + '    ' + str(kpoint[1]) + '    '  + str(kpoint[2]) + '\n')
        f.close()

    #Last file is overwhelmingly likely to have a different number of points 

    f = open('KPTS' + str(int(num_files)-1), 'w+') # Python indexing
    points_left = int(num_points - (num_files-1)*kpts_per_file)
    f.write('K_POINTS  crystal_b\n')
    f.write(str(points_left)+'\n')
    for n in range(points_left):
        kpoint = np.dot(cart2hex, full_bz[int((num_files-1)*kpts_per_file +n)])
        f.write(str(kpoint[0]) + '    ' + str(kpoint[1]) + '    '  + str(kpoint[2]) + '\n')
    f.close() 

get_kpts_files(A_hex, A_cart, 115, 85, 1, 5000)


