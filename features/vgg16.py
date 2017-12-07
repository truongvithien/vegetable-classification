from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
import os

model = VGG16(weights='imagenet', include_top=False)

path = "D:/ML/vegetable-detection/"
os.chdir(path)

for folder in os.walk(path + '/images/'):
    break

folders = folder[1]

for folder in folders:
    child_path = path + 'images/' + folder
    files = os.listdir(child_path)
    for file in files:
        img_path = 'images/' + folder + '/' + file
        img = image.load_img(img_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        features = model.predict(x)

        print(features)


