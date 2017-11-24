import os

path = "D:/ML/vegetable-detection/"
os.chdir(path)

for folder in os.walk(path + '/images/'):
    break

folders = folder[1]


for folder in folders:
    os.mkdir(path+'features/'+folder)

