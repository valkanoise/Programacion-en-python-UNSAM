'''Ejercicio clase 3'''

#%% 
'''A partir de un archivo csv se crea una lista con diccionarios que incluyen 
keys/values de las frutas.'''

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            camion.append(record)
          
    return camion
        


#%% 
'''Se crea un diccionario que incluye todos los precios de venta de las frutas
y sus nombres'''

def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding = 'utf-8') as f:
        rows = csv.reader(f)
        diccionario = {}
        for i, row in enumerate(rows):
            try:
                diccionario[row[0]] = float(row[1])
            except IndexError:
                print(f'Ups! No logro entender la linea {i+1}:{row}')
        return diccionario


#%% Balance compra venta

#defino las ubicaciones de los archivos para las funciones
# archivo_camion = '../Data/camion.csv'
archivo_camion = '../Data/fecha_camion.csv'
archivo_precios = '../Data/precios.csv'

# se crean los diccionarios de compra y venta
camion = leer_camion(archivo_camion)        
precios = leer_precios(archivo_precios)

# averiguo costo de compra y venta en simultáneo
costo_camion = 0.0
total_vendido = 0.0


for producto in camion:
    nombre = producto['nombre']
    cajones = int(producto['cajones'])
    costo = float(producto['precio'])
#costo del camion
    costo_camion += cajones * costo

#ganancia de lo vendido: miro el precio de los productos en el dict de precios
    precio_venta = precios[nombre]
    total_vendido += cajones * precio_venta
    
balance = total_vendido - costo_camion

print('\n\n')
print('*'*22)
print('* BALANCE VERDULERIA *')
print('*'*22)
print(f'Costo camion:{costo_camion:.2f}\nVenta: {total_vendido:.2f}\nBalance:{balance:.2f}')
