import csv

f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

# agrego una funcion para el BONUS
def tupla_fecha(fecha):
    '''función que convierte una fecha en string como tupla de 3 elementos,
    (día, mes, año). Cada elemento es un int'''
    tupla = tuple ([int(i) for i in fecha.split('/')])
    # b= a.split('/')
    # tupla_fecha = (int(b[0]), int(b[1]), int(b[2]))
    return tupla  


# print(headers)
# print(row)

#%% Defino tipos en una lista y agrego fecha para el BONUS
types = [str, float, tupla_fecha, str, float, float, float, float, int]
# con =list(zip(types, row))

#%% Convierto y creo lista con los elementos de row usando las funciones de la 
# lista types
converted = [func(val) for func, val in zip(types, row)]

#%% Armo diccionario con los header y los elementos convertidos en sus tipos

record = dict(zip(headers, converted))
print(record)
# print(record['name'])
# print(record['price'])
