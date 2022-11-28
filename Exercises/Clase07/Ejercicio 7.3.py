import csv


def parse_csv(nombre_archivo, select = None, types = None, has_headers= True, silence_errors= False):
    '''
    Parsea un archivo CSV en una lista de registros que son diccionarios.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        
        #### SI HAY ENCABEZADOS DEFINE VARIABLE ENCABEZADOS####
        if has_headers:
            
        # Lee los encabezados del archivo
            encabezados = next(filas)

            # Si se indicó un selector de columnas,
            # buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
    
        if select:
            # Ejercicio 7.1
            # si alguien seleccionó columnas pero puso has_headers = False la variable encabezados no existe, por ende hay que atrapar error
            try:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                encabezados = select
            except NameError:
                # Frente al error NameError lanzo una exception tipo RuntimeError
                raise RuntimeError("Para seleccionar, necesito encabezados.")
        else:
            indices = []

        registros = []
        for nfila, fila in enumerate(filas):
            
            # Si hay alguna fila vacía la saltea y no da error
            if not fila:
                continue
            
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
           
            # Si hay tipos definos,
            # Aplica los typos a las distintas columnas
            
            if types:
                # Ejercicio 7.2
                try:
                    fila = [func(val) for func, val in zip(types, fila) ]
                except ValueError as e:
                    # Ejercicio 7.3 agrego opción de imprimir o no los errores
                    if not silence_errors:
                        print(f'Fila {nfila+1}: no pude convertir {fila}')
                        print(f'Fila {nfila+1}: Motivo:', e)
                    continue # con continue esta fila no se utiliza (con pass se usaría pero quedarían datos vacios)
            
            #### SI HAY ENCABEZADOS ####
            ### Si hay encabezados arma un diccionario usando como Keys a la variable encabezado
            if has_headers:
                registro = dict(zip(encabezados, fila))
            ### Si no hay encabezados arma una tupla
            else:
                registro = tuple(fila)

            # Armar el diccionario
            
            registros.append(registro)

            
    return registros


#%% Pruebas
if __name__ == '__main__':
    # 7.1 Levanta error RuntimeError e indica que necesita encabezados
    # parse_csv('../Data/precios.csv', select = ['nombre','precio'], has_headers = False)
    
    # 7.2 Atrapa los errores e imprime donde están
    camion = parse_csv('../Data/missing.csv', types = [str, int, float])
    
    # 7.3 Atrapa los errores y me da la opción de imprimor o no donde están los errores con parametro silence_errors= True/False
    camion2 = parse_csv('../Data/missing.csv', types = [str,int,float], silence_errors = True)
