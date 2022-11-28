import csv

#%% Ejercicio 6.8
'''
    Misma función que la 6.7 pero en este caso vamos a poder
    convertir el tipo de los datos recuperados antes de devolverlos.
'''
   

def parse_csv(nombre_archivo, select = None, types = None):
    '''
    Parsea un archivo CSV en una lista de registros que son diccionarios.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        # buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
            # Si hay tipos definos,
            # Aplica los typos a las distintas columnas
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]

            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)

    return registros