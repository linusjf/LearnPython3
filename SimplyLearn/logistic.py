#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import numpy as np

from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics

# The PDF document
pdf_pages = PdfPages("logistic.pdf")

digits = load_digits()

print("Image Data Shape",digits.data.shape)
print("Label Data Shape",digits.target.shape)

import numpy as np
fig = plt.figure(figsize=(8,40))

for index,(image,label) in enumerate(zip(digits.data[0:10],digits.target[0:10])):
    plt.subplot(5,2,index+1)
    plt.imshow(np.reshape(image,(8,8)),cmap=plt.cm.gray)
    plt.title("Training: %i\n" % label, fontsize = 20)

fig.tight_layout()
pdf_pages.savefig()
pdf_pages.close()

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(digits.data,digits.target,test_size = 0.23,random_state = 2)

print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)

from sklearn.linear_model import LogisticRegression
logistic_regr = LogisticRegression(max_iter=2000)
logistic_regr.fit(X_train,Y_train)
print(logistic_regr.predict(X_test[0].reshape(1,-1)))

logistic_regr.predict(X_test[0:10])

predictions = logistic_regr.predict(X_test)

score = logistic_regr.score(X_test,Y_test)
print(score)
