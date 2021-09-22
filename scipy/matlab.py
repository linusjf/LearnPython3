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

from scipy import io as spio
a = np.ones((3, 3))
spio.savemat('file.mat', {'a': a}) # savemat expects a dictionary
data = spio.loadmat('file.mat')
print(data['a'])

a = np.ones(3)
print(a)

spio.savemat('file.mat', {'a': a})
spio.loadmat('file.mat')['a']

import imageio
arr = imageio.imread('fname.png')    
print(arr.shape)
# Matplotlib also has a similar function
import matplotlib.pyplot as plt
arr = plt.imread('fname.png')    
print(arr.shape)
