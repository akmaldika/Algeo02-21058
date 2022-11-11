import pickle
import numpy as np
from initialization import totalImage

"""
Fungsi untuk mencari matriks mean dari database.
Mengembalikan result berupa matriks mean.
"""
def mean(database_path='test/database.pck'):
    dbfile = open(database_path, 'rb')     
    db = pickle.load(dbfile)
    result = [0] * 2048
    for matrix in db:
        result = np.add(db[matrix], result)
    result = np.true_divide(result, totalImage())
    dbfile.close()

    return result