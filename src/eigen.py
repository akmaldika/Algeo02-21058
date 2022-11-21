import numpy as np
import pickle
import os

import covareigen

def CalculateEigenface():
    """ melakukan penyimpanan nilai eigen face kedalam databse menggunakan fungsi eigen vector
    """
    database_selisih_path = 'src/Database/databaseSelisih.pck'
    database_eigenface_path = 'src/Database/databaseEigen.pck'
    
    dbfile = open(database_selisih_path, 'rb')
    db = pickle.load(dbfile)
    hasil = {}
    for value in db:
        key = value
        eigen_vector, eigen_value = covareigen.eigen(covareigen.covariance())
        hasil[key] = np.matmul(np.squeeze(np.asarray(eigen_vector)), db[value])
    dbfile.close()

    if os.path.exists(database_eigenface_path, 'ab'):
        os.remove(database_eigenface_path)
        
    dbfile = open(database_eigenface_path, 'ab')
    
    pickle.dump(hasil, dbfile)
    dbfile.close()
    
    print('Database eigenface berhasil dibuat (src/Database/databaseEigenface.pck)\n')