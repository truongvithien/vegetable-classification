import os

path = "D:/ML/vegetable-detection/images/"
os.chdir(path)

for folder in os.walk(path):
    break

folders = folder[1]


for folder in folders:
    child_path = path+folder
    files = os.listdir(child_path)
    i = 1
    for file in files:
        os.rename(folder + '/' + file, folder + '/' + str(i)+'.jpg')
        i = i+1

