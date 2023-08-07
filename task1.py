

import os

def info_path(path):
    file_path, file_extension = os.path.splitext(path)
    dirc, file_name = os.path.split(file_path)
    return (dirc, file_name, file_extension)


print(info_path("C:\\картинки.jpg"))