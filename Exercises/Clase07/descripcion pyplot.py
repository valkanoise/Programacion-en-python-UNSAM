import numpy as np
import matplotlib.pyplot as plt

# Crea una figura nueva, de 8x6 pulgadas, con 80 puntos por pulgada
plt.figure(figsize=(8, 6), dpi=80)

# Crea un nuevo subplot, en una grilla de 1x1 (o sea, un solo plot sin subplots)
plt.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

# Plotea el coseno con una línea azul punteda de ancho 2.5 (en pixeles)
# También agregamos el nombre de la serie con 'label'
plt.plot(X, C, color="blue", linewidth=2.5, linestyle= ':', label = 'Coseno')

# Plotea el seno con una línea roja contínua de ancho 2.5 (en pixeles)
# También agregamos el nombre de la serie con 'label'
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-", label = 'Seno')

# Agregamos los rotulos arriba a la izq del grafico
plt.legend(loc='upper left') 

# Rango del eje x
plt.xlim(X.min()*1.1, X.max()*1.1)

# Ponemos marcas (ticks) en el eje x, desde -4 hasta +4 con 9 saltos
# plt.xticks(np.linspace(-4, 4, 9))
# Se agrega una lista que marca los valores que uno quiere en el eje X
# plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
# Primera lista marca los puntos en x, la segunda lista indica el rotulo en formato Latex (r'$\pi$') = Simbolo Pi
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

# Rango del eje y
plt.ylim(C.min() * 1.1, C.max() * 1.1)

# Ponemos marcas (ticks) en el eje y
# plt.yticks(np.linspace(-1, 1, 5))
# Agrego en y valores de interes y sus respectivos rotulos
plt.yticks([-1, 0, 1], [r'$-1$', r'$0$', r'$+1$'])

########################################### MOVER EJES

# Movemos el contorno (hay 4 contornos: izq, der, sup e inferior)
ax = plt.gca()  # gca es 'get current axis' ó 'tomar eje actual'
ax.spines['right'].set_color('none') # borramos la linea derecha del contorno
ax.spines['top'].set_color('none') # borramos la linea superior del contorno
ax.xaxis.set_ticks_position('bottom') # definimos la posición de los rotulos
ax.spines['bottom'].set_position(('data',0)) # el contorno inferior x lo llevamos a la posicion 0
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0)) # el contorno izquierdo y lo llevamos a la posicion 0

########################################### MARCAR PUNTOS EN EL GRAFICO
# Con la fn annotate() marcamos el punto  2pi/3 en sen, cos y agregamos flechas
# Marca la linea punteada desde x=0 hasta y=cos(2pi/3)
t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")

# Para marcar un punto usa scatter()
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')

# Le agrega rotulos al punto del cos(2pi/3) y una flecha
plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# Marca linea 2pi/3 en rojo
plt.plot([t, t],[0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
# Agrega punto rojo maranco el sen
plt.scatter([t, ],[np.sin(t), ], 50, color='red')
# Agrega rotulos y flecha
plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

###########################################
# Para agrandar los rotulos de los ejes a modo de verlos mejor

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65)) # contorno de los rotulos en x e y



# Podemos grabar el gráfico (con 72 dpi)
# plt.savefig("ejercicio_2.png)", dpi=72)

# Mostramos el resultado en pantalla
plt.show()