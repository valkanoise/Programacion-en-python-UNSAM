import random
import numpy as np


#%% Ejercicio 5.10: Crear
def crear_album(figus_total):
    album= np.zeros(figus_total, dtype = int)
    return album

#%% Ejercicio 5.11: Incompleto
def album_incompleto(A):
    return (0 in A)

#%% Ejercicio 5.12: Comprar
def comprar_figu(figus_total):
    return random.randint(0, figus_total - 1)

#%% Ejercicio 5.13: Cantidad de compras
def cuantas_figus(figus_total):
    
    album = crear_album(figus_total)
    compras_totales = 1
    
    while album_incompleto(album):
        figu = comprar_figu(figus_total)
        album[figu] += 1
        compras_totales += 1
    
    return compras_totales

#%% Ejercicio 5.14
'''Función que calcula N veces la cantidad de figus necesarias para llenar
el album, arma una lista y calcula el promedio de comprar necesarias para llenar
el album. Por default repeticiones = 1000'''

def n_repeticiones(repeticiones=1000):
    cantidad_compras = [cuantas_figus(6) for i in range(repeticiones)]
    promedio_cantidad_compras = np.mean(cantidad_compras)
    return promedio_cantidad_compras

#Para n_repeticiones(1000000) dió 15.701019

#%% Ejercicio 5.15
'''función llamada experimento_figus(n_repeticiones, figus_total) que simula 
el llenado de n_repeticiones álbums de figus_total figuritas y devuelva el 
número estimado de figuritas que hay que comprar, en promedio, para completar 
el álbum.'''

def experimento_figus(n_repeticiones, figus_total):
    cantidad_compras = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
    promedio_cantidad_compras = np.mean(cantidad_compras)
    return promedio_cantidad_compras
    
# ¿Cuánto te da para 100 repeticiones en un álbum de 670 figuritas?
# Me dió 4862.07 compras (cada compra es una figu!)












