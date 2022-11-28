import random
from collections import Counter

def tirar(nro_dados):
    '''Función que crea una lista con 5 numeros (entre 1-6) al azar'''
    tirada=[]
    for i in range(nro_dados):
        tirada.append(random.randint(1,6)) 
    return tirada


def es_generala(tirada):
    '''función que devuelve True si y sólo si los cinco dados de la lista 
    tirada son iguales.'''
    if min(tirada)==max(tirada):
        return True
    else:
      return False

def prob_generala(N=1):
    '''Funcion que simula con N repeticiones la probabilidad de obtener una 
    generala al finalizar una mano de tres tiradas.
    Si en la primer mano no salen dados repetidos se vuelven a tirar todos los 
    dados restantes'''
    
    suma_generalas = 0
    
    for i in range(N):    
        repetidos = []
        nro_repetido = 0
    
        # por cada mano tenemos 3 tiradas o sacamos generala
        for i in range(3) or len(repetidos)!=5:
            
            #cambio el nro de dados a tirar en la mano 2 y 3 según si hay dados repetidos
            tirada = tirar(5-len(repetidos))
            # print(tirada)
            
            #dentro de la tirada busco el nro y repeticiones del dado mas repetido de la tirada
            try: 
                dado_valor_rep = Counter(tirada).most_common(1)[0]
                nro = dado_valor_rep[0]
                rep = dado_valor_rep[1]
                # print(f'Nro: {nro} con: {rep} repeticiones')
                
                # si es la 1er mano o no hay dados almacenados
                # si hay dado con mas de 2 repeticiones lo agrego a la lista de repetidos
                # tambien guardo el nro del dado repetido para buscarlo en la proxima mano
                if len(repetidos) == 0:
                    if rep >= 2:
                        repetidos = [i for i in tirada if i == nro]
                        # for i in tirada:
                        #     if i == nro:
                        #         repetidos.append(i)
                        nro_repetido = nro
                
                # si ya hay dados almacenados con cierto nro
                # busco en la nueva tirada los dados con valor a nro_repetido para ir sumando dados a la generala
                else:
                    for i in tirada:
                        if i == nro_repetido:
                            repetidos.append(i)
                
            except IndexError:
                pass
        # si hay lista con len = 5 significa que es una generala y la sumo a la lista de generalas
        if len(repetidos) == 5:
            suma_generalas += 1
        # print(repetidos)

    # Calculo suma total de generalas / numero de iteraciones    
    probabilidad = suma_generalas/N
        
    return probabilidad
    
def prob_generala_extra(N=1):
    '''Funcion que simula con N repeticiones la probabilidad de obtener una 
    generala al finalizar una mano de tres tiradas.
    Si en la primer mano no salen dados repetidos se elige uno al azar y se
    tiran todos los 4 dados restantes'''
        
    suma_generalas = 0
    
    for i in range(N):    
        repetidos = []
        nro_repetido = 0
    
        # por cada mano tenemos 3 tiradas o sacamos generala
        for i in range(3) or len(repetidos)!=5:
            
            #cambio el nro de dados a tirar en la mano 2 y 3 según si hay dados repetidos
            tirada = tirar(5-len(repetidos))
            # print(tirada)
            
            #dentro de la tirada busco el nro y repeticiones del dado mas repetido de la tirada
            try: 
                dado_valor_rep = Counter(tirada).most_common(1)[0] #devuelve tupla (nro.dado, nro.repeticiones)
                nro = dado_valor_rep[0]
                rep = dado_valor_rep[1]
                # print(f'Nro: {nro} con: {rep} repeticiones')
                
                # si es la 1er mano o no hay dados almacenados
                # si hay dado con mas de 2 repeticiones lo agrego a la lista de repetidos
                # tambien guardo el nro del dado repetido para buscarlo en la proxima mano
                if len(repetidos) == 0:
                    if rep >= 2:
                        repetidos = [i for i in tirada if i == nro]
                        # for i in tirada:
                        #     if i == nro:
                        #         repetidos.append(i)
                        nro_repetido = nro
                    
                    #### EXTRA ####
                    # si no hay generala pre-armada y en la primer mano no salen dados repetidos, elijo uno al azar
                    else:
                        repetidos.append(random.choice(tirada))
                
                # si ya hay dados almacenados con cierto nro
                # busco en la nueva tirada los dados con valor a nro_repetido para ir sumando dados a la generala
                else:
                    for i in tirada:
                        if i == nro_repetido:
                            repetidos.append(i)
                
            except IndexError:
                pass
        
        #Chequeo si es generala con la funcion es_generala()
        if es_generala(repetidos):
            suma_generalas += 1
        
        # # Otra forma de chequear si es genala sería...
        # # si hay lista con len = 5 significa que es una generala y la sumo a la lista de generalas
        # if len(repetidos) == 5:
        #     suma_generalas += 1
        # # print(repetidos)

    # Calculo suma total de generalas / numero de iteraciones    
    probabilidad = suma_generalas/N
        
    return probabilidad

if __name__ == '__main__':
    print(prob_generala(10000))
    print(prob_generala(10000))


# Hago las iteraciones 100 millones de veces
# suma_generala = 0
# suma_generala_extra = 0
# iteraciones = 10000
# for i in range (iteraciones):
    
#     suma_generala += prob_generala(iteraciones)
#     suma_generala_extra += prob_generala(iteraciones)

# promedio_generala = suma_generala / iteraciones
# promedio_generala_extra = suma_generala_extra / iteraciones


# print(promedio_generala / promedio_generala_extra)

###################### RESULTADO ITERACIONES #################
# Resultado generala / generala_extra = 1.0001513824105943
# NO HAY DIFERENCIA ENTRE ELEGIR UN DADO AL AZAR O TIRAR TODOS DE VUELTA
