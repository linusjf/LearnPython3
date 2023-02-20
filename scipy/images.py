#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy import misc
from scipy import ndimage
from imageio import imwrite
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp = PdfPages("images.pdf")
print("Setup Complete")

f = misc.face(gray=False)
# uses the Image module (PIL)
imwrite("face.png", f)

plt.imshow(f)
pp.savefig()
plt.clf()

print(f.mean(), f.max(), f.min())
face = misc.face(gray=True)
lx, ly = face.shape
# Cropping
crop_face = face[lx // 4 : -lx // 4, ly // 4 : -ly // 4]
plt.imshow(crop_face)
pp.savefig()
plt.clf()

face = misc.face()
flip_ud_face = np.flipud(face)
plt.imshow(flip_ud_face)
pp.savefig()
plt.clf()

rotate_face = ndimage.rotate(face, 45)
plt.imshow(rotate_face)
pp.savefig()
plt.clf()

blurred_face = ndimage.gaussian_filter(face, sigma=3)
plt.imshow(blurred_face)
pp.savefig()
plt.clf()

im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1
im[90:-90, 90:-90] = 2
im = ndimage.gaussian_filter(im, 8)

plt.imshow(im)
pp.savefig()
plt.clf()

sx = ndimage.sobel(im, axis=0, mode="constant")
sy = ndimage.sobel(im, axis=1, mode="constant")
sob = np.hypot(sx, sy)

plt.imshow(sob)
pp.savefig()
plt.clf()

pp.close()
