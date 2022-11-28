import csv


#%% Ejercicio 6.6

def parse_csv(nombre_archivo):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        
        # Lee los encabezados del archivo
        headers = next(rows)
        
        #Ahora iteramos sobre las filas del archivo
        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            registro = dict(zip(headers, row))
            registros.append(registro)

    return registros