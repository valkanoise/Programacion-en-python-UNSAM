import numpy as np
import random
import timeit as tt
import matplotlib.pyplot as plt

def generar_lista(N):
    '''
    genere una lista aleatoria de largo N con nÃºmeros enteros del 1 al 1000 
    (puede haber repeticiones).
    '''
    
    # Genero una lista con valores desde 1 hasta 1000
    lista = list(np.array([i for i in range(1,1001)]))
    
    # Selecciono al azar y con reposiciÃ³n N elementos de la lista
    seleccion = random.choices(lista, k=N)
    
    return seleccion

def generar_listas(Nmax):
    ''' Genera una lista de listas, una de cada longitud entre 1 y Nmax, con 
    valores aleatorios entre 1 y 1000.
    '''
    
    listas = []
    
    for i in range (1,Nmax+1):
            
        # 1ro genero la lista de tamaÃ±o N
        listas.append(generar_lista(i))
    
    return listas

#%%
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        # lo que hace es intercambiar posiciones, al elemento más grande de posición[p] lo pone al final con posicion [n] y viceversa, al ultimo elemento lo pone donde estaba el más grande
        lista[p], lista[n] = lista[n], lista[p]
        # print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1 para seguir iterando hacta que n = 0 y while sea False
        n = n - 1
    
    return lista

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

#%%
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
        # print("DEBUG: ", lista)

    return lista

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v

#%%

def ord_burbujeo(lista):
    # defino la cantidad de pasadas = cantidad elementos - 1
    for pasada in range(len(lista)-1,0,-1):
        # en cada pasada comparo i contra i+1
        for i in range(pasada):
            if lista[i]>lista[i+1]:
                # hago asignación simultánea en una sola fila, intercambio [i] con [i+1] si i menor a i+1
                lista[i], lista[i+1] = lista[i+1], lista[i]
    
    return lista

#%% Ejercicio 12.7

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado
                


#%%
def experimento_timeit(Nmax):
    '''
    para N entre 1 y Nmax genere una lista de largo N con números enteros 
    del 1 al 1000 en orden aleatorio, calcule el tiempo que tarda cada método 
    en ordenar la lista y guarde estos resultados en tres vectores de largo Nmax
    '''
    
    tiempos_seleccion = []
    tiempos_insercion = []
    tiempos_burbujeo = []
    tiempos_mergesort = []
    
    global lista
    
    # Se generan las listas que se usaran para medir los tiempos en cada metodo
    listas = generar_listas(Nmax)
    
    
    for lista in listas:
        
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = 1, globals = globals())
        
        tiempo_insercion = tt.timeit('ord_insercion(lista.copy())', number = 1, globals = globals())

        tiempo_burbujeo = tt.timeit('ord_burbujeo(lista.copy())', number = 1, globals = globals())
        
        tiempo_mergesort = tt.timeit('merge_sort(lista.copy())', number = 1, globals = globals())

    
        tiempos_seleccion.append(tiempo_seleccion)
        tiempos_insercion.append(tiempo_insercion)
        tiempos_burbujeo.append(tiempo_burbujeo)
        tiempos_mergesort.append(tiempo_mergesort)
    
    # Devuelve un vector con los tiempos que tardo cada metodo en ordenar cada lista
    return tiempos_seleccion, tiempos_insercion, tiempos_burbujeo, tiempos_mergesort

#%% Graficar

if __name__ == '__main__':
    # Defino el largo de las listas
    Nmax = 250
    # Defino el eje X y sus valores
    largos = np.arange(Nmax)
    tiempos_seleccion, tiempos_insercion, tiempos_burbujeo, tiempos_mergesort = experimento_timeit(Nmax)
    # Grafico los 3 vectores, uno para cada metodo de ordenamiento
    plt.plot(largos,tiempos_seleccion,label = 'Tiempos ord_seleccion')
    plt.plot(largos,tiempos_insercion, '--', label = 'Tiempos ord_insercion')
    plt.plot(largos,tiempos_burbujeo, ":", label = 'Tiempos ord_burbujeo')
    plt.plot(largos,tiempos_mergesort, label = 'Tiempos merge_sort')
    
    # Grafico titulos
    plt.xlabel("Largo de la lista")
    plt.ylabel("Tiempo de comparacion")
    plt.title("Tiempos de ordenamiento vs longitud de la lista")
    plt.legend()
    plt.show()
    
