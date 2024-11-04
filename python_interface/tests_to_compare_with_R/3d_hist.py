import numpy as np
import matplotlib.pyplot as plt

data_x = np.random.normal(0, 1, 20)
data_y = np.random.normal(1, 2, 20)

bins_x = 30
bins_y = 30

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

hist, xedges, yedges = np.histogram2d(data_x, data_y, bins=[bins_x, bins_y])

xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Высота баров
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average', edgecolor='black')

ax.set_title('3D гистограмма двух выборок')
ax.set_xlabel('Значения выборки 1')
ax.set_ylabel('Значения выборки 2')
ax.set_zlabel('Частота')

plt.show()
