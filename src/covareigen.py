import numpy as np

import initialization

def covariance(db):
    # menyusun matriks AT (transpose A) berdasarkan vektor-vektor database
    vector = initialization.readImage('test\Adriana Lima (1).jpg')

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