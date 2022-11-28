def buscar_u_elemento (lista, elemento):
    '''Busca el ultimo elemento elegido de una lista'''
    ultima_pos = -1
    index = len(lista) - 1
    while index >= 0:
        if lista[index] == elemento:
            ultima_pos = index
            return ultima_pos            
        index -= 1    
    return ultima_pos


def maximo(lista):
    '''Devuelve el máximo numero de una lista'''
    m = None 
    for e in lista: 
        if m == None:
            m = e    
        elif e > m:
            m = e
    return m


def minimo(lista):
    '''Devuelve el menor número de una lista'''
    m = None 
    for e in lista:
        if m == None:
            m = e    
        elif e < m:
            m = e
    return m