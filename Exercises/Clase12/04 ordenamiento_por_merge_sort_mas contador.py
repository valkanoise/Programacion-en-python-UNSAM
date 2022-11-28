

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve tupla: (una nueva lista ordenada y nro de comparaciones) ."""
    if len(lista) < 2:
        lista_nueva = lista
        comparaciones = 0
    else:
        medio = len(lista) // 2
        izq, comp_izq = merge_sort(lista[:medio])
        der, comp_der = merge_sort(lista[medio:])
        lista_nueva, comp_merge = merge(izq, der)
        comparaciones = comp_izq + comp_der + comp_merge
    return lista_nueva, comparaciones

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    comparaciones_extra =0

    while(i < len(lista1) and j < len(lista2)):
        comparaciones_extra += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, comparaciones_extra