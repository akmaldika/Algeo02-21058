import numpy as np
import pickle
import math
import os

from covariance import getCovariance

def getEigen(covmat, diffmat):
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
    eigenvector = np.dot(diffmat, Q)
    return eigenvector, eigenvalue

def CalculateEigenface(eigenvector):
    """ melakukan penyimpanan nilai eigen face kedalam databse menggunakan fungsi eigen vector
    """
    database_selisih_path = 'src/Database/databaseSelisih.pck'
    database_eigenface_path = 'src/Database/databaseEigen.pck'
    
    dbfile = open(database_selisih_path, 'rb')
    db = pickle.load(dbfile)
    hasil = {}
    for value in db:
        key = value
        hasil[key] = np.matmul(db[value], eigenvector)
    dbfile.close()

    if os.path.exists(database_eigenface_path):
        os.remove(database_eigenface_path)
        
    dbfile = open(database_eigenface_path, 'ab')
    
    pickle.dump(hasil, dbfile)
    dbfile.close()
    
    print('Database eigenface berhasil dibuat (src/Database/databaseEigenface.pck)\n')