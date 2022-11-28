
import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    ''' 
    Crea un vector con una cantidad de valores = len(largo.
    los valores posibles dentro del vector son -1, 0 y 1.
    
    Pre: Largo debe ser un valor entero > 0
    Post: Devuelve un np.array de una dimensión, o sea, un vector
    '''
    
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

def generar_caminatas(largo_caminata=100000, cantidad_caminatas=12):
    '''
    Crea una lista de caminatas(vectores). La lista esta compuesta por
    cierta_cantidad de caminatas, cada una de un largo definido por
    largo_caminata.
    
    Pre: largo_caminata y cantidad_caminatas requieren valores enteros > 0
    Post: Devuelve una lista de caminatas(vectores)

    '''
    caminatas = [randomwalk(largo_caminata) for i in range(cantidad_caminatas)]
    return caminatas


def calcular_distancias(caminatas):
    '''
    Toma una lista de caminatas(vectores) y para cada una calcula la
    distancia maxima alcanzada desde el origen. 
    Como resultado devuelve un tupla que incluye la distancia maxima desde
    el origen para esa caminata y el vector de la caminata.
    
    Pre: Se debe ingresar una lista de caminatas(vectores)
    Post: Devuelve una lista de tuplas [(distancia maxima, caminata(vector))]
    '''
    distancias_maximas = []
    for caminata in caminatas:
        tupla_dist_max = (max(abs(caminata)),caminata) # calcula la distancia max absoluta de cada caminata y arma una tupla (dis_max, vector de esa caminata)
        distancias_maximas.append(tupla_dist_max)
    return distancias_maximas
    
    


def f_principal():
    caminatas = generar_caminatas(100000,12)
    distancias = calcular_distancias(caminatas)
    
    
    # Graficar
    plt.figure(figsize=(14, 9), dpi=80)
    
    
    ###### Subplot princial de la 1era fila
    plt.subplot(2, 1, 1) 
    for caminata in caminatas:
                plt.plot(caminata)
    # plt.xlabel("Tiempo")
    plt.xticks([])
    plt.ylabel("Distancia al origen")
    plt.title("12 Caminatas al azar")
    plt.ylim(- max(distancias)[0] * 1.1, max(distancias)[0] * 1.1) # establezco max y min del eje x según la distancia máxima
    
    
    ###### Subplot 3 (izq) de la segunda fila
    
    plt.subplot(2, 2, 3) # define la primera de abajo, que sería la cuarta si fuera una grilla regular de 2x3
    # De todas las distancias selecciono la que más se aleja del origen y tomo su vector
    plt.plot(max(distancias)[1])
    plt.ylabel("Distancia al origen")
    plt.title("Caminata que más se aleja")
    plt.ylim(- max(distancias)[0] * 1.1, max(distancias)[0] * 1.1)
    plt.xticks([])
    
    
    ###### Subplot 4 (der) de la segunda fila
    
    plt.subplot(2, 2, 4) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
    # De todas las distancias selecciono la que menos se aleja del origen y tomo su vector
    plt.plot(min(distancias)[1])
    plt.xticks([])
    plt.title("Caminata que menos se aleja")
    plt.ylim(- max(distancias)[0] * 1.1, max(distancias)[0] * 1.1)
    # Agrego los rotulos en el eje y de la derecha
    ax = plt.gca()
    ax.yaxis.set_ticks_position('right')
    
    # Guardar archivo
    plt.savefig("Ejercicio 7.12.jpg", bbox_inches="tight", pad_inches=0.3, transparent=True)
    plt.show()

#%% Prueba

if __name__ == '__main__':
    f_principal()