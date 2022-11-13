import pickle
import os
import numpy as np
from mean import mean

def selisih():
    """
    Fungsi untuk mencari matriks selisih antara matriks database dengan mean.
    Lalu matriks selisih dimasukkan ke dalam database baru yaitu databaseSelisih.
    """
    
    database_path='test/database.pck'
    database_selisih_path='test/databaseSelisih.pck'

    dbfile = open(database_path, 'rb')     
    db = pickle.load(dbfile)
    result = {}
    for matrix in db:
        names = matrix
        result[names] = np.subtract(db[matrix], mean())
    dbfile.close()

    if os.path.exists(database_selisih_path):
        os.remove(database_selisih_path)

    dbfile = open(database_selisih_path, 'ab')
      
    pickle.dump(result, dbfile)                  
    dbfile.close()

    print('Database selisih berhasil dibuat (test/databaseSelisih.pck)\n')