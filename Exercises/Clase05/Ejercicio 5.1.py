# import random

# def tirar():
#     '''función que devuelve una lista con cinco dados generados 
#     aleatoriamente.'''
#     tirada=[]
#     for i in range(5):
#         tirada.append(random.randint(1,6)) 
#     return tirada

#%% Otra formar de tirar() con comprensión de listas

import random

def tirar():
    tirada = [random.randint(1, 6) for i in range(5)]
    return tirada

#%% Definir si la tirada es generala

def es_generala(tirada):
    '''función que devuelve True si y sólo si los cinco dados de la lista 
    tirada son iguales.'''
    if tirada[0]==tirada[1]==tirada[2]==tirada[3]==tirada[4]:
        return True
    else:
        return False
    
#%% Otra forma de definir si es generala es si el nro más repetido y el menos repetido son iguales

def es_generala(tirada):
    if max(tirada) == min(tirada) and len(tirada) == 5:
        return True
    else:
        return False
        
#%% Calcular la probabilidad de sacar generala servida con N tiradas

N= 10000

# Si una generala es servida es generala devuelve TRUE y es igual a 1
# En G se suman todas las generalas servidas en el total de N lanzamientos
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

