from keras.applications.vgg16 import VGG16
from keras.applications.vgg19 import VGG19
from keras.applications import InceptionV3
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input as vgg16_pi
from keras.applications.vgg19 import preprocess_input as vgg19_pi
from keras.applications.inception_v3 import preprocess_input as iv3_pi
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

    ROOT = 'images\\'
    f = os.listdir('images')

    if model_name == "vgg19":
        base_model = VGG19(weights='imagenet')
        folder_name = 'vgg19_features\\'

        model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc2').output)

        for folder in f:
            direct = ROOT + folder + '\\'
            print(direct)

            for filename in glob.glob(direct + '*.jpg'):
                print(filename)

                img = image.load_img(filename, target_size=(224, 224))
                x = image.img_to_array(img)
                x = np.expand_dims(x, axis=0)
                x = vgg19_pi(x)

                features = model.predict(x)

                names = filename.split('\\')
                count = names[2].split('.')
                newpath = r'' + folder_name + names[1] + '\\'
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                newName = newpath + count[0] + '.npy'
                np.save(newName, features)
                #print(features.shape)
    elif model_name == "vgg16":
        base_model = VGG16(weights='imagenet')
        folder_name = 'vgg16_features\\'

        model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc2').output)

        for folder in f:
            direct = ROOT + folder + '\\'
            print(direct)

            for filename in glob.glob(direct + '*.jpg'):
                print(filename)

                img = image.load_img(filename, target_size=(224, 224))
                x = image.img_to_array(img)
                x = np.expand_dims(x, axis=0)
                x = vgg16_pi(x)

                features = model.predict(x)

                names = filename.split('\\')
                count = names[2].split('.')
                newpath = r'' + folder_name + names[1] + '\\'
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                newName = newpath + count[0] + '.npy'
                np.save(newName, features)
                #print(features.shape)

    elif model_name == 'inception':
        base_model = InceptionV3(weights='imagenet')
        folder_name = 'inceptionV3_features\\'

        model = base_model

        for folder in f:
            direct = ROOT + folder + '\\'
            print(direct)

            for filename in glob.glob(direct + '*.jpg'):
                print(filename)

                img = image.load_img(filename, target_size=(299, 299))
                x = image.img_to_array(img)
                x = np.expand_dims(x, axis=0)
                x = iv3_pi(x)

                features = model.predict(x)

                names = filename.split('\\')
                count = names[2].split('.')
                newpath = r'' + folder_name + names[1] + '\\'
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                newName = newpath + count[0] + '.npy'
                np.save(newName, features)
    else:
        print('Not support model ' + model_name)
feature_extract('inception')

