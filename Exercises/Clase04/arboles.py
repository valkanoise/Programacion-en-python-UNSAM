
import csv
from pprint import pprint

#%% Ejercicio 3.18: Lectura de los árboles de un parque
'''Definí una función leer_parque(nombre_archivo, parque) que abra 
el archivo indicado y devuelva una lista de diccionarios con la 
información del parque especificado. La función debe devolver, 
en una lista un diccionario con todos los datos por cada árbol 
del parque elegido (recordá que cada fila del csv es un árbol).'''



def leer_parque(nombre_archivo, parque):
    lista_parque = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        fila1 = next(filas)
        for fila in filas:
            if fila[10] == parque:
                record = dict(zip(encabezados, fila))
                lista_parque.append(record)
          
    return lista_parque


#%% Probar funcion leer_parque

nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
parque_interes = 'CENTENARIO'
parque = leer_parque(nombre_archivo, parque_interes)


#%%Ejercicio 3.19: Determinar las especies en un parque
'''Escribí una función especies(lista_arboles) que tome una lista 
de árboles (cada arbol es un diccionario) como la generada en el ejercicio 
anterior y devuelva el conjunto de especies (la columna 'nombre_com' 
del archivo) que figuran en la lista. ugerencia: Usá el comando set 
como en la Sección 2.5.'''

def especies(lista_arboles):
    especies = set()
    for arbol in lista_arboles:
        especies.add(arbol['nombre_com'])
    return especies
        
#%% Prueba funcion especies. Devuelve cantidad de especies en determinado parque
# En el Parque GENERAL PAZ hay 81 especies distintas

especies_parque = especies(parque) 

#%% Ejercicio 3.20: Contar ejemplares por especie
'''Usando contadores como en el Ejercicio 3.11, escribí una función 
contar_ejemplares(lista_arboles) que, dada una lista como la que generada 
con leer_parque(), devuelva un diccionario en el que las especies 
(recordá, es la columna 'nombre_com' del archivo) sean las claves y tengan 
como valores asociados la cantidad de ejemplares en esa especie en la lista 
dada.'''

from collections import Counter

def contar_ejemplares(lista_arboles):
    contador = Counter()
    for arbol in lista_arboles:
        contador[arbol['nombre_com']] += 1
    return contador

#%% Prueba funcion contar ejemplares por especie en determinado parque

cantidad = contar_ejemplares(parque)
pprint(cantidad.most_common(5))

#%%3.21

#%%3.22

#%%3.24


#============================================================================#
#%% Clase 4
#============================================================================#

import csv

#%% 4.15

def leer_arboles(nombre_archivo):
    '''Crea una lista de diccionarios con información sobre todos los árboles del
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


#%% Prueba del ejercicio 4.18
if __name__ == '__main__':
    
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas= medidas_de_especies(especies, arboleda)
    

