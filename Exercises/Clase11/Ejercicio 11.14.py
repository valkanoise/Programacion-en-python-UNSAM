import matplotlib.pyplot as plt
import numpy as np

def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b

# Datos X
superficie = np.array([150.0, 120.0, 170.0, 80.0])
# Datos Y
alquiler = np.array([35.0, 29.6, 37.4, 21.0])


# Se grafican los alquileres vs superficie
g = plt.scatter(x = superficie, y = alquiler)
plt.title('gráfico de dispersión de los datos')
plt.xlabel('Superficie (metros cuadrados)')
plt.ylabel('Alquiles (miles de pesos)')

# Se buscan los parametros a y b de la recta de cuadrados minimos
a, b = ajuste_lineal_simple(superficie, alquiler)

# Se grafica la recta de ajuste lineal
grilla_x = np.linspace(start = min(superficie), stop = max(superficie)+10, num = 10)
grilla_y = grilla_x*a + b
plt.plot(grilla_x, grilla_y, c = 'green')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

errores = alquiler - (a*superficie + b)
# print(errores)
print("ECM:", (errores**2).mean())