import csv

def leer_precios(nombre_archivo):
    diccionario = {}

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        encabezado = next(f) #contiene el encabezado con el nombre de las columnas
        
        for row in rows:    # itera sobre la fila 2 en adelante sin tener en cuenta los encabezados
            try:
                diccionario[row[0]] = row[1]
            except IndexError:
                print ('- WARTNING - Hay elementos incompletos')

    return diccionario

precios = leer_precios('precios.csv')
print(precios)