

def costo_camion(nombre_archivo):
    'Función para calcular el costo de las frutas en los camiones'
    with open(nombre_archivo, 'rt') as f:
        header = next(f)
        costo_total_frutas = 0
        
        for linea in f: # itero por todas las lineas desde la segunda!
            fila = linea.split(',') # cada linea la separo usando comas y se arma una lista
            costo_fruta = int(fila[1])*float(fila[2]) # calculo el valor total de cada fruta
            costo_total_frutas = costo_total_frutas + costo_fruta # creo una variable y le voy sumando el valor total de cada fruta
            
    return costo_total_frutas
            
costo = costo_camion('camion.csv')
print('Costo total:', costo)