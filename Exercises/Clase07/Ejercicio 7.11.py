# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 07:39:29 2021

@author: FEFe
"""

import matplotlib.pyplot as plt


#%% Ejercicio original
fig = plt.figure()

plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja el "techo" del triangulo
plt.xticks([]), plt.yticks([]) # saca las marcas de los ejes x e y

plt.subplot(2, 2, 3) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])



plt.show()

#%% Ejercicio resuelto

fig = plt.figure()

plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja el "techo" del triangulo
plt.xticks([]), plt.yticks([]) # saca las marcas de los ejes x e y

###### Subplots de la segunda fila
# Subplot izq
# Modifico estos subplot para que haya 3 columnas en la 2da fila plt.subplot(2,3,x)
plt.subplot(2, 3, 4) # define la primera de abajo, que sería la cuarta si fuera una grilla regular de 2x3
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

#Subplot der
# Este subplot original ahora es el 5 plt.subplot(x,x,5)
plt.subplot(2, 3, 6) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

#Subplot nuevo subplot en elmedio
# Agrego subplot para que haya en la 2da fila un subplot en el medio o sea, plt.subplot(x,x,5)
plt.subplot(2, 3, 5) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot([0,1],[1,1])
plt.xticks([]), plt.yticks([])

plt.show()
