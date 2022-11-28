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





