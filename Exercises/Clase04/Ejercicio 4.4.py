'''Agregale a tu archivo busqueda_en_listas.py una función maximo() que busque 
el valor máximo de una lista de números positivos. Python tiene el comando max 
que ya hace esto, pero como práctica te proponemos que completes el siguiente 
código:
'''


def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = None # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if m == None:
            m = e    
        elif e > m:
            m = e
    return m

#%% Prueba de la funcion maximo
# print(maximo([1,2,7,2,3,4]))
# print(maximo([-4,-5]))

#%% Funcion que busque el menor numero de una lista

def minimo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = None # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if m == None:
            m = e    
        elif e < m:
            m = e
    return m

#%% Prueba de la funcion minimo
print(minimo([1,2,7,2,3,4,-13]))
print(minimo([-4,-5,8]))
