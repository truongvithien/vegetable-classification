import numpy as np
import os
from sklearn.model_selection import  train_test_split


def load_feature_label():
    ROOT = 'features/'
    iROOT = 'images/'
    f = os.listdir('features')
    X = []
    Y = []

    for folder in f:
        direct = ROOT + folder + '/'
        i_direct = iROOT + folder + '/'
        i_direct = i_direct + folder + ".txt"

        feature_files = os.listdir(direct)
        for feature in feature_files:
            temp = np.load(direct + feature)
            X.append(temp)
            with open(i_direct) as label_file:
                Y.append(int(label_file.readline().replace('\n','')))

    X = np.array(X)
    X = X.reshape((X.shape[0], X.shape[2]))
    Y = np.array(Y)
    Y = Y.reshape((1, Y.shape[0])).T
    return X,Y


X,Y = load_feature_label()
X_train, X_dev, y_train, y_dev = train_test_split(X, Y, test_size=0.2)

print(X_train.shape)
print(X_dev.shape)