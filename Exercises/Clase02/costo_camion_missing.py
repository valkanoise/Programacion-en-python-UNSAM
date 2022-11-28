

def costo_camion(nombre_archivo):
    'Función para calcular el costo de las frutas en los camiones'
    with open(nombre_archivo, 'rt') as f:
        header = next(f)
        costo_total_frutas = 0
        
        for linea in f: # itero por todas las lineas desde la segunda!
            fila = linea.split(',') # cada linea la separo usando comas y se arma una lista
            try: #pruebo calcular cantidad de cajones y costo de todos los cajones por fruta
                costo_fruta = int(fila[1])*float(fila[2]) # calculo el valor total de cada fruta
                costo_total_frutas = costo_total_frutas + costo_fruta # creo una variable y le voy sumando el valor total de cada fruta
            except ValueError: #si alguna fruta tiene faltantes en cantidad de cajones o precios imprime qué fruta no tiene los datos
                print(f'La fruta {fila[0]} tiene datos faltantes')
    return costo_total_frutas
            
costo = costo_camion('Data/missing.csv')
print('Costo total:', costo)