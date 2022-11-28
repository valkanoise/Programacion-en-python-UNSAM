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
        print("DEBUG: ", p, n, lista)

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

#%% Pruebas
print('Primera lista')
lista0 = [1, 2, 3, 4, 5]
z0= ord_seleccion(lista0)
print('\n Segunda lista')
# Incluso si ya está ordenada la lista hace todas las comparaciones
lista = [1, 2, 3, 4, 5]
z= ord_seleccion(lista)
