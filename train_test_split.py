import numpy as np
import os
import glob

def k_fold_split(k, drirectory):
    ROOT = 'images\\'

    f = os.listdir('images')

    for folder in f:
