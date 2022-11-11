import numpy as np

def covariance(db):
    # menyusun matriks AT (transpose A) berdasarkan vektor-vektor database
    for names, vectors in db.items():
        row = len(db)
        col = len(vectors)
        AT = np.zeros((row,col))
        for i in range(row):
            AT[i] = vectors
    # menyusun matriks A berdasarkan AT
    A = np.zeros((col,row))
    for i in range(col):
        for j in range(row):
            A[i][j] = AT[j][i]
    # menyusun matriks kovarians dengan C = AT*A
    C = np.zeros((row,row))
    for i in range(row):
        for j in range(row):
            for k in range(col):
                C[i][j] += AT[i][k] * A[k][j]
    return C