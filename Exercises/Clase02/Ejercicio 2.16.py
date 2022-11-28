import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        encabezado = next(f) #contiene el encabezado con el nombre de las columnas
        
        for row in rows:    # itera sobre la fila 2 en adelante sin tener en cuenta los encabezados
            diccionario = {}    
            diccionario['nombre'] = row[0]
            diccionario['cajones'] = int(row[1])
            diccionario['precio'] = float(row[2])
            camion.append(diccionario)
    
    return camion
        
        
camion = leer_camion('camion.csv')
pprint(camion)
#calculo el total de costo en el camión
total = 0
for s in camion:
    total += s['cajones']*s['precio']

print(total)