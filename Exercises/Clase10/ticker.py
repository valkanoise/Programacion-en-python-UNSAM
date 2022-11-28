''' Esta función de ticker usar expresiones generadoras en vez de funciones
generadoras'''

from vigilante import vigilar
from lote import Lote
import informe_final
import csv
from formato_tabla import crear_formateador



def ticker(camion_file, log_file, fmt):
    ### Abre log_file ###
    rows = csv.reader(vigilar(log_file)) 
    
    ### Procesamiento ###
    # Elije columnas
    index = [0,1,2]
    rows = ([row[index] for index in index] for row in rows)
    # Cambia el tipo
    types = [str, float, int]
    rows = ([func(val) for func, val in zip(types, row)] for row in rows)
    # Hace dicts
    headers = ['nombre', 'precio', 'volumen']
    rows = (dict(zip(headers, row)) for row in rows)
    # Selecciona filas con frutas presentes en el camion_file y las convierte a tipo lote
    camion = informe_final.leer_camion(camion_file) # selecciono el camion con sus productos
    rows = (Lote(row['nombre'], row['volumen'], row['precio']) for row in rows if row['nombre'] in camion) # chequea si los productos generados en el log están en el camions
    
    ### Impresión de los datos ###
    # Selecciona tipo de salida (txt, csv o html)
    formateador = crear_formateador(fmt)
    # Imprime encabezados
    formateador.encabezado(['Nombre', 'Precio', 'Volumen']) #defino el nombre de las columnas
    
    # Imprime las filas
    for c in rows:
        rowdata = []
        for col in ['nombre','precio','cajones']:
            if hasattr(c, col): 
                col = getattr(c, col) # si tiene el atributo columna lo buscamos y lo asignamos a col
                rowdata.append(str(col))
        formateador.fila(rowdata)

#%% Prueba

ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'txt')


