import numpy as np
import pickle
<<<<<<< Updated upstream
import os

import covareigen
=======
<<<<<<< HEAD
import math
import os
import pickle

from covariance import getCovariance

<<<<<<<< Updated upstream:src/covareigen.py
========
<<<<<<<< HEAD:src/eigen.py
def getEigen(covmat, diffmat):
========
>>>>>>>> Stashed changes:src/eigen.py
def covariance(images_path):
    # menyusun matriks AT (transpose A) berdasarkan vektor-vektor database
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    vector = initialization.readImage(files[0])

    row = initialization.totalImage(images_path)
    col = len(vector)
    AT = np.zeros((row,col))
    
    dbfile = open('src/Database/databaseSelisih.pck', 'rb') 
    db = pickle.load(dbfile)

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

    dbfile.close()

    return C

def eigen(covmat):
>>>>>>>> dd5ebe6885e4b9d6be287037d2c2b86a98854043:src/covareigen.py
    # inisialisi ukuran matriks vektor-vektor eigen
    size = len(covmat)
    # matriks Q menyimpan vektor-vektor eigen pada kolom-kolom matriks Q
    Q = np.zeros((size,size))
    # membuat vektor U, proj1, proj2, minProj untuk mempermudah perhitungan
    U = np.zeros(size)
    proj1 = np.zeros(size)
    proj2 = np.zeros(size)
    minProj = np.zeros(size)
    # menyimpan nilai-nilai eigen dari hasil perhitungan
    eigenvalue = np.zeros(size)

    # kolom pemrosesan utama
    for mainCol in range(size):
        # inisialisasi panjang vektor U = 0
        dU = 0
        # inisialisasi vektor U dan proj1 sebagai vektor kolom ke-mainCol dari matriks covmat
        for initRow in range(size):
            U[initRow] = covmat[initRow][mainCol]
            proj1[initRow] = covmat[initRow][mainCol]
        # baris pemrosesan utama
        for procRow in range(size):
            if (mainCol > 0):
                # kolom perhitungan projeksi vektor proj1 pada proj2
                for projCol in range(mainCol):
                    # inisialisasi panjang vektor proj2 = 0
                    dProj2 = 0
                    # inisialisasi vektor proj2 sebagai vektor kolom ke-projCol dari matriks 
                    for initRow in range(size):
                        proj2[initRow] = Q[initRow][projCol]
                        dProj2 += proj2[initRow]*proj2[initRow]
                    # assign nilai projeksi vektor proj1 pada vektor proj2
                    koefProj = np.dot(proj1,proj2) / dProj2
                    # assign nilai pengurang vektor U
                    minProj[procRow] += koefProj*proj2[procRow]
                # mengurangi vektor U dengan minProj
                U[procRow] -= minProj[procRow]
                # reassign elemen vektor minProj dengan 0
                minProj[procRow] = 0
            # menambahkan panjang vektor U sesuai elemen vektor U
            dU += U[procRow]*U[procRow]
        dU = math.sqrt(dU)
        # assign nilai eigen = dU (panjang vektor U)
        eigenvalue[mainCol] = dU
        # assign nilai elemen matriks Q adalah elemen vektor U dibagi panjang vektor U
        for initRow in range(size):
            Q[initRow][mainCol] = U[initRow] / dU

    Q = np.dot(diffmat, Q)
    return Q, eigenvalue
=======
import os

import covareigen
>>>>>>> dd5ebe6885e4b9d6be287037d2c2b86a98854043
>>>>>>> Stashed changes

def CalculateEigenface():
    """ melakukan penyimpanan nilai eigen face kedalam databse menggunakan fungsi eigen vector
    """
    database_selisih_path = 'src/Database/databaseSelisih.pck'
    database_eigenface_path = 'src/Database/databaseEigen.pck'
    
    dbfile = open(database_selisih_path, 'rb')
    db = pickle.load(dbfile)
    hasil = {}
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
    covMat, diffMat = getCovariance(db)
    eigenVector, eigenValue = getEigen(covMat, diffMat)
    for value in db:
        key = value
        hasil[key] = np.matmul(eigenVector, db[value])
=======
>>>>>>> Stashed changes
    for value in db:
        key = value
        eigen_vector, eigen_value = covareigen.eigen(covareigen.covariance())
        hasil[key] = np.matmul(np.squeeze(np.asarray(eigen_vector)), db[value])
<<<<<<< Updated upstream
=======
>>>>>>> dd5ebe6885e4b9d6be287037d2c2b86a98854043
>>>>>>> Stashed changes
    dbfile.close()

    if os.path.exists(database_eigenface_path, 'ab'):
        os.remove(database_eigenface_path)
        
    dbfile = open(database_eigenface_path, 'ab')
    
    pickle.dump(hasil, dbfile)
    dbfile.close()
    
<<<<<<< Updated upstream
    print('Database eigenface berhasil dibuat (src/Database/databaseEigenface.pck)\n')
=======
<<<<<<< HEAD
    print('Database eigenface berhasil dibuat (src/Database/databaseEigenface.pck)\n')
=======
    print('Database eigenface berhasil dibuat (src/Database/databaseEigenface.pck)\n')
>>>>>>> dd5ebe6885e4b9d6be287037d2c2b86a98854043
>>>>>>> Stashed changes
