import os
import glob

def rename():
    ROOT = 'images/'
    f = os.listdir('images')
    for folder in f:
        i = 0
        direct = ROOT + folder + '/'
        label_file = open(direct + str(folder) + ".txt", "w+")
        for filename in glob.glob(direct + '*.jpg'):
            os.rename(filename, direct + str(i) + '.jpg')
            i = i + 1
            label_file.write(str(label_name) + "\n")
        label_name = label_name + 1
        label_file.close()

def mark_label():
    ROOT = 'images/'
    f = os.listdir('images')
    label_name = 0
    for folder in f:
        direct = ROOT + folder + '/'
        label_file = open(direct + str(folder) + ".txt", "w+")
        for _ in glob.glob(direct + '*.jpg'):
            label_file.write(str(label_name) + "\n")
        label_name = label_name + 1
        label_file.close()

mark_label()