import numpy as np
import os
import glob

ROOT = 'z:\\Subjects\\ML\\BaiTap\\images\\'

f = os.listdir('z:\\Subjects\\ML\\BaiTap\\images')

for folder in f:
    
    i = 0
    direct = ROOT + folder + '\\'
    print(direct)
    for filename in glob.glob(direct + '*.jpg'):
        os.rename(filename, direct + str(i) + '.jpg')
        i = i + 1