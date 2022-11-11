import numpy as np
import os

import initialization

def covariance(db):
    # menyusun matriks AT (transpose A) berdasarkan vektor-vektor database
    files = [os.path.join('test', p) for p in sorted(os.listdir('test'))]
    vector = initialization.readImage(files[0])

    row = initialization.totalImage()
    col = len(vector)
    AT = np.zeros((row,col))
    
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
    # menyusun matriks kovarians dengan C = AT*A
    C = np.dot(AT, A)

    return C