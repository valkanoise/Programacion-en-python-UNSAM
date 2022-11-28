# informe.py

import fileparse
from lote import Lote
import formato_tabla
from camion import Camion

#%%
def leer_camion(filename):
    '''
    Lee un archivo con el contenido de un camión
    y lo devuelve como un objeto Camion.
    '''
    with open(filename) as file:
        camiondicts = fileparse.parse_csv(file,
                                        select = ['nombre', 'cajones', 'precio'],
                                        types = [str, int, float])

    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts]
    return Camion(camion)
        
def leer_precios(nom_archivo):
    '''
    Lee un archivo CSV con data de precios 
    y lo devuelve como un diccionario
    con claves nombres y con sus precios como valores
    '''
    with open(nom_archivo) as lines:
        return dict(fileparse.parse_csv(lines, types = [str,float], has_headers = False))
#%%
def hacer_informe(camion, precios):
    '''
    Crea una lista de tuplas (nombre, cajones, precio, cambio) 
    dada una lista de lotes en un camión y un diccionario de precios nuevos.
    '''
    filas = []
    for c in camion:
        precio_orig = c.precio
        cambio = precios[c.nombre] - precio_orig
        reg = (c.nombre, c.cajones, precio_orig, cambio)
        filas.append(reg)
    return filas
        
#%%
def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        precio = f'${precio:0.2f}' #le agrego el simbolo pesos
        rowdata = [nombre, str(cajones), precio, f'{cambio:0.2f}']
        formateador.fila(rowdata)
        
    
#%%
def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es txt
    Alternativas: csv o html
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = dict(leer_precios(archivo_precios))

    # Crear los datos para el informe
    data_informe = hacer_informe(camion, precios)

    # Imprimir el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)


#%%
def main(args):
    if len(args) < 3:
        raise SystemExit('Uso: %s archivo_camion archivo_precios formato(opt)' % args[0])
    
    # si pasamos 3 parametros, imprime usando el formato por default de 'txt'
    if len(args) == 3:
        informe_camion(args[1], args[2])
    
    # si pasamos 4 parametros, el 4to indica el formato = fmt
    if len(args) == 4:
        informe_camion(args[1], args[2], args[3])

    
#%%
if __name__ == '__main__':
    import sys
    main(sys.argv)
    