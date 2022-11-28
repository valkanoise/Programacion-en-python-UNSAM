#%% 2.16 - Precio pagado por el productor
'''Defino función para crear una lista con varios diccionarios
adentro. Cada dict tendrá {nombre fruta, cantidad cajones, precio}'''

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        encabezado = next(f)
        print(encabezado)
        for row in rows:    # itera sobre la fila 2 en adelante sin tener en cuenta los encabezados
            d = {
                'nombre': row[0],
                'cajones': int(row[1]),
                'precio' : float(row[2])
                }
            camion.append(d)
    
    return camion
        


#%% 2.17 - Precio de venta 
'''Creo una función que creará un diccionario que incluirá los
nombres de frutas y sus precios. Si del archivo que uso para crear
el dict hay algún dato faltante o sea, IndexError la función
informa la línea del error y cuál es el contenido de esa linea'''

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
archivo_camion = '../Data/camion.csv'
archivo_precios = '../Data/precios.csv'

# se crean los diccionarios de compra y venta
camion = leer_camion(archivo_camion)        
precios = leer_precios(archivo_precios)

# averiguo costo de compra y venta en simultáneo
costo_camion = 0.0
total_vendido = 0.0


for producto in camion:
    nombre = producto['nombre']
    cajones = producto['cajones']
    costo = producto['precio']
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
