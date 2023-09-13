#숫자 지우기

import os
import re

FILE_PATH = './pandas/'

print('=============')
for file_name in os.listdir(FILE_PATH):
    print(file_name)
    # 정규표현식을 사용하여 숫자 부분을 찾아 제거합니다.
    new_file_name = re.sub(r'\d+', '', file_name)
    
    if new_file_name != file_name:
        os.rename(os.path.join(FILE_PATH, file_name), os.path.join(FILE_PATH, new_file_name))
        print(f'Renamed: {file_name} to {new_file_name}')
