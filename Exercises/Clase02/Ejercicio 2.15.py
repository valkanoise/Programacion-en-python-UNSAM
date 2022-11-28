import csv

def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        encabezado = next(f) #contiene el encabezado con el nombre de las columnas
        print(encabezado)
        for row in rows:    # itera sobre la fila 2 en adelante sin tener en cuenta los encabezados
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
    
    return camion
        
        
camion = leer_camion('camion.csv')
total = 0.0
# for s in camion: #itero sobre los tuples dentro de la lista
#     total += s[1] * s[2] #multiplico cajones * precio y se va sumando en cada ciclo
        
  # otra forma como son tuples los que se iteran se puede desempaquetar

for nombre, cajones, precio in camion:
    total += cajones * precio       
    