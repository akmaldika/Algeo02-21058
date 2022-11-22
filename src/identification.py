import numpy
from mean import *

def getNewEigenface(image_input, image_path, eigenvector):
    selisih = image_input - mean(image_path)
    testface = numpy.dot(selisih, eigenvector)
    min = 999
    name = None

    database_eigenface_path = 'src/Database/databaseEigen.pck'

    dbfile = open(database_eigenface_path, 'rb')
    db = pickle.load(dbfile)
    for value in db:
        hasil = np.subtract(testface, db[value])
        sum = 0
        for i in range(len(hasil)):
            sum += numpy.power(hasil[i], 2)
        distance = numpy.sqrt(sum)
        if (distance < min):
            min = distance
            if (distance < 10):
                name = value
            
    dbfile.close()

    return name, min