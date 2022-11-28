import random
import matplotlib.pyplot as plt
import numpy as np


def generar_lista(n, m):
    '''
    Devuelve una lista ordenada de n elementos unicos enteros diferentes 
    elegidos al azar entre 0 y m-1
    '''

    l = random.sample(range(m), k = n)
    l.sort()
    return l


def generar_elemento(m):
    '''
    Devuelve un elemento entero aleatorio entre 0 y m- 1.
    '''
    return random.randint(0, m-1)


def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps


def experimento_secuencial_promedio(lista, m, k):
    '''Función que calcula la cantidad de comparaciones promedio en 
    k experimentos elementales donde en cada experimento se busca el 
    elemento m generado al azar dentro de la lista también generada al azar.
    '''
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1] # cuenta el numero de comparaciones totales realizadas 

    comps_prom = comps_tot / k
    return comps_prom


def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve como resultado una tupla (posición , nro de comparaciones)
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista.

    '''
    
    if verbose:
        print(f'[DEBUG] izq | der | medio | Comps.')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    # Agrego variable para contar el nro de operaciones/comparaciones
    comparaciones = 0
    while izq <= der:
        comparaciones += 1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:4d} |{medio:6d} | {comparaciones:5d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            break # si encuentra al elemento termina la busqueda
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    
    return pos , comparaciones


def experimento_binario_promedio(lista, m, k):
    '''Función que calcula la cantidad de comparaciones promedio en 
    k experimentos elementales donde en cada experimento se busca el 
    elemento m generado al azar dentro de la lista también generada al azar.
    '''
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1] # cuenta el numero de comparaciones totales realizadas 

    comps_prom = comps_tot / k
    return comps_prom



    
#%% Prueba función de busqueda_binaria

# if __name__ =='__main__':
    # print(busqueda_binaria([1, 3, 5], 0, verbose = True))
    # print(busqueda_binaria([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],18, verbose = True))
    # print(busqueda_binaria([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],11, verbose = True))
    


#%% 
'''
Funcion que a partir de los parámetros m y K genere un experimento y su 
gráficocomparando ambos algoritmos de búsqueda.
'''

def graficar_bbin_vs_bseq(m=10000, k=1000):
    
    largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
    comps_promedio_secuencial = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
    comps_promedio_binario = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

    for i, n in enumerate(largos):
        lista = generar_lista(n, m) # genero lista de largo n
        comps_promedio_secuencial[i] = experimento_secuencial_promedio(lista, m, k)
        comps_promedio_binario[i] = experimento_binario_promedio(lista, m, k)
    
    # ahora grafico largos de listas contra operaciones promedio de búsqueda.
    # grafico el promedio de las busquedas secuenciales
    plt.plot(largos,comps_promedio_secuencial, label = 'Búsqueda secuencial')
    # tambien grafico el promedio de las busquedas binarias
    plt.plot(largos,comps_promedio_binario, label = 'Búsqueda binaria')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.xlim(0,250) 
    # achiqué el eje x para poder apreciar mejor la serie de búsqueda binaria
    plt.ylim(0,50) 
    plt.legend()
    # Desactivo el pt.show() para que aparezcan los dos graficos juntos
    # plt.show()
    
#%% Prueba

if __name__ == '__main__':
    graficar_bbin_vs_bseq(m=10000, k=1000)