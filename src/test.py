import cv2
import numpy as np
import os
import pickle

def extract_features(image_path, vector_size=32):
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

def batch_extractor(images_path, pickled_db_path="features.npy"):
    files = [os.path.join(images_path, p) for p in sorted(os.listdir(images_path))]

    result = {}
    for f in files:
        print ('Extracting features from image %s' % f)
        names = f.split('/')[-1].lower()
        result[names] = extract_features('test\Adriana Lima0_0.jpg')
    
    # saving all our feature vectors in pickled file
    with open(pickled_db_path, 'wb') as fp:
        np.save(fp, result)

batch_extractor('test')

with open('features.npy', 'rb') as f:
    matrix = np.load(f, allow_pickle=True)
print(matrix)
matrix.names = []
matrix.matrix = []
for k, v in matrix.data.iteritems():
    matrix.names.append(k)
    matrix.matrix.append(v)
matrix.matrix = np.array(matrix.matrix)
matrix.names = np.array(matrix.names)