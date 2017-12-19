import numpy as np
import os

def get_feature(img_name, feature_type):
    """
    Author: Truong Vi Thien
    :param  img_name: "images/Chuoi_Su/4.jpg"
            feature_type: "vgg16, vgg19"
    :return:
        img_feature_name: "features/Chuoi_Su/4.npy"
        img_feature_data: [[ 0. 0. 1.340..., 0. 1.557 0. ]]
    :usage:
        from . import support_function as sf
        _, data = sf.get_feature(img_name)
    """
    img_feature_name = img_name
    img_feature_name = img_feature_name.replace("images",str(feature_type) + "_features")
    img_feature_name = img_feature_name.replace("jpg","npy")
    img_feature_name = img_feature_name.replace("JPG","npy")

    img_feature_data = np.load(img_feature_name)
    # print(img_feature_data)

    return img_feature_name, img_feature_data

def get_features_labels_from_folder(name_folder_direct, datatype, feature_type):
    """
    Author: Trinh Man Hoang
    :param  name_folder_direct: "db/db0"
            datatype: "train, dev"
            feature_type: "vgg16, vgg19 "
    :return:
        X: set of feature for ( train, dev )
        Y: set of labels correlative to X
    :usage:
        from . import support_function as sf
        X, Y = sf.get_features_labels_from_folder(name_folder_direct, ...)
    """



    db_ROOT = name_folder_direct
    name_file_direct = os.path.join(name_folder_direct, str(datatype) +".txt")
    #name_file_direct = db_ROOT + "/" + str(datatype) +".txt"
    Y = []
    X = []

    with open(name_file_direct) as name_file:
        names = name_file.read().splitlines()

    for name in names:
        X.append(get_feature(name, feature_type)[1])


    X = np.asarray(X)
    X = X.reshape((X.shape[0], X.shape[2]))

    #print(X.shape)

    label_file_direct = os.path.join(db_ROOT, "lb" + str(datatype) + ".txt")

    #label_file_direct = db_ROOT + "/" + "lb" + str(datatype) + ".txt"

    with open(label_file_direct) as label_file:
        Y = label_file.read().splitlines()

    Y = np.array(Y)
    Y = Y.reshape((1, Y.shape[0])).T
    Y = np.ravel(Y)
    #print(Y.shape)
    return X, Y

