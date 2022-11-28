

def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    index = len(lista) - 1 # ultimo elemento de la lista
    while index >= 0:    
        invertida.append (lista[index]) #agrego a la lista invertida el ultimo elemento
        index = index - 1 # me muevo al anteultimo elemento y sucesivamente
    return invertida



#%% Prueba de a funcion invertir_lista
if __name__ == "__main__":
    print(invertir_lista([1, 2, 3, 4, 5]))
    print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))
    print(__name__)