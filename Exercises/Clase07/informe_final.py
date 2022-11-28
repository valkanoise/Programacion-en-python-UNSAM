import csv
import fileparse



#%% Acá importo fileparse.parse_csv y le pongo el tipo de elementos


def leer_camion(nombre_archivo):
    # 7.7 hay que abrir los archivos ya que se sacó del fileparse, por ende agrego with open
    with open(nombre_archivo, 'rt') as file:
        return fileparse.parse_csv(file, types=[str, int, float])
    
#%% 
''' Acá importo fileparse.parse_csv y le pongo el tipo de elementos y que no 
hay encabezados. ADICIONALMENTE convierto la lista a un diccionario para que
la funcion informe la pueda usar
'''


def leer_precios(nombre_archivo):
    # 7.7 hay que abrir los archivos ya que se sacó del fileparse, por ende agrego with open
    with open(nombre_archivo, 'rt') as file:
        return dict(fileparse.parse_csv(file, types=[str,float], has_headers=False ))

    
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


#%% Prueba para ejecutar desde IDE

# if __name__ == '__main__':
#     informe_camion('../Data/camion2.csv', '../Data/precios.csv')
    
    # # o podes seleccionar varios archivos e iterar la funcion informe_camion
    # # así lográs imprimir varios informes en simultáneo
    # files = ['../Data/camion.csv', '../Data/camion2.csv']
    # for name in files:
    #     print(f'{name:-^43s}')
    #     informe_camion(name, '../Data/precios.csv')
    #     print()
            
#%% Ejercicio 7.4 preparo el script para ejecutarse por línea de comando

''' 
Defino una función que recibe una lista con 3 elementos.
# La lista es sys.argv y sus 3 elementos. lista[0] = el nombre del script. 
lista[1] = ubicación y nombre de los datos del camion
lista[2] = ubicación y nombre de la lista de precios
'''

def f_principal(lista_argv):
    '''
    Función que recibe una lista de elementos provista por
    sys.argv y ejecuta el informe de compra-venta.
    Lista_argv debe contener 3 elementos, nombre del archivo.py, nombre
    del archivo del camion y nombre del archivo de precios
    '''
    
    # Agrego un error para que siempre ingresen LOS 3 PARAMETROS NECESARIOS para que todo funcione
    if len(lista_argv) != 3:
        raise SystemExit('Error! Se requieren 3 parametros: \n 1.Nombre Script \n 2.Archivo_camion \n 3.Archivo_precios')
    
    
    informe_camion(lista_argv[1], lista_argv[2])

'''  Ahora declaro que si este script es el modulo principal, importe sys
y ejecute la función principal para que arme un informe con los datos enviados
mediante línea de comando
'''

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)

#%% Prueba para ejecutarlo en línea de comando!######
'''
python3 informe_final.py ../Data/camion.csv ../Data/precios.csv
 
o también
 
import informe_final 
informe_final.f_principal(['informe_final.py', '../Data/camion.csv', '../Data/precios.csv'])

'''