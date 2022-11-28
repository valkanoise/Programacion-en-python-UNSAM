def bbinaria_rec(lista, e):
    
    # Casos bases
    if len(lista) == 0:
        res = False
    
    elif len(lista) == 1:
        res = lista[0] == e
    
    # Casos recursivos, se va achicando la lista a la mitad cada vez
    else:
        # busco punto medio
        medio = len(lista)//2
        
        # Si e es mayor al punto medio ahora la lista es la mitad derecha
        if lista[medio] <= e:
            lista = lista[medio:]
        
        # Si e es menor al punto medio ahora la lista es la mitad izquierda
        else:
            lista = lista[:medio]
        
        res = bbinaria_rec(lista,e)

    
    return res


#%% Prueba
if __name__ == '__main__':
        
    listaPrueba = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(bbinaria_rec(listaPrueba, 11))
    print(bbinaria_rec(listaPrueba, 13))