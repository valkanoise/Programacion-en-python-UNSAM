# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 11:47:32 2021

@author: FEFe
"""

def busqueda_lineal_lordenada(lista,e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    Esta función ordena la lista y es más eficiente, porque si encuentra
    un elemento > a e deja de seguir buscando
    '''
    lista.sort()
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        
        if z > e:
            break
        
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    
    return pos

# if __name__ == '__main__':
#     print(busqueda_lineal_lordenada([1, 4, 54, 3, 0, -1], 44))
#     print(busqueda_lineal_lordenada([1, 4, 54, 3, 0, -1], 3))
#     print(busqueda_lineal_lordenada([1, 4, 54, 3, 0, -1], 0))
#     print(busqueda_lineal_lordenada([], 42))
    
    
def busqueda_binaria(lista, x, verbose = False):
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
    
    
    
    return pos











