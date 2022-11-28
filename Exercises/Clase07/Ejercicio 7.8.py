#%% Sumar usando ciclos

def sumar_enteros(desde = 0, hasta = 0):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    
    if hasta > desde:
        
        suma = 0
        for i in range(desde,hasta+1):
            suma = suma + i
            
    else:
        suma = 0
            
    return suma

#%% Sumar usando ciclos pero con comprensión de listas

def sumar_enteros1(desde = 0, hasta = 0):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    if hasta > desde:
        
           suma = sum([i for i in range(desde,hasta+1)])

    else:
        suma = 0
            
    return suma

#%% Sumar sin ciclos

def sumar_enteros2(desde = 0, hasta = 0):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
   
    if hasta > desde:
        # Estas sumas se pueden escribir como diferencia de dos números triangulares.
        # T_hasta - T_desde-1 = suma(desde, hasta)
        desde = desde -1
        # Calculo el numero triangular
        T_hasta = hasta*(hasta+1)/2
        T_desde = desde*(desde+1)/2
        # Resto los numeros triangulares
        suma = T_hasta - T_desde
        
    else:
        suma = 0
    
    return int(suma)

#%% Pruebas

print(sumar_enteros2(14,22) == sumar_enteros(14,22))
