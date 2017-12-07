from keras.applications.vgg16 import VGG16
from keras.applications.vgg19 import VGG19
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
import os
import glob
from keras.models import Model

def feature_extract(model_name):
    """
    Author: Vu The Dung, Trinh Man Hoang
    :param  model_name: vgg16, vgg19
    :return:
        features were extracted and stored in to correlative folders
    :usage:
        from . import extract_deep_features as exf
        exf.feature_extract('vgg16')
    """



    if model_name == "vgg19":
        base_model = VGG19(weights='imagenet')
        folder_name = 'vgg19_features/'

<<<<<<< HEAD
    if model_name == "vgg16":
        base_model = VGG19(weights='imagenet')
        folder_name = 'vgg16_features/'
=======
    j = 0
    for filename in glob.glob(direct + '*.jpg'):
        print (filename)
>>>>>>> master

    model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc2').output)
    ROOT = 'images/'

    f = os.listdir('images')

<<<<<<< HEAD
    for folder in f:
        direct = ROOT + folder + '/'
        print(direct)
=======
        names = filename.split('\\')
        newName = 'features' + '\\' + names[1] + '\\' + str(j) + '.npy'
>>>>>>> master

        for filename in glob.glob(direct + '*.jpg'):
            print(filename)

            img = image.load_img(filename, target_size=(224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)

            features = model.predict(x)

            names = filename.split('/')
            count = names[2].split('.')
            newpath = r'' + folder_name + names[1] + '/'
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            newName = newpath + count[0] + '.npy'
            np.save(newName, features)
            #print(features.shape)

#feature_extract("vgg16")

<<<<<<< HEAD
=======
        j = j + 1

        # print (features)
>>>>>>> master
