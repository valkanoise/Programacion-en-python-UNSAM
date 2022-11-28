''' Esta versión de ticker.py usa funciones generadoras para funcionar'''

from vigilante import vigilar
from lote import Lote
import informe_final
import csv
from formato_tabla import crear_formateador


def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))
        
def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def filtrar_datos(rows, nombres):
    for row in rows:
        if row['nombre'] in nombres:
            # genero lotes porque uso la funcion formato_tabla.imprimir_tabla()
            yield Lote(row['nombre'], row['volumen'], row['precio']) 
        

def ticker(camion_file, log_file, fmt):
    ####################
    # Este es el generador de datos (log_file) y se arma un dict por cada fila
    rows = parsear_datos(vigilar(log_file)) 
    
    ###################
    # Procesamiento de los datos
    # Se monitorea el camion_file (conjunto de lotes)
    camion = informe_final.leer_camion(camion_file) # mirar productos para filtrar
    # Acá se seleccionan los datos que están en camion_file
    rows = filtrar_datos(rows, camion) #filtro
    
    ###################
    # Se consumen los datos /seleccionan como se van a imprimir las filas seleccionadas
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
    

#%% Prueba ticker
if __name__ == '__main__':
    ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'txt')



