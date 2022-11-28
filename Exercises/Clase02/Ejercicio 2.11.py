import csv

f = open('Data/camion.csv')
filas = csv.reader(f)

encabezado = next(filas)
fila = next(filas)

t = (fila[0], int(fila[1]), float(fila[2]))