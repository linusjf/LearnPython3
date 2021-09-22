#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scipy.io as sio
import numpy as np

#Save a mat file
vect = np.arange(10)
sio.savemat('array.mat', {'vect':vect})

#Now Load the File
mat_file_content = sio.loadmat('array.mat')
print(mat_file_content)
print(mat_file_content['vect'])

mat_file_content = sio.whosmat('array.mat')
print(mat_file_content)

# Import:
mydata = sio.loadmat('array.mat', squeeze_me=True)

print(mydata['vect'])
