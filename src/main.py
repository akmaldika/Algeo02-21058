import numpy as np
import pickle

import initialization
import selisih
import covareigen
import EigenfaceValue

# Memasukkan semua gambar yang telah dikonversi ke matriks ke dalam database (test/database.pck)
# initialization.updateDatabase()

# Menghitung selisih matriks dengan mean lalu dimasukkan ke dalam database baru (test/databaseSelisih.pck)
# selisih.selisih()

# Test display database (Untuk test aja, bisa dihapus kalo udah ok)
# print('Database')
# dbfile = open('test/database.pck', 'rb')     
# db = pickle.load(dbfile)
# for matrix in db:
#     print(matrix, '=>', db[matrix])
# dbfile.close()

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
print('\nUKURAN', len(covmat), 'x', len(covmat[0]))
dbfile.close()

# Membuat matriks vektor-vektor eigen
eigenvector, eigenvalue = covareigen.eigen(covmat)
print('\nMatriks Vektor Eigen')
print(eigenvector)
print('\nUKURAN', len(eigenvector), 'x', len(eigenvector[0]))
print('\nUKURAN', len((eigenvector).flatten()))

# Membuat matrix eigenface dan memasukkan dalam database
EigenfaceValue.CalculateEigenface()

# Test display databaseEigenface (Untuk test aja, bisa dihapus kalo udah ok)
print('\nDatabase Eigenface')
dbfile = open('test/databaseEigenface.pck', 'rb')
db = pickle.load(dbfile)
for matrix in db:
    print(matrix, '=>',db[matrix])
dbfile.close()