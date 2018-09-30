# -*- coding: utf-8 -*-
"""

"""
import os

src = 'C:\\Temp_2'

print(os.listdir(src))
dir1 = os.listdir(src)[1]
path2 = os.path.join(src,dir1)
