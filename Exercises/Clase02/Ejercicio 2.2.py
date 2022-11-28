'''jercicio 2.2: Lectura de un archivo de datos
Ahora que sabés leer un archivo, escribamos un programa que haga un cálculo simple 
con los datos leídos. Las columnas en camion.csv corresponden a un nombre de fruta, 
una cantidad de cajones cargados en el camión, y un precio de compra por cada cajón 
de ese grupo. Escribí un programa llamado costo_camion.py que abra el archivo, 
lea las líneas, y calcule el precio pagado por los cajones cargados en el camión. 
Ayuda: para interpretar un string s como un número entero, usá int(s). Para leerlo 
como punto flotante, usá float(s).
Tu programa debería imprimir una salida como la siguiente:

Costo total 47671.15
'''

with open('camion.csv', 'rt') as f:
    header = next(f)
    print(header) # imprime el encabezado
    
    costo_total_frutas = 0
    
    for linea in f: # itero por todas las lineas desde la segunda!
        fila = linea.split(',') # cada linea la separo usando comas y se arma una lista
        costo_fruta = int(fila[1])*float(fila[2]) # calculo el valor total de cada fruta
        costo_total_frutas = costo_total_frutas + costo_fruta # creo una variable y le voy sumando el valor total de cada fruta
        
        
print ('Costo total', costo_total_frutas)