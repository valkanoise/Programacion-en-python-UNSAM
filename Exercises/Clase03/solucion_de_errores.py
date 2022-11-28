#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era que no iteraba todos los elementos del str ni consideraba la letra A mayúscula.
#    Lo corregí eliminando el else y agregando el metodo lower() en la linea 14
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() == 'a':
            return True
        # else:
        #     return False
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print (tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))



#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: Los errores eran numerosos errores sintácticos: Faltaban ":", y False mal escrito
#    Lo corregí agregando ":" en varios lugares y escribiendo False en vez de Falso en la linea 38
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))



#%%
#Ejercicio 3.3: Tipos
#Comentario: El error ocurría al ingresar una expresion que no fuera un string.
#    Lo corregí convirtiendo las expresiones a string en la linea 54.
#    A continuación va el código corregido


def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))


#%%
#Ejercicio 3.4: Alcances
#Comentario: El error ocurría dado que la función devolvía None como resultado.
#    Lo corregí agregando la declaración return en la linea 79
#    A continuación va el código corregido


def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)

print(f"La suma da {a} + {b} = {c}")


#%%
#Ejercicio 3.5: Pisando memoria
#Comentario: El error ocurría dado que la función devolvia una lista con diccionarios iguales.
#    Lo corregí sacando el dict registros{} de la linea 100 y lo puse dentro de la iteración para vaciarlo antes de cada ciclo
#    A continuación va el código corregido


import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)







