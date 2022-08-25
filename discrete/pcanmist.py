#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Importing the dataset
from sklearn.datasets import fetch_openml
mnist_data = fetch_openml('mnist_784', version = 1)
# Choosing the independent (X) and dependent variables (y)
X,y = mnist_data["data"], mnist_data["target"]
#Plotting one of the digits
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('pcanmist.pdf')
print("Setup Complete")
plt.figure(1)
#Plotting the 50000th digit
digit = X[50000]
#Reshaping the 784 features into a 28x28 matrix
digit_image = digit.reshape(28,28)
plt.imshow(digit_image, cmap='binary')
pp.savefig()
#Scaling the data
from sklearn.preprocessing import StandardScaler
scaled_mnist_data = StandardScaler().fit_transform(X)

#Applying PCA to ur dataset
from sklearn.decomposition import PCA
pca = PCA(n_components=784)
mnist_data_pca = pca.fit_transform(scaled_mnist_data)
#Calculating cumulative variance captured by PCs
import numpy as np
variance_percentage = pca.explained_variance_/np.sum(pca.
 explained_variance_)
#Calculating cumulative variance
cumulative_variance = np.cumsum(variance_percentage)

plt.figure(2)
plt.plot(cumulative_variance)
plt.xlabel('Number of principal components')
plt.ylabel('Cumulative variance explained by PCs')
plt.grid()
pp.savefig()
pp.close()
