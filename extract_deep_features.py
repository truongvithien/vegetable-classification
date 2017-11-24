from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
import os
import glob
from keras.models import Model


base_model = VGG16(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc2').output)
ROOT = 'images\\'

f = os.listdir('images')

for folder in f:
    direct = ROOT + folder + '\\'
    print(direct)

    j = 0
    for filename in glob.glob(direct + '*.jpg'):
        print (filename)

        img = image.load_img(filename, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        features = model.predict(x)

        names = filename.split('\\')
        newName = 'features' + '\\' + names[1] + '\\' + str(j) + '.npy'

        np.save (newName, features)

        j = j + 1

        # print (features)
