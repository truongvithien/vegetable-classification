import os
import glob


def mark_label():
    """
    Author: Trinh Man Hoang
    :param  None
    :return:
        a text file contains labels for each image in images folder
    :usage:
        from . import label_maker as lmk
        lmk.mark_label()
    """

    ROOT = 'images\\'
    f = os.listdir('images')
    label_name = 0
    for folder in f:
        direct = ROOT + folder + '\\'
        if not os.path.exists(direct):
            os.makedirs(direct)
        label_file = open(direct + str(folder) + ".txt", "w+")
        for _ in glob.glob(direct + '*.jpg'):
            label_file.write(str(label_name) + "\n")
        label_name = label_name + 1
        label_file.close()
# mark_label()