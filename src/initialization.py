import cv2
import numpy as np
import os
import pickle

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

def updateDatabase(images_path='test', database_path='test/database.pck'):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    result = {}
    for f in files:
        if (f != 'test\database.pck'):
            print ('Membaca gambar %s' % f)
            names = f.split('/')[-1].lower()
            result[names] = readImage(f)
    
    # saving all our feature vectors in pickled file
    dbfile = open(database_path, 'ab')
      
    # source, destination
    pickle.dump(result, dbfile)                     
    dbfile.close()

    print('Semua gambar telah dimasukkan ke dalam database\n')

def totalImage(images_path='test'):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    count = 0

    for f in files:
        count += 1
    
    return count-1