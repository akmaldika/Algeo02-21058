import numpy as np
import pickle

from initialization import totalImage

def mean(images_path):
    """
    Fungsi untuk mencari matriks mean dari database.
    Mengembalikan result berupa matriks mean.
    """
    
    database_path='src/Database/database.pck'
    
    dbfile = open(database_path, 'rb')     
    db = pickle.load(dbfile)
    result = [0] * 2048
    for matrix in db:
        result = np.add(db[matrix], result)
    result = np.true_divide(result, totalImage(images_path))
    dbfile.close()

    return result