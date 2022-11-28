def propagar(vector):
    # encender fósforos hacia la derecha
    for i, z in enumerate(vector, start=0): # recorremos la lista
        if z == 1:   # si encontramos a e
            try:
                if vector[i+1] != -1:
                    vector[i+1] = 1
                    # pos += 1
            # da error de index por lo que agrego except
            except:
                continue
            
    # encender fósforos hacia la izquierda
    index = len(vector) - 1
    while index >0:
        if vector[index] == 1 and vector[index-1] != -1:
                vector[index-1] = 1
        index -= 1
        
    return vector

#%% otra vesion más simple

def propagar(vector):
    '''Función que recibe un vector con 0's, 1's y -1's y devuelve un vector 
    en el que los 1's se propagaron a sus vecinos con 0.'''
    
    # loop para encender fósforos hacia la derecha
    for i, z in enumerate(vector, start=0): # recorremos la lista
        if z == 1:   # si encontramos un fosforo encendido...
            try:
                if vector[i+1] == 0: # ...chequeamos que el fosforo a la derecha este apagado
                    vector[i+1] = 1  # ...si esta apagado lo encendemos
            # da error de index cuando miramos vecino de la ultima posicion
            except IndexError:
                continue
            
    # loop para encender fósforos hacia la izquierda
    # aprovecho que i está en la última posición luego del loop anterior y lo uso acá
    while i >0:
        if vector[i] == 1 and vector[i-1] == 0: # si encuentra un fosforo encendido y su vecino de la izq está apagado
                vector[i-1] = 1 # enciende el fosforo apagado
        i -= 1 # nos movemos hacia la izquiera
        
    return vector

#%% Probar funcion y chequeo los resultados con los de la clase
if __name__ == '__main__':
    prueba_1 = propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
    resultado_clase1 = [ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]
    print(f'{prueba_1}')
    print(prueba_1==resultado_clase1)
    prueba_2 = propagar([ 0, 0, 0, 1, 0, 0])
    resultado_clase2 = [1, 1, 1, 1, 1, 1]
    print(f'{prueba_2}')
    print(prueba_2 == resultado_clase2)
    