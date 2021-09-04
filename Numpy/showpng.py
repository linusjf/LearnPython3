#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('showpng.pdf')
print("Setup Complete") 

img = plt.imread('elephant.png')
print(img.shape, img.dtype)
plt.imshow(img)

pp.savefig()
plt.savefig('plot.png')
plt.imsave('red_elephant.png', img[:,:,0], cmap=plt.cm.gray)

plt.clf()

plt.imshow(plt.imread('red_elephant.png'))
pp.savefig()
plt.clf()

import imageio
imageio.imsave('tiny_elephant.png', img[::6,::6])
plt.imshow(plt.imread('tiny_elephant.png'), interpolation='nearest')
pp.savefig()
plt.clf()

pp.close()
