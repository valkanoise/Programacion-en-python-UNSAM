# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:02:33 2021

@author: FEFe
"""

import fileparse
import gzip

'''
Distintos métodos para usar la función fileparse.parse_csv(). 
Dado que recibe cualquier iterable:
    Si es un archivo csv con distintas lineas hay que abrirlo primero con open()
    Si es una lista puede ingresar directamente en la función parse_csv()
'''


# Prueba para abrir un archivo (comprimido)
with gzip.open('../Data/camion.csv.gz', 'rt') as file:
    camion1 = fileparse.parse_csv(file, types=[str,int,float])

# Prueba abriendo una archivo sin comprimir
with open('../Data/camion.csv', 'rt') as file:
    camion2 = fileparse.parse_csv(file, types=[str,int,float])


# Prueba usando una lista (iterable) con varios strings (cada uno es una linea iterable)
lines = ['nombre,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
camion3 = fileparse.parse_csv(lines, types=[str,int,float])

#### ERROR ####    
# OJO! Ahora no abre el archivo en la función parse_csv como hacia antes...
# Por ende hace cualquier cosa!!!!! HAY QUE ABRIR EL ARCHIVO antes de usar parse_csv
camion4 = fileparse.parse_csv('../Data/camion.csv', types=[str,int,float])