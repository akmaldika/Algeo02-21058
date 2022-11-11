import cv2
import numpy as np
import os
import pickle

"""
Fungsi untuk membaca gambar dengan input paramater path.
Mengembalikan matriks dari gambar.
"""
def readImage(image_path, vector_size=32):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    alg = cv2.KAZE_create()
    # Dinding image keypoints
    kps = alg.detect(image)
    # Getting first 32 of them. 
    # Number of keypoints is varies depend on image size and color pallet
    # Sorting them based on keypoint response value(bigger is better)
    kps = sorted(kps, key=lambda x: -x.response)[:vector_size]
    # computing descriptors vector
    kps, dsc = alg.compute(image, kps)
    # Flatten all of them in one big vector - our feature vector
    dsc = dsc.flatten()
    # Making descriptor of same size
    # Descriptor vector size is 64
    needed_size = (vector_size * 64)
    if dsc.size < needed_size:
        # if we have less the 32 descriptors then just adding zeros at the
        # end of our feature vector
        dsc = np.concatenate([dsc, np.zeros(needed_size - dsc.size)])
    return dsc

"""
Fungsi untuk memasukkan semua matriks gambar ke dalam database.
"""
def updateDatabase(images_path='test', database_path='test/database.pck'):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    result = {}
    for f in files:
        if (f != 'test\database.pck') and (f != 'test\databaseSelisih.pck'):
            print ('Membaca gambar %s' % f)
            names = f.split('/')[-1].lower()
            result[names] = readImage(f)
    
    if os.path.exists(database_path):
        os.remove(database_path)

    dbfile = open(database_path, 'ab')
      
    pickle.dump(result, dbfile)                 
    dbfile.close()

    print('Semua gambar telah dimasukkan ke dalam database (test/database.pck)\n')

"""
Fungsi untuk menghitung total gambar yang ada di test folder.
"""
def totalImage(images_path='test'):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    count = 0

    for f in files:
        count += 1
    
    return count-1