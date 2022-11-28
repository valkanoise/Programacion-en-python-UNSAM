import csv
import fileparse



#%% Acá importo fileparse.parse_csv y le pongo el tipo de elementos


def leer_camion(nombre_archivo):
    return fileparse.parse_csv(nombre_archivo, types=[str, int, float])
    
#%% 
''' Acá importo fileparse.parse_csv y le pongo el tipo de elementos y que no 
hay encabezados. ADICIONALMENTE convierto la lista a un diccionario para que
la funcion informe la pueda usar
'''


def leer_precios(nombre_archivo):
    return dict(fileparse.parse_csv(nombre_archivo, types=[str,float], has_headers=False ))

    
#%%
def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio']
        t = (lote['nombre'], lote['cajones'], precio_venta, cambio)
        lista.append(t)
    return lista

#%% Ejercicio 6.4

def imprimir_informe(informe):
    
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
 
#%% Ejercicio 6.5. Esta función recopila/utiliza todas las funciones anteriores
      
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)


#%% Prueba

if __name__ == '__main__':
    informe_camion('../Data/camion2.csv', '../Data/precios.csv')
    
    # # o podes seleccionar varios archivos e iterar la funcion informe_camion
    # # así lográs imprimir varios informes en simultáneo
    # files = ['../Data/camion.csv', '../Data/camion2.csv']
    # for name in files:
    #     print(f'{name:-^43s}')
    #     informe_camion(name, '../Data/precios.csv')
    #     print()
            
        