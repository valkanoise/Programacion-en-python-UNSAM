import csv

#%% 4.15

def leer_arboles(nombre_archivo):
    '''Crea una lista conteniendo información sobre todos los árboles del
    archivo. Cada árbol es un diccionario conteniendo la información de cada 
    árbol'''
    
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        #Uso comprension de listas para armar dict con encabezadp:values para cada arbol.
        #Cada fila de la iteracion es un arbol.
        lista_diccionarios = [dict(zip(encabezados,fila)) for fila in filas]
    return lista_diccionarios
    

#%% Prueba arboleda
if __name__ == '__main__':
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    arboleda = leer_arboles(nombre_archivo)

#%% 4.16 
'''Armo una lista que contenga la altura de todos los Jacarandá'''

H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']

#%% 4.17 
'''Armo una lista de tuplas  que contenga la altura y diametro de todos los 
Jacarandá'''

alt_diam=[(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']


#%% 4.18 Version mas legible


# def medidas_de_especies(especies,arboleda):
#     diccionario = {}
#     for especie in especies:
#         diccionario[especie] = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie]
#     return diccionario
    


#%% 4.18 Usando comprensión de diccionarios

def medidas_de_especies(especies,arboleda):
    diccionario = {especie : [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie] for especie in especies}
    return diccionario


#%%Prueba del ejercicio 4.18

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas= medidas_de_especies(especies, arboleda)

