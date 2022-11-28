import os
import csv
import matplotlib.pyplot as plt
import numpy as np


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


def medidas_de_especies(especies,arboleda):
    diccionario = {especie : [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie] for especie in especies}
    return diccionario

def scatter_hd(diccionario, especie):
    '''Función que a partir de una lista de tuplas (alto, diámetro), crea
    dos listas, una [diámetros] y otra de[alturas]. Con esas listas genera
    un scatter plot con x= diametros e y= alturas'''
    
    lista_de_pares = diccionario[especie]
    vector_altura_diametro = np.array(lista_de_pares)
    alturas = vector_altura_diametro[:,0]
    diametros = vector_altura_diametro[:,1]
    #Genero un array con 3255 colores al azar
    # colores = np.random.rand(len(lista_de_pares))
    
    # alpha define nivel de transparencia de los puntos, c= se agrega un dato de color para cada punto
    # plt.figure() #define una nueva imagen para que no se superpongan figuras
    plt.scatter(diametros,alturas,alpha=0.15)
    plt.xlabel("diámetro (cm)")
    plt.ylabel("alto (m)")
    plt.title(f"Relación diámetro-alto para {especie}")
    plt.xlim(0,320) 
    plt.ylim(0,60) 
    plt.show()
    

nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)


for especie in especies:
    scatter_hd(medidas, especie)



