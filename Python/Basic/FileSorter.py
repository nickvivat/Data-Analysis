import os, shutil

path = r"C:/Users/Nickv/Downloads/"

for file in os.listdir(path):
    if '.pdf' in file:
        shutil.move(path + file, path + "pdf/" + file)
