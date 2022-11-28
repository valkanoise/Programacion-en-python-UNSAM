import csv
import os
import matplotlib.pyplot as plt
import numpy as np



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

# H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']

#%% 4.17 
'''Armo una lista de tuplas  que contenga la altura y diametro de todos los 
Jacarandá'''

alt_diam = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']


#%% 4.18 Version mas legible


def medidas_de_especies(especies,arboleda):
    diccionario = {}
    for especie in especies:
        diccionario[especie] = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie]
    return diccionario
    


#%% 4.18 Usando comprensión de diccionarios

def medidas_de_especies(especies,arboleda):
    diccionario = {especie : [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie] for especie in especies}
    return diccionario


#%% Prueba del ejercicio 4.18

# if __name__ == '__main__':
    
#     especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
#     medidas= medidas_de_especies(especies, arboleda)
    
#%% Ejercicio 5.25

'''Se usa el módulo os.path para definir la ubicación del archivo a leer.
os.path.join(path, *paths) Join one or more path components intelligently.'''

nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')

# Lista de diccionarios. Cada dic contiene la información de un árbol
arboleda = leer_arboles(nombre_archivo)

# Lista que contiene la altura de todos los Jacarandás incluidos en arboleda
altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']

# Se grafica un histrograma de las alturas (altos) de los Jacarandás
plt.hist(altos,bins=100)
plt.title("Histograma de alturas de los Jacarandás")
plt.xlabel("Alto (m)")
plt.ylabel("Nro. de Jacarandás")

#para borrar un gráfico y no se superponga con el próximo
# plt.clf()


#%% Ejercicio 5.26 trabajando con listas. Versión que hice para probar

#Lista creada en el 4.17
alt_diam = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']

def scatter_hd_listas(lista_de_pares):
    '''Función que a partir de una lista de tuplas (alto, diámetro), crea
    dos listas, una [diámetros] y otra de[alturas]. Con esas listas genera
    un scatter plot con x= diametros e y= alturas'''
    
    alturas = [tupla[0] for tupla in alt_diam]
    diamteros = [tupla[1] for tupla in alt_diam]
    
    plt.scatter(diametros,alturas)
    plt.title("Diámetros vs. Alturas de los Jacarandás")
    plt.xlabel("Diámetros")
    plt.ylabel("Alturas")
    plt.show()


#%% Ejercicio 5.26 trabajando con arrays

def scatter_hd(lista_de_pares):
    '''Función que a partir de una lista de tuplas (alto, diámetro), crea
    dos listas, una [diámetros] y otra de[alturas]. Con esas listas genera
    un scatter plot con x= diametros e y= alturas'''
    
    vector_altura_diametro = np.array(alt_diam)
    alturas = vector_altura_diametro[:,0]
    diametros = vector_altura_diametro[:,1]
    #Genero un array con 3255 colores al azar
    colores = np.random.rand(len(lista_de_pares))
    
    # alpha define nivel de transparencia de los puntos, c= se agrega un dato de color para cada punto
    plt.figure() #define una nueva imagen para que no se superpongan figuras
    plt.scatter(diametros,alturas,alpha=0.15, c=colores)
    plt.xlabel("diámetro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()
    
#%% Prueba 5.26
scatter_hd(alt_diam)


