import numpy as np
import pickle

import initialization
import selisih
import covareigen

# Memasukkan semua gambar yang telah dikonversi ke matriks ke dalam database (test/database.pck)
initialization.updateDatabase()

# Menghitung selisih matriks dengan mean lalu dimasukkan ke dalam database baru (test/databaseSelisih.pck)
selisih.selisih()

# Test display database (Untuk test aja, bisa dihapus kalo udah ok)
print('Database')
dbfile = open('test/database.pck', 'rb')     
db = pickle.load(dbfile)
for matrix in db:
    print(matrix, '=>', db[matrix])
dbfile.close()

# Test display databaseSelisih (Untuk test aja, bisa dihapus kalo udah ok)
print('\nDatabase Selisih')
dbfile = open('test/databaseSelisih.pck', 'rb')     
db = pickle.load(dbfile)
for matrix in db:
    print(matrix, '=>', db[matrix])

# Membuat matriks kovarians dari database
covmat = covareigen.covariance(db)
print('\nMatriks Kovarian')
print(covmat)
dbfile.close()

# Membuat matriks vektor-vektor eigen
eigenvector, eigenvalue = covareigen.eigen(covmat)
print('\nMatriks Vektor Eigen')
print(eigenvector)