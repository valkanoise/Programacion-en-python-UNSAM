


f = open('Data/precios.csv', 'rt')
encabezado = next(f)

for linea in f:
    linea = linea.split(',')
    if linea[0] == 'Naranja':
        print('El precio de la naranja es: ', linea[1])


f.close()


