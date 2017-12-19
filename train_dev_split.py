import glob
import os

from sklearn.model_selection import train_test_split


def one_random_split(dev_size):
    """
    Author: Trinh Man Hoang
    :param  dev_size : size of dev_set < 1
    :return:
        X_train, X_dev, Y_train, Y_dev respectively
    :usage:
        from . import train_dev_split as spl
        X, Y = spl.one_random_split(devsize)
    """

    i_l_ROOT = 'images'
    f = os.listdir(i_l_ROOT)


    X = []
    Y = []

    for folder in f:
        direct = os.path.join(i_l_ROOT, folder)
        l_direct = os.path.join(direct,folder + ".txt")

        with open(l_direct) as label_file:
            label_list = label_file.read().splitlines()

        file_list = glob.glob(os.path.join(direct, '*.jpg'))
        for i in range(len(file_list)):
            X.append(file_list[i])
            Y.append(label_list[i])

    X_train, X_dev, Y_train, Y_dev = train_test_split(X, Y, test_size=dev_size)



    return X_train, X_dev, Y_train, Y_dev


def k_split_sample(k_set, size):
    """
    Author: Trinh Man Hoang
    :param  k_set: #train_split sets
            dev_size : size of dev_set < 1
    :return:
        k_set folders (in db_Root) contains random splitting
    :usage:
        from . import train_dev_split as spl
        spl.k_split_sample(kset, devsize)
    """


    db_ROOT = 'db'
    db_ROOT = os.path.abspath(db_ROOT)

    for k in range(k_set):

        db_direct = os.path.join(db_ROOT, "db" + str(k) + "/")
        #db_direct = db_ROOT + "db" + str(k) + "/"
        if not os.path.exists(db_direct):
            os.makedirs(db_direct)
        else:
            trash_files = os.listdir(db_direct)
            for trash in trash_files:
                os.remove(db_direct + trash)

        train_file = open(db_direct + "train.txt", "w+")
        val_file = open(db_direct + "val.txt", "w+")
        dev_file = open(db_direct + "dev.txt", "w+")
        lbtrain_file = open(db_direct + "lbtrain.txt", "w+")
        lbval_file = open(db_direct + "lbval.txt", "w+")
        lbdev_file = open(db_direct + "lbdev.txt", "w+")

        X_train, X_dev, Y_train, Y_dev = one_random_split(dev_size= size)

        for i in range(len(X_train)):
             train_file.write(X_train[i] + "\n")
             lbtrain_file.write(Y_train[i] + "\n")

        for i in range(len(X_dev)):
             dev_file.write(X_dev[i] + "\n")
             lbdev_file.write(Y_dev[i] + "\n")

        train_file.close()
        val_file.close()
        dev_file.close()
        lbtrain_file.close()
        lbval_file.close()
        lbdev_file.close()

k_split_sample(5, 0.33)
