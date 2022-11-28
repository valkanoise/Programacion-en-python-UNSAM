'''Escribí una función invertir_lista(lista) que dada una lista devuelva otra 
que tenga los mismos elementos pero en el orden inverso. Es decir, el que era 
el primer elemento de la lista de entrada deberá ser el último de la lista de 
salida y análogamente con los demás elementos.'''

def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    index = len(lista) - 1 # ultimo elemento de la lista
    while index >= 0:    
        invertida.append (lista[index]) #agrego a la lista invertida el ultimo elemento
        index = index - 1 # me muevo al anteultimo elemento y sucesivamente
    return invertida


#%% Otra forma

def invertir_lista(lista):
    invertida = []
    longitud = len(lista)
    i= -1
    while i >= -(longitud):
        print(i)
        invertida.append(lista[i])
        i = i - 1
        
    return invertida

#%% Prueba de a funcion invertir_lista
print(invertir_lista([1, 2, 3, 4, 5]))
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))
