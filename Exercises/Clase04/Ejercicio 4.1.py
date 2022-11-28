#%% Ejercicio original con error

def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i = len(lista)
    while i > 0:    # tomo el último elemento 
        i = i-1
        invertida.append (lista.pop(i))  #
    return invertida

l = [1, 2, 3, 4, 5]    
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')


#%% Ejercicio corregido
''' El error estaba en la linea 9, dado que lista.pop(i) es un metodo de las 
listas el cual saca el elemento i de la lista y lo devuelve.
Para solucionarlo se saca lista.pop(i) y se reemplaza por lista[i] y ahora
la lista no se va reduciendo en elementos luego de cada ciclo'''

def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i = len(lista)
    while i > 0:    # tomo el último elemento 
        i = i-1
        invertida.append (lista[i])  #
    return invertida

l = [1, 2, 3, 4, 5]    
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')