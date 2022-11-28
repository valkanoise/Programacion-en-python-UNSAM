import csv

f = open('../Data/fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)


# definimos una lista con las columnas de interes
select = ['nombre', 'cajones', 'precio']

#Ubiquemos los índices de esas columnas de interes en el header del CSV:
indices = [headers.index(ncolumna) for ncolumna in select]

#avanzamos una fila
row = next(rows)

record = {ncolumna: row[index] for ncolumna, index in zip(select, indices)}  

camion = [{ ncolumna: row[index] for ncolumna, index in zip(select, indices)} for row in rows]