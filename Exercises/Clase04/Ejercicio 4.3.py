'''En este primer ejercicio tenés que escribir una función buscar_u_elemento() 
que reciba una lista y un elemento y devuelva la posición de la última aparición 
de ese elemento en la lista (o -1 si el elemento no pertenece a la lista).
'''

def buscar_u_elemento (lista, elemento):
    ultima_pos = -1
    index = len(lista) - 1 #index del ultimo elemento de la lista
 
    #voy a mirar todos los elementos desde atrás hacia adelante
    while index >= 0: #es un loop hasta llegar al index 0
        if lista[index] == elemento:
            ultima_pos = index
            break        
        index -= 1    
    
    return ultima_pos
       
        
#%% Para probar que funciona
prueba = [2,2,3,2,2,3,5,3]
print(buscar_u_elemento(prueba, 3))

