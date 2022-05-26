import os
import shutil

# The Path of the directory to be sorted
path = 'C:\\Users\\OMAR\\Downloads'
# This populates a list with the filenames in the directory
fileList = os.listdir(path)

for file_ in fileList:
    name, ext = os.path.splitext(file_)
    ext = ext[1:]
    if os.path.isdir(f'{path}/{file_}'):
        continue
    if not os.path.exists(f'{path}/{ext}'):
        os.makedirs(f'{path}/{ext}')
    shutil.move(f'{path}/{file_}', f'{path}/{ext}/{file_}')
    print(f'{file_} is moved')
