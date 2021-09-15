#!/usr/bin/env python

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('pcadigits.pdf')
print("Setup Complete")
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
digits = load_digits()
print(digits.data.shape)
# project from 64 to 2 dimensions
pca = PCA(2)
projected = pca.fit_transform(digits.data)
print(digits.data.shape)
print(projected.shape)
plt.scatter(projected[:, 0], projected[:, 1],
            c=digits.target, edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('nipy_spectral', 10))
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.colorbar();
pp.savefig()
pp.close()
