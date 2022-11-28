
import csv
from pprint import pprint

#%% Ejercicio 3.18: Lectura de los árboles de un parque
'''
Definí una función leer_parque(nombre_archivo, parque) que abra 
el archivo indicado y devuelva una lista de diccionarios con la 
información de los arboles presentes dentro 
del parque especificado. La función devuelve, 
en una lista un diccionario por cada árbol dentro de parque elegido.
'''


def leer_parque(nombre_archivo, parque):
    lista_parque = []
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        
        for fila in filas:
            if fila[10] == parque:
                record = dict(zip(encabezados, fila))
                lista_parque.append(record)
          
    return lista_parque


#%% Probar funcion leer_parque

nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
parque_interes = 'GENERAL PAZ'
parque = leer_parque(nombre_archivo, parque_interes)


#%%Ejercicio 3.19: Determinar las especies en un parque
'''Escribí una función especies(lista_arboles) que tome una lista 
de árboles (cada arbol es un diccionario) como la generada en el ejercicio 
anterior y devuelva el conjunto de especies (la columna 'nombre_com' 
del archivo) que figuran en la lista. ugerencia: Usá el comando set 
como en la Sección 2.5.'''

def especies(lista_arboles):
    especies = set() # genero un set()
    for arbol in lista_arboles:
        especies.add(arbol['nombre_com']) #voy agregando elementos al set. Si estaba no pasa nada y si no estaba lo agrega. El set contiene elementos único.
    return especies
   
# otra versión usando set comprehension     
def especies1(lista_arboles):
    return {arbol['nombre_com'] for arbol in lista_arboles}


#%% Prueba funcion especies. Devuelve cantidad de especies en determinado parque
# En el Parque GENERAL PAZ hay 81 especies distintas

especies_parque = especies(parque) 
especies = {arbol['nombre_com'] for arbol in parque}

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

#%%
