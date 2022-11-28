import numpy as np
import matplotlib.pyplot as plt


# plt.axes([0, 0, 1, 1])
# Se agrega el parametro polar = True
# plt.axes([0, 0, 1, 1], polar=True)
# Otra opción
plt.axes([0, 0, 1, 1], projection = 'polar')

N = 20
theta = np.arange(0., 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)


bars = plt.bar(theta, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)