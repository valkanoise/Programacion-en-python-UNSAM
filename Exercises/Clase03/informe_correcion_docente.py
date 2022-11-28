#%%
import csv
import gzip

def leer_camion(nombre_archivo):
    '''
    Para un archivo camión devuelve una lista
    con diccionarios respetando los encabezados 
    como claves y valores por fila
    '''
    #Lista final de retorno
    camion = []

    # op tomará el valor adecuado si el archivo está comprimido
    op =  n if nombre_archivo.endswith('gz') else open

    with op(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        #Defino la primer lína de archivo como headers
        encabezado = next(filas)
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezado,fila))
            print(record)
            try:
                # armo dict cajon, y para cada Key(nombre, cajones,precio) le asigno valor del record
                cajon = {} 
                cajon['nombre'] = str(record['nombre'])
                cajon['cajones'] = int(record['cajones'])
                cajon['precio'] = float(record['precio'])
                camion.append(cajon)
            except ValueError:
                print(f'\nFila {n_fila}: no se puede interpretar: {fila}'
                      f' del archivo: {nombre_archivo}\n')
    return camion

#%%
def leer_precios(nombre_archivo):
    '''
    Parsea archivo csv y devuelve un diccionario
    ordenando por fila y valor 
    {f1_v1:f1_v2, f2_v1:f2_v2..., fn_v1:fn_v2}
    '''
    #Diccionario final.
    l_precios = {}

    # op tomará el valor adecuado si el archivo está comprimido
    op = gzip.open if nombre_archivo.endswith('gz') else open

    with op(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)

        for n_fila, fila in enumerate (filas, start = 1):
            try:
                #Tomo cada valor de fila
                nombre, precio = fila
                l_precios[nombre] = float(precio)
            except ValueError:
                print(f'\nFila {n_fila}: no se puede interpretar: {fila}'
                      f' del archivo: {nombre_archivo}\n') 
        
    return l_precios

#%%
def hacer_balance(archivo_costos, archivo_ventas):
    '''
    Toma dos archivos de un camión (costo y precios)
    Compara los imtems y calcula la utilidad
    Imprime una tabla con el balance por utilizada
    retorna un str con el balance final
    '''
    costos = leer_camion(archivo_costos)
    ventas = leer_precios(archivo_ventas)
    costo_tot = 0
    venta_tot = 0
    cap_no_vendido = 0
    
    #Imprime el encabezado del balance.
    print(f'\nNombre{" "*7}|{" "*2}N-Cajones{" "*2}|{" "*2}'
          f'$ Compra{" "*3}|{" "*3}$ Venta\n{"="*55}')
    
    #Cálculo de ganacia
    for costo in costos:
        costo_tot += costo['cajones'] * costo['precio']
        #Miro que el intem esté o no enventas
        if costo['nombre'] in ventas:
            venta_tot += ventas[costo['nombre']] * costo['cajones']
        else:
            cap_no_vendido += costo['cajones'] * costo['precio']
        #Imprime para cada item el balance de venta
        print(f"{costo['nombre']:10}{' '*3}|"   
              f"{costo['cajones']:10.2f}{' '*3}|"
              f"{costo['precio']:10.2f}{' '*3}|"
              f"{ventas[costo['nombre']]:10.2f}")
     
    ganancia = venta_tot - costo_tot

    if ganancia > 0:
        bal = f'Excelente, hubo ganancia y quedó sin vender ${cap_no_vendido:0.2f}'
    else:
        bal = f'Mala racha revisemos números, quedó sin vender ${cap_no_vendido:0.2f}'
    
    print(f'\nCosto total: ${costo_tot:0.2f}\n'
          f'Recaudado: ${venta_tot:0.2f}\n'
          f'\nSaldo: ${ganancia:0.2f}\n'
          f'Capital no vendido ${cap_no_vendido:0.2f}\n')

    return bal

#%% pruebas Descomentar las líneas para hacer pruebas

resumen_camion = hacer_balance('../Data/camion.csv','../Data/precios.csv')
#print(resumen_camion)

#Archivos con faltantes
#hacer_balance('../Data/camion.csv.gz', '../Data/precios.csv')
#hacer_balance('../Data/missing.csv', '../Data/precios.csv')
#hacer_balance('../Data/fecha_camion.csv', '../Data/precios.csv')
