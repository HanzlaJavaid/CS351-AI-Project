import numpy as np
import tensorflow as tf
from keras.preprocessing import image
import matplotlib.pyplot as plt

def testts(img):
    ar = image.img_to_array(img)
    ar = resize(ar,(28,28,1))
    print(ar.shape)

def Predict_image(img,model):
    labels = ['fantastic','high_five','strength','thumbs_down','thumbs_up','victory','yolo']
    ret = {}
  
    ar = image.img_to_array(img)
    ar = tf.image.resize(ar, size=(28,28), preserve_aspect_ratio=False, antialias=False, name=None)
    if(ar.shape[2]!=1):
        ar = tf.image.rgb_to_grayscale(ar, name=None) 
    r = ar
    print(ar.shape)
    ar = np.expand_dims(ar,axis=0)
    pred = model.predict(ar)
    pred = pred.flatten()
    for i in range(0,len(labels)):
        print("{} => {}".format(labels[i],pred[i]))
        ret[labels[i]] = pred[i]*100
    return r,ret
