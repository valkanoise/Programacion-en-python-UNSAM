#%% 2.16

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
# pprint(camion)
#calculo el total de costo en el camión
total = 0
for s in camion:
    total += s['cajones']*s['precio']

# print(total)


#%% 2.17

def leer_precios(nombre_archivo):
    diccionario = {}

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        # encabezado = next(f) #contiene el encabezado con el nombre de las columnas
        
        for row in rows:    # itera sobre la fila 2 en adelante sin tener en cuenta los encabezados
            # print(row)
            try:
                diccionario[row[0]] = float(row[1])
            except IndexError:
                # print ('- WARTNING - Hay elementos incompletos')
                pass
    return diccionario

precios = leer_precios('precios.csv')
# print(precios)

#%%
diferencia_total = 0.0
recaudacion = 0
for items in camion:
    # print (items['nombre'] in precios)
    
    if items['nombre'] in precios:
        # print (items['nombre'], '- cajones:', items['cajones'], 'compra:', items['precio'], 'venta:', precios[items['nombre']])
        recaudacion += items['cajones'] * precios[items['nombre']]
        # print(recaudacion)
        
diferencia_total = recaudacion - total        
        
      
print (f'El camion costó= {total:.2f}\nSe recaudaron= {recaudacion:.2f}\nDiferencia= {diferencia_total:.2f}')
        
        
        