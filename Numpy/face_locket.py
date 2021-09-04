#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('face_locket.pdf')
print("Setup Complete")

# 2D grayscale image
face = misc.face(gray=True)
plt.imshow(face)
pp.savefig()
plt.clf()
plt.imshow(face, cmap=plt.cm.gray)
pp.savefig()
plt.clf()
crop_face = face[100:-100, 100:-100]
sy, sx = face.shape
# x and y indices of pixels
y, x = np.ogrid[0:sy, 0:sx] 
y.shape, x.shape

# center of the image
circleface = face.copy()
centerx, centery = (660, 300) 
# circle
mask = (y - centery)**2 + (x - centerx)**2 > 230**2 
circleface[mask] = 0
plt.imshow(circleface)
pp.savefig()
plt.clf()

# ellipse
ellipseface = face.copy()
a,b = (430,230)
mask = ((y - centery)/b)**2 + ((x - centerx)/a)**2 > 1 
ellipseface[mask] = 0
plt.imshow(ellipseface)
pp.savefig()
plt.clf()

# ellipse
a,b = (230,430)
mask = ((y - centery)/b)**2 + ((x - centerx)/a)**2 > 1 
face[mask] = 0
plt.imshow(face)
pp.savefig()
plt.clf()
pp.close()
