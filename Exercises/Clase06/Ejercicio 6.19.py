


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
            
            #Le agrego el break para que NO HAGA todas las comparaciones si encuentra el número x
            break # si encuentra al elemento termina la busqueda
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    
    return pos , comparaciones

#%% Prueba

if __name__ =='__main__':
    print(busqueda_binaria([1, 3, 5], 0, verbose = True))
    print(busqueda_binaria([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],18, verbose = True))
    print(busqueda_binaria([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23],11, verbose = True))