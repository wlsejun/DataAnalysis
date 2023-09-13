import os
import shutil

FILE_PATH = './pandas/'

for file_name in os.listdir(FILE_PATH):
    print(file_name)
    if file_name.startswith('_'):
        new_file_name = file_name.replace('_', "")
        os.rename(os.path.join(FILE_PATH, file_name), os.path.join(FILE_PATH, new_file_name))
        print(f'Renamed: {file_name} to {new_file_name}')
    elif file_name.startswith('[실습]Ch02.pandas'):
        new_file_name = file_name.replace('[실습]Ch02.pandas', "")
        os.rename(os.path.join(FILE_PATH, file_name), os.path.join(FILE_PATH, new_file_name))
        print(f'Renamed: {file_name} to {new_file_name}')