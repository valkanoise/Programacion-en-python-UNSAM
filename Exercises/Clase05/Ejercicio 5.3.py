import random
from collections import Counter


def prob_cumple(N=1):
    ''' estima la probabilidad de que en un grupo de 30 personas elegidas al 
    azar, dos cumplan años el mismo día'''
    
    suma = 0
    for iteracion in range(N):
        
        #Elijo 30 fecha de cumple años al azar
        #A partir de una lista de 365 elementos armo al azar una lista de 30 elementos
        lista = [random.choice([cumple for cumple in range(1,366)]) for persona in range(30)]
        
        #Cuento el numero de cumples repetidos
        contador = Counter(lista)
        
        # print(contador.most_common(1))
        
        #Si el conteo de la fecha mas repetida es mayor o igual a 2 sumo 1 a la variable suma
        if contador.most_common(1)[0][1]>=2:
            suma += 1
        #     print(True)
        # else:
        #     print(False)
            
        # print(suma)
    probabilidad = suma / N
    print(f'La probabilidad es: {probabilidad} en: {N} iteraciones')
    return suma/N

if __name__ == '__main__':
    print(prob_cumple(10000))