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

if __name__ == '__main__':
    print(busqueda_lineal_lordenada([1, 4, 54, 3, 0, -1], 44))
    print(busqueda_lineal_lordenada([1, 4, 54, 3, 0, -1], 3))
    print(busqueda_lineal_lordenada([1, 4, 54, 3, 0, -1], 0))
    print(busqueda_lineal_lordenada([], 42))