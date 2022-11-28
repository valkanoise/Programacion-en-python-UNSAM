import numpy as np
import matplotlib.pyplot as plt


n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)


#Calculo los angulos
T = np.arctan2(X,Y)

plt.axes([0, 0, 1, 1])
plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(min(X), max(X))
plt.xticks([])
plt.ylim(min(Y), max(Y))
plt.yticks([])

plt.show()