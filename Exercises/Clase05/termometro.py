import random
import numpy as np


def medir_temp(n=1):
    '''Función que devuelve n cantidad de temperaturas al azar con una
    distribución normal con media (mu) 37.5 y desvío estándar (sigma) 0.2.
    A los valores generados se los redondea con un decimal y se los almacena
    en una lista que es devuelta por la función'''
    
    #Creo lista con valores aleatorios de dist. normal    
    mediciones = [round(random.normalvariate(37.5,0.2),1) for i in range(n)]

    # La lista creada previamente la uso para genera un vector de n valores
    mediciones_vector = np.array(mediciones)
    
    # Almaceno el vector en un archivo .npy
    np.save('../Data/temperatura.npy', mediciones_vector)

    return mediciones

def resumen_temp(n=1):
    
    mediciones = medir_temp(n)
    maximo = max(mediciones)
    minimo = min(mediciones)
    promedio = sum(mediciones)/n
    
    #Calculo de la mediana
    half = len(mediciones) // 2
    mediciones.sort()
    
    # Si la lista es par promedio los dos elementos del medio de la lista ordenada
    if not len(mediciones) % 2:
        mediana = (mediciones[half - 1] + mediciones[half]) / 2.0
    #si la lista es impar utilizo el valor del medio de la lista ordenada
    else:
        mediana = mediciones[half]
    
    
    tupla = (round(maximo,1), round(minimo,1), round(promedio,1), round(mediana,1))
    return tupla
        
        
    