#!/usr/bin/env python
import numpy as np
from patsy import dmatrix
from matplotlib import pyplot as plt
from matplotlib import cm

from mpl_toolkits.mplot3d.axes3d import Axes3D

x1 = np.linspace(0., 1., 100)
x2 = np.linspace(0., 1., 100)
x1, x2 = np.meshgrid(x1, x2)
df = 3
y = dmatrix("te(cr(x1, df), cc(x2, df)) - 1", {"x1": x1.ravel(), "x2": x2.ravel(), "df": df})
print(y.shape)

fig = plt.figure()

fig.suptitle("Tensor product basis example (2 covariates)");

for i in range(df * df):
   ax = fig.add_subplot(df, df, i + 1, projection='3d')
   yi = y[:, i].reshape(x1.shape)
   ax.plot_surface(x1, x2, yi, rstride=4, cstride=4, alpha=0.15)
   ax.contour(x1, x2, yi, zdir='z', cmap=cm.coolwarm, offset=-0.5)
   ax.contour(x1, x2, yi, zdir='y', cmap=cm.coolwarm, offset=1.2)
   ax.contour(x1, x2, yi, zdir='x', cmap=cm.coolwarm, offset=-0.2)
   ax.set_xlim3d(-0.2, 1.0)
   ax.set_ylim3d(0, 1.2)
   ax.set_zlim3d(-0.5, 1)
   ax.set_xticks([0, 1])
   ax.set_yticks([0, 1])
   ax.set_zticks([-0.5, 0, 1])

#fig.tight_layout()

plt.savefig("tensors.png")
