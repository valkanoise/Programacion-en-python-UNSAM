import csv
import gzip

# Ej 7.6 cambio nombre_de_arhivo por iterable
def parse_csv(iterable, select = None, types = None, has_headers= True, silence_errors= False):
    '''
    Parsea un archivo CSV o una lista (ambos son elemento iterables) 
    en una lista de registros que son diccionarios.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando 
    el parámetro select, que debe ser una lista de nombres de las columnas a 
    considerar. 
    Si se seleccionan columnas, adicionalmente hay que usar has_headers=TRUE. 
    El parametro silence_errors permite mostrar/ocultar errores que informan
    si hay datos faltantes y su ubicación en los datos ingresados.
    '''
    # 7.6 Eliminé open(nombre_de_archivo) as f:
    # 7.6 El cvs.reader() puede tomar cualquier iterable linea a linea, sea un archivo csv o una lista
    filas = csv.reader(iterable)
    
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
    with gzip.open('../Data/camion.csv.gz', 'rt') as file:
        camion1 = parse_csv(file, types=[str,int,float])
    
    
    lines = ['nombre,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
    camion2 = parse_csv(lines, types=[str,int,float])