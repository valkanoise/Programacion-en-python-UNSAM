import csv
f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

print(row)

types = [str, int, float]

print(types)

print(types[1](row[1])) #aplico metodo int al string '100' sería int(row[1])

r = list(zip(types, row))
print(r)

#%% Crear una lista con los elementos transformados a str, int y float
converted = []
for func, val in zip(types, row):
          converted.append(func(val))

print(converted)


#%% otra forma de hacer lo de arriba sin for, usando comprensión de listas

converted2 = [func(val) for func,val in zip(types, row)]

print(converted2)



