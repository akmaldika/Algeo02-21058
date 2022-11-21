import numpy as np
import pickle
import os

from mean import mean

def selisih(images_path):
    """
    Fungsi untuk mencari matriks selisih antara matriks database dengan mean.
    Lalu matriks selisih dimasukkan ke dalam database baru yaitu databaseSelisih.
    """
    
    database_path='src/Database/database.pck'
    database_selisih_path='src/Database/databaseSelisih.pck'

    dbfile = open(database_path, 'rb')     
    db = pickle.load(dbfile)
    result = {}
    for matrix in db:
        names = matrix
        result[names] = np.subtract(db[matrix], mean(images_path))
    dbfile.close()

    if os.path.exists(database_selisih_path):
        os.remove(database_selisih_path)

    dbfile = open(database_selisih_path, 'ab')
      
    pickle.dump(result, dbfile)                  
    dbfile.close()

    print('Database selisih berhasil dibuat (src/Database/databaseSelisih.pck)\n')