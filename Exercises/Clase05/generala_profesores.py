# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 15:32:08 2021

@author: iri_0
"""
#Escribí una función tirar() que devuelva una lista con cinco dados generados aleatoriamente. Escribí otra función llamada es_generala(tirada) que devuelve True si y sólo si los cinco dados de la lista tirada son iguales.

import random

def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6)) 
    return tirada
    
tirada= tirar()

def es_generala(tirada):
    resultado= all(numero==tirada[0] for numero in tirada)
    print(resultado)

es_generala(tirada)

N= 100000
salio_generala_servida= [(es_generala(tirada)) for i in range (N)]
G = sum([es_generala(tirada) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

#Ejercicio 5.2: Generala no necesariamente servida

import random
import numpy as np
from collections import Counter


def completar_tirada(seleccion):
    '''recibe los datos que se guardaron en una tirada anterior y completa tirando los que falta hasta 5'''
    tirada=seleccion
    while len(tirada) < 5: 
        tirada.append(np.random.randint(1,7)) 
    return tirada



def seleccionar_mejores (tirada):
    '''selecciona los dados que más se repiten'''
    T=Counter(tirada)
    d= T.most_common(1)[0][0] #me de el dado que más se repite
    n= T.most_common(1)[0][1] #cuantas veces se repite
    
    seleccion= [d]*n #selecciono estos dados para la proxima mano
    return seleccion
    
# completar_tirada([3,3,3])

N=100000  #vamos a jugar N veces
generalas=0

for j in range (N):
    if j%10000==0:
        print(j)
    seleccion=[]
    for k in range(3):
        tirada= completar_tirada(seleccion)
        seleccion= seleccionar_mejores(tirada)
    if len(seleccion)==5: #opcion2= len(set(seleccion)==1)
        generalas+=1

print(f'la probabilidad de hacer generala es de: {generalas/N}')

#%% Opcion 2: Generala 

import random

def tirar(n):
    tirada=[]
    for i in range(n):
        tirada.append(random.randint(1,6)) 
    return tirada

def es_generala(tirada):
    return len(set(tirada))==1

def repetidos(tirada):
    lista=[]
    for i in range(1,7):
        lista.append(tirada.count(i))
    for j, e in enumerate (lista):
        if e==max(lista):
            res= [j+1]*e
    return res      
    
def mejorar_tirada(tirada):
    rep= repetidos(tirada)
    l= tirar(5-len(rep))
    t= rep + l
    return t

def jugar_generala():
    t= tirar(5)
    t= mejorar_tirada(t)
    t= mejorar_tirada(t)
    return es_generala(t)
  
N= 100000
G= sum([jugar_generala() for i in range(N)])
prob=G/N
print(f'Tiré {N} veces de las cuales {G} saqué generala')
print(f' la probabilidad de hacer generada es de {prob}')






