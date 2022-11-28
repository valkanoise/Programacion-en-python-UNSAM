import csv
''' Es un mÃ³dulo que facilita trabajar con archivos csv. Maneja directamente
las comillas y las , por lo que no es necesario hacer split de la lineas durante
su iteraciÃ³n para separar los elementos de cada lÃ­nea'''

def costo_camion(nombre_archivo):
    'FunciÃ³n para calcular el costo de las frutas en los camiones'
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f) # con este comando se crea un elemento que se puede iterar entre sus lineas ya preparadas como listas separadas por comas
        encabezado = next(filas)
        costo_total_frutas = 0
        
        for fila in filas: # itero por todas las lineas desde la segunda!
            try: #pruebo calcular cantidad de cajones y costo de todos los cajones por fruta
                costo_fruta = int(fila[1])*float(fila[2]) # calculo el valor total de cada fruta
                costo_total_frutas = costo_total_frutas + costo_fruta # creo una variable y le voy sumando el valor total de cada fruta
            except ValueError: #si alguna fruta tiene faltantes en cantidad de cajones o precios imprime quÃ© fruta no tiene los datos
                print(f'WARNING! La fruta {fila[0]} tiene datos faltantes')
    return costo_total_frutas
            
costo = costo_camion('Data/missing.csv')
print('Costo total:', costo)
