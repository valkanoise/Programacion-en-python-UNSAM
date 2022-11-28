''' En este script están las 3 formas de ordenar lista de nros, cada una 
devuelve el nro de comparaciones que realiza para ordenar las listas.
RECORDAR que las listas son mutables, por lo que si se ejecutan las funciones
las listas se veran modificadas (ordenadas)
'''
import matplotlib.pyplot as plt
import numpy as np
import random

def generar_lista(N):
    '''
    genere una lista aleatoria de largo N con números enteros del 1 al 1000 
    (puede haber repeticiones).
    '''
    
    # Genero una lista con valores desde 1 hasta 1000
    lista = list(np.array([i for i in range(1,1001)]))
    
    # Selecciono al azar y con reposición N elementos de la lista
    seleccion = random.choices(lista, k=N)
    
    return seleccion

#%%
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1

    nro_comparaciones = 0
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p, comparaciones = buscar_max(lista, 0, n)[0], buscar_max(lista, 0, n)[1]

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        # lo que hace es intercambiar posiciones, al elemento más grande de posición[p] lo pone al final con posicion [n] y viceversa, al ultimo elemento lo pone donde estaba el más grande
        lista[p], lista[n] = lista[n], lista[p]
        # print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1 para seguir iterando hacta que n = 0 y while sea False
        n = n - 1
        nro_comparaciones += comparaciones
        
    
    return nro_comparaciones

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    comparaciones = b - a
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
            
            
    return pos_max, comparaciones

#%%
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    contador_comparaciones = 0

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        contador_comparaciones += 1
        if lista[i + 1] < lista[i]:
            contador_comparaciones += reubicar(lista, i + 1)
        # print("DEBUG: ", lista)

    return contador_comparaciones

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]
    
    comparaciones = 0
    
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        comparaciones += 1
    lista[j] = v
    
    return comparaciones

#%%

def ord_burbujeo(lista):
    
    comparaciones = 0
    
    for pasada in range(len(lista)-1,0,-1):
        
        for i in range(pasada):
            comparaciones += 1
            if lista[i]>lista[i+1]:
                
                lista[i], lista[i+1] = lista[i+1], lista[i]
    
    return comparaciones
                
#%%
def experimento(N, k):
    suma_seleccion = 0
    suma_insercion = 0
    suma_burbujeo = 0
    
    for i in range (k):
            
        # 1ro genero la lista de tamaño N
        lista = generar_lista(N)
        
        # 2do ordenar la lista por los 3 metodos
        suma_seleccion += ord_seleccion(lista.copy())
        suma_insercion += ord_insercion(lista.copy())
        suma_burbujeo += ord_burbujeo(lista.copy())
    
    # 3ro devuelve los promedio de comparaciones para cada método
    return (suma_seleccion/k, suma_insercion/k, suma_burbujeo/k )


    
#%% Prueba

if __name__ == '__main__':
    # Hace gráfico que muestra las curvas de complejidad para los distintos metodos
    # de ordenamiento
    print(experimento(5,1000))
    