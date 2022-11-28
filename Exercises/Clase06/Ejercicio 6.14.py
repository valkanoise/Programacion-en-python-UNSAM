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
    
    # Si el elemento no fue encontrado veo dónde insertarlo
    if pos == -1:
        if izq == medio: pos = medio
        
        # Le otorga índice al nro buscado si es mayor al último de la lista
        if der == medio: pos = medio + 1
        
    return pos

if __name__ =='__main__':
    print(donde_insertar([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23], 27, True))
    print(donde_insertar([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23], 0))
    print(donde_insertar([0,2,4,6], 3))
    print(donde_insertar([0,2,4,6], 4))