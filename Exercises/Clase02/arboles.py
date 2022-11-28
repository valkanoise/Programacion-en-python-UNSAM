#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rgrimson
"""

#%% Abrir archivos

f = open('Data/arboles.csv', 'rt') # es un puntero hacia el archivo, pero no lo lee. Sólo se indica el archivo con el cual se trabajará
data = f.read() #ahora si python lee el contenido del archivo y lo guarda dentro de una variable
print(data)

#%% ES IMPORTANTE CERRAR LOS ARCHIVOS
f.close() #se cierra el archivo, se vacía el buffer y se guarda la información

#%% con el comando WITH uno abre los archivos y no debe preocuparse por cerrarlos
### cuando iteras con ENUMERATE() tenés dos elementos: i= index y linea.
### cuando imprimís sale el index y al lado la línea

nombre_archivo = 'Data/arboles.csv'
with open(nombre_archivo, 'rt') as archivo:
    for i, linea in enumerate(archivo):
        print(i, linea)

#%%

f = open('Data/arboles.csv', 'rt')
# o si hace falta aclararlo en tu SO les podés aclarar el tipo de encoding del archivo usado UTF-8
f = open('Data/arboles.csv', 'rt', encoding='utf8') 
encabezados = next(f).split(',') # funcion que se mueve fila a fila a lo largo del archivo... empieza por la primera fila (encabezados)
print(encabezados)

#%%

for line in f:
    fila = line.split(',')
    print(fila)

#%%

encabezados #la primer fila se guardo como encabezados antes en la linea 30
fila # es la ultima linea impresa en la iteracion realizada en la linea 35

#%% zip

l=[]
f = open('Data/arboles.csv', 'rt')
encabezados = next(f).split(',')
for line in f:
    fila = line.split(',')
    print(fila)
    registro = dict(zip(encabezados, fila))
    l.append(registro)



#%%

f = open('Data/arboles.csv', 'rt', encoding='utf8') 
encabezados = next(f).split(',')
for line in f:
    fila = line.split(',')
    for e,d in zip(encabezados,fila):
        el = e.strip("\n")
        dl = d.strip("\n")
        print(f'{el:>12s}: {dl}')
    print()



#%%

f = open('Data/arboles.csv', 'rt', encoding='utf8') 
encabezados = next(f).strip("\n").split(',')
arboles = []
for line in f:
    fila = line.strip("\n").split(',')
    arbol = {}
    for e,d in zip(encabezados,fila):
        arbol[e]=d
    arboles.append(arbol)