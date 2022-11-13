import numpy as np
import os

import initialization

def covariance(db):
    # menyusun matriks AT (transpose A) berdasarkan vektor-vektor database
    files = [os.path.join('test', p) for p in sorted(os.listdir('test'))]
    vector = initialization.readImage(files[0])

    row = initialization.totalImage()
    col = len(vector)
    AT = np.zeros((row,col))
    
    i = 0
    for vectors in db:
        for j in range(col):
            AT[i][j] = (db[vectors])[j]
        i += 1
  
    # menyusun matriks A berdasarkan AT
    A = np.zeros((col,row))
    for i in range(col):
        for j in range(row):
            A[i][j] = AT[j][i]
    # menyusun matriks kovarians dengan C = AT*A
    C = np.dot(AT, A)

    return C

covmat = np.zeros((3,3))
covmat[0][0] = 1
covmat[0][1] = 1
covmat[1][0] = 1
covmat[1][2] = 1
covmat[2][1] = 1
covmat[2][2] = 1

# mencari nilai eigen dan vektor eigen
size = len(covmat)
# matriks Q menyimpan venktor-vektor eigen pada kolom-kolom matriks
Q = np.zeros((size,size))
# matriks R menyimpan nilai-nilai eigen pada diagonal utama matriks
R = np.zeros((size,size))
# membuat vektor U untuk mempermudah perhitungan matriks Q dan R
U = np.zeros(size)
# menyimpan nilai-nilai eigen dari matriks R
eigenvalue = np.zeros(size)


for i in range(size):

    print(f"\n current column : {i+1}")

    U = covmat[:,i]
    dU = 0
    proj1 = covmat[:,i]

    for j in range(size):

        if (i > 0):

            for k in range(i):

                dQ = 0
                proj1 = covmat[:,i]
                proj2 = Q[:,k]

                for l in range(size):
                    dQ += proj2[l]*proj2[l]
                dQ = math.sqrt(dQ)

                print(f"\nVektor projeksi")
                print(proj1)
                print(proj2)

                print(f"\nNilai pengurang U")
                print((np.dot(proj1,proj2)*proj2[j]) / (dQ*dQ))

                U[j] -= (np.dot(proj1,proj2)*proj2[j]) / (dQ*dQ)

        dU += U[j]*U[j]

    dU = math.sqrt(dU)
    
    for l in range(size):
        Q[l][i] = U[l] / dU
        if (l <= i):
            R[l][i] = np.dot(covmat[:,i], Q[:, l])
            if (l == i):
                eigenvalue[l] = R[l][i]