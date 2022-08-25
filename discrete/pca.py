#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width',500)
dataset = pd.read_csv('pizza.csv')
print(dataset.head())
print(dataset.corr())
# Dropping the brand name column before standardizing the data
df_num = dataset.drop(["brand"], axis=1)
# Setting the brand name column as the target variable
target = dataset['brand']
#Scaling the data (Step 1)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(df_num)
scaled_data = scaler.transform(df_num)
#Applying PCA to the scaled data
from sklearn.decomposition import PCA
#Reducing the dimensions to 2 components so that we can have a 
 # 2D visualization
pca = PCA(n_components = 2)
pca.fit(scaled_data)
#Applying to our scaled dataset
scaled_data_pca = pca.transform(scaled_data)
#Check the shape of the original dataset and the new dataset
print("The dimensions of the original dataset is: ", scaled_data.shape)
print("The dimensions of the dataset after performing PCA is: ", scaled_data_pca.shape)

#Plotting the principal components
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages
pp = PdfPages('pca.pdf')
print("Setup Complete")

sns.scatterplot(x=scaled_data_pca[:,0], y=scaled_data_pca[:,1], 
hue=target)
plt.legend(loc="best")
plt.gca().set_aspect("equal")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
pp.savefig()
pp.close()
