#%%

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        encabezado = next(f)
        for row in rows:    # itera sobre la fila 2 en adelante sin tener en cuenta los encabezados
            d = {
                'nombre': row[0],
                'cajones': int(row[1]),
                'precio' : float(row[2])
                }
            camion.append(d)
    
    return camion
        


#%% 2.17 - Precio de venta 


def leer_precios(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding = 'utf-8') as f:
        rows = csv.reader(f)
        diccionario = {}
        for i, row in enumerate(rows):
            try:
                diccionario[row[0]] = float(row[1])
            except IndexError:
                pass
        return diccionario


#%% Ejercicio 3.13: Recolectar datos
'''Funcion para recolectar los datos necesarios para imprimir la tabla.
La funcion devuelve una tupla (nombre fruta, cajones, precio compra, diferencia venta-compra)'''

def hacer_informe(lista_cajones, precios):
    lista = []
    for dic in lista_cajones:    # itera sobre la fila 2 en adelante sin tener en cuenta los encabezados
            tupla = (
                dic['nombre'],
                dic['cajones'],
                dic['precio'],
                precios[dic['nombre']] - dic['precio']
                )
            lista.append(tupla)
    return lista
    

#%% Balance compra venta

#defino las ubicaciones de los archivos para las funciones
archivo_camion = '../Data/camion.csv'
archivo_precios = '../Data/precios.csv'

# se crean los diccionarios de compra y venta
camion = leer_camion(archivo_camion)        
precios = leer_precios(archivo_precios)

# averiguo costo de compra y venta en simultÃ¡neo
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

# print('\n\n')
# print('*'*22)
# print('* BALANCE VERDULERIA *')
# print('*'*22)
# print(f'Costo camion:{costo_camion:.2f}\nVenta: {total_vendido:.2f}\nBalance:{balance:.2f}')


#%% Impresion de la tabla de Frutas, cajones, precio compra y diferencia compra-venta

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print(f'{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10}')
print('---------- ---------- ---------- ----------')

informe = hacer_informe(camion, precios)
for nombre, cajones, precio, cambio in informe:
        precio = '$' + str(precio) #agrego el simbolo $
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
