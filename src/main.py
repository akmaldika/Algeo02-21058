import numpy as np
import pickle

import initialization

# Memasukkan semua gambar yang telah dikonversi ke matriks ke dalam database (test/database.pck)
initialization.updateDatabase()

# Menghitung selisih matriks dengan mean lalu dimasukkan ke dalam database baru (test/databaseSelisih.pck)
initialization.selisih()

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
dbfile.close()