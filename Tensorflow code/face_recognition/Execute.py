import tensorflow as tf
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

# DIR = 'Capture\\ Capture.png'
DIR = 'test_14.png'
path = 'Dataset'

def get_lables(directory):
  labels = list()
  for subdir in os.listdir(directory):
	  path = subdir
	  labels.append(path)
  return labels

labels = get_lables(path)
print(labels)

def prepare(filepath):
  IMG_SIZE = 130
  img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
  img_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
  return img_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

def Recognize():
  model = tf.keras.models.load_model("Face_Detection.h5")

  prediction = model.predict([prepare(DIR)])
  predicted_class = np.argmax(prediction[0])
  return(labels[predicted_class])