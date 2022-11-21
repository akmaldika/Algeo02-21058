import numpy as np
import pickle
import os

from initialization import readImage, totalImage

def getCovariance(images_path):
    # menyusun matriks AT (transpose A) berdasarkan vektor-vektor database
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]
    vector = readImage(files[0])

    row = totalImage(images_path)
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
    # menyusun matriks kovarians dengan L = AT*A
    L = np.dot(AT, A)

    dbfile.close()

    return L, A