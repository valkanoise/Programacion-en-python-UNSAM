import csv

def costo_camion(nombre_archivo):
   
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f) 
        encabezado = next(filas)
        costo_total_frutas = 0
        
        for n_fila,fila in enumerate(filas, start=1):
            try: 
                costo_fruta = int(fila[1])*float(fila[2])
                costo_total_frutas = costo_total_frutas + costo_fruta 
            except ValueError: 
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return costo_total_frutas
            
costo = costo_camion('../Data/missing.csv')
print('\n\nCosto total:', costo)

