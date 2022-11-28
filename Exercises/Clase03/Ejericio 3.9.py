'''Se modifica el script para que tome datos con columnas en distinto orden.
Para ello el script usará ZIP para crear dict y poder trabajar con KEY 
y no por su posición en el archivo csv.'''

import csv

def costo_camion(nombre_archivo):
   
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f) 
        encabezados = next(filas)
        costo_total = 0
        
        for n_fila, fila in enumerate(filas, start=1):
        #itera en cada fila y arma cada vez un nuevo un dict para cada fila
        #los KEYS del dict se usan mas abajo para calcular el costo_total buscando por KEYs cajones y precios
            record = dict(zip(encabezados, fila))
            print(record)
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costo_total += ncajones * precio
            # Esto atrapa errores/falta datos en los int() y float() de arriba.
            except ValueError:
                continue
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return costo_total
 
#%%
costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)


#%% Prueba con otro archivo que tiene distinto nro de columnas

costo = costo_camion('../Data/fecha_camion.csv')
print('\n\nCosto total:', costo)