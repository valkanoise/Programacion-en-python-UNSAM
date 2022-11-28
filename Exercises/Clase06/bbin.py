# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 02:08:39 2021

@author: FEFe
"""

def donde_insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq | der | medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:4d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    
    # Si el elemento no fue encontrado veo dónde debería insertarlo
    if pos == -1:
        if izq == medio: pos = medio
        
        # Le otorga índice al nro buscado si es mayor al último de la lista
        if der == medio: pos = medio + 1
        
    return pos

def insertar(lista, x):
    '''
     Función que recibe una lista ordenada y un elemento x. Si el elemento se 
     encuentra en la lista solamente devuelve su posición; si no se encuentra 
     en la lista, lo inserta en la posición correcta para mantener el orden. 
     En este segundo caso, también devuelve su posición.
     '''
    # si x está en la lista uso la funcion de arriba para buscar la posición
    # de x y la función lo devuelve.
    
    if x in lista:
        pos = donde_insertar(lista, x, verbose = False)
    
    # Si x no está en la lista, uso la fn de arriba para encontrar su index
    # y lo utiliza para agregar el elemento dentro de la lista manteniendo
    # el orden de la misma    
    else:
        pos = donde_insertar(lista, x, verbose = False)
        lista.insert(pos, x)
    
    return pos
    

if __name__ =='__main__':
    # Pruebas para fn donde_insertar
    # print(donde_insertar([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23], 27, True))
    # print(donde_insertar([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23], 0))
    # print(donde_insertar([0,2,4,6], 3))
    # print(donde_insertar([0,2,4,6], 4))
    
    # Pruebas para fn insertar
    a = [0,2,4,6]
    insertar(a, 3)
    # la lista a luego de ejecutar la función inserta el nro 3 en orden
    print(a)
    


    
    