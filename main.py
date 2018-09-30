# -*- coding: utf-8 -*-
"""

"""
import os

src = 'C:\\Anaconda3'
src = 'C:\Temp_2'
dst = 'E:\\'

# find the image files in source
count = 0

for folder, subfolder, file in os.walk(src):
    print('folder: ', folder)
    print('subfolder: ', subfolder)
    print('file: ', file)
    count += len(file)
    # defind image files - *.jpg
print('count files in ', src, ' = ', count)
