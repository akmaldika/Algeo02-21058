import numpy as np
import pickle
import cv2
import os

def readImage(image_path):
    """
    Fungsi untuk membaca gambar dengan input paramater path.
    Mengembalikan matriks dari gambar.

    args:
        image_path: string berupa relative path dari folder gambar
    """

    vector_size=32
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

def updateDatabase(images_path):
    """
    Fungsi untuk memasukkan semua matriks gambar ke dalam database.
    """

    print('Updating Database...\n')

    database_path='src/Database/database.pck'

    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    result = {}
    for f in files:
        names = f.split('/')[-1].lower()
        result[names] = readImage(f)
    
    if os.path.exists(database_path):
        os.remove(database_path)

    dbfile = open(database_path, 'ab')
      
    pickle.dump(result, dbfile)                 
    dbfile.close()

    print('Semua gambar telah dimasukkan ke dalam database (src/Database/database.pck)\n')

    return

def totalImage(images_path):
    """
    Fungsi untuk menghitung total gambar yang ada di test folder.
    """

    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    count = 0

    for f in files:
        count += 1
    
    return count