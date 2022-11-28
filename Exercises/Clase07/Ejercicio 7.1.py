import csv


def parse_csv(nombre_archivo, select = None, types = None, has_headers= True):
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
        for fila in filas:
            
            # Si hay alguna fila vacía la saltea y no da error
            if not fila:
                continue
            
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
           
            # Si hay tipos definos,
            # Aplica los typos a las distintas columnas
            
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]
            
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
# if __name__ == '__main__':
# #     # Pruebo que arme un diccionario y le ponga los typos a cada elemento    
#     camion = parse_csv('../Data/camion.csv', types=[str, int, float])
# #     print(camion == [{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}, {'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1}, {'nombre': 'Caqui', 'cajones': 150, 'precio': 103.44}, {'nombre': 'Mandarina', 'cajones': 200, 'precio': 51.23}, {'nombre': 'Durazno', 'cajones': 95, 'precio': 40.37}, {'nombre': 'Mandarina', 'cajones': 50, 'precio': 65.1}, {'nombre': 'Naranja', 'cajones': 100, 'precio': 70.44}])
    
# #     # Pruebo seleccionar algunos elementos del camion y que les ponga sus tipos
#     cajones_lote = parse_csv('../Data/camion.csv', select=['nombre', 'cajones'], types=[str, int])
# #     print(cajones_lote == [{'nombre': 'Lima', 'cajones': 100}, {'nombre': 'Naranja', 'cajones': 50}, {'nombre': 'Caqui', 'cajones': 150}, {'nombre': 'Mandarina', 'cajones': 200}, {'nombre': 'Durazno', 'cajones': 95}, {'nombre': 'Mandarina', 'cajones': 50}, {'nombre': 'Naranja', 'cajones': 100}])
    
# #     # Pruebo que si no hay encabezados arme una tupla con sus tipos de datos
# #     # Son iguales pero da False porque hay errores con los acentos
#     precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)
# #     print(precios == [('Lima',40.22), ('Uva',24.85), ('Ciruela',44.85), ('Cereza',11.27), ('Frutilla',53.72), ('Caqui',105.46), ('Tomate',66.67), ('Berenjena',28.47), ('Lechuga',24.22), ('Durazno',73.48), ('Remolacha',20.75), ('Habas',23.16), ('Frambuesa',34.35), ('Naranja',106.28), ('Bruselas',15.72), ('Batata',55.16), ('Rúcula',36.9), ('Radicheta',26.11), ('Repollo',49.16), ('Cebolla',58.99), ('Cebollín',57.1), ('Puerro',27.58), ('Mandarina',80.89), ('Ajo',15.19), ('Rabanito',51.94), ('Zapallo',24.79), ('Espinaca',52.61), ('Acelga',29.26), ('Zanahoria',49.74), ('Papa',69.35)])

# # # Si a cualquiera de las funciones de arriba saco el TYPE de la función funciona igual pero todos sus elementos como strings