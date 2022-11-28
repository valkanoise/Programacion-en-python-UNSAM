# informe.py

import fileparse
import lote
import formato_tabla

#%%
def leer_camion(nom_archivo):
    '''
    Lee un archivo y lo devuelve como lista de lotes con los atributos:
    lote.nombre, lote.cajones y lote.precio
    '''
    with open(nom_archivo) as lines:
        camion_dicts = fileparse.parse_csv(lines, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
        camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
        return camion        
        
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
def imprimir_informe_original(data_informe):
    '''
    Imprime adecuadamente una tabla de una lista de tuplas
    (nombre, cajones, precio, cambio).
    '''
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s' % headers)
    print(('-'*10 + ' ')*len(headers))
    for fila in data_informe:
        print('%10s %10d %10.2f %10.2f' % fila)
        
#%%
def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)
        
    
#%%
def informe_camion(archivo_camion, archivo_precios):
    '''
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = dict(leer_precios(archivo_precios))

    # Crear los datos para el informe
    data_informe = hacer_informe(camion, precios)

    # Imprimir el informe
    formateador = formato_tabla.FormatoTabla()
    imprimir_informe(data_informe, formateador)


#%%
def main(args):
    if len(args) != 3:
        raise SystemExit('Uso: %s archivo_camion archivo_precios' % args[0])
    informe_camion(args[1], args[2])
#%%
if __name__ == '__main__':
    import sys
    main(sys.argv)
