#%% Primero abro el archivo con with, luego se lee ENTERO y se lo imprime entero

with open('camion.csv', 'rt') as f:
    data = f.read()
    print(data)
    
#%% A veces no conviene leer todo el archivo si es muy grande

with open('camion.csv', 'rt') as f:
    for line in f:
        # print(line) #imprime dejando un enter entre lineas \n para evitar eso
        print(line, end= '') # le decis que imprima dejando nada al final de cada linea
        
#%% Si querés separar el encabezado del resto

with open('camion.csv', 'rt') as f:
    encabezado = next(f)
    print(encabezado, end= '') #imprime primera linea
    for line in f:
        print(line, end='') #imprime todas las lineas a partir de la segunda porque la primera ya se saleto con next()
