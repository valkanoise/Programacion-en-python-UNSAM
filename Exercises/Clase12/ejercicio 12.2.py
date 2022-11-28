# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 20:40:32 2021

@author: Usuario
"""

def ord_burbujeo(lista):
    for pasada in range(len(lista)-1,0,-1):
        for i in range(pasada):
            if lista[i]>lista[i+1]:
                # hago asignación simultánea en una sola fila, intercambio [i] con [i+1] si i menor a i+1
                lista[i], lista[i+1] = lista[i+1], lista[i]
                
#%% Prueba
if __name__ == '__main__':
        
    lista_1 = [1, 2, -3, 8, 1, 5]
    ord_burbujeo(lista_1)
    print(lista_1)
    
    
    lista_2 = [1, 2, 3, 4, 5]
    ord_burbujeo(lista_2)
    print(lista_2)
    
    
    lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
    ord_burbujeo(lista_3)
    print(lista_3)
    

    lista_4 = [10, 8, 6, 2, -2, -5]
    ord_burbujeo(lista_4)
    print(lista_4)
    
    
    lista_5 = [2, 5, 1, 0]
    ord_burbujeo(lista_5)
    print(lista_5)
