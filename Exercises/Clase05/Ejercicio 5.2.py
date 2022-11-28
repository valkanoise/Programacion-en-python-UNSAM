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
    suma_generalas = 0
    
    for i in range(N):    
        repetidos = []
        nro_repetido = 0
    
        for i in range(3) or len(repetidos)==5:
            
            tirada = tirar(5-len(repetidos))
            # print(tirada)
            try: 
                dado_valor_rep = Counter(tirada).most_common(1)[0]
                nro = dado_valor_rep[0]
                rep = dado_valor_rep[1]
                # print(f'Nro: {nro} con: {rep} repeticiones')
                
                if len(repetidos) == 0:
                    if rep >= 2:
                        for i in tirada:
                            if i == nro:
                                repetidos.append(i)
                        nro_repetido = nro
                    
                else:
                    for i in tirada:
                        if i == nro_repetido:
                            repetidos.append(i)
                
            except IndexError:
                pass
        
        if len(repetidos) == 5:
            suma_generalas += 1
        # print(repetidos)

        
    probabilidad = suma_generalas/N
        
    return probabilidad
    



print(prob_generala(100000))