import os
import shutil

FILE_PATH = './matplotlib/seaborn/'

for file_name in os.listdir(FILE_PATH):
    print(file_name)
    if file_name.startswith('.'):
        new_file_name = file_name.replace('.', "")
        os.rename(os.path.join(FILE_PATH, file_name), os.path.join(FILE_PATH, new_file_name))
        print(f'Renamed: {file_name} to {new_file_name}')
    elif file_name.startswith('~.'):
        new_file_name = file_name.replace('~.', "")
        os.rename(os.path.join(FILE_PATH, file_name), os.path.join(FILE_PATH, new_file_name))
        print(f'Renamed: {file_name} to {new_file_name}')
