def diccionario_ger(lista_palabras):
    palabra_ger = ''
    diccionario = {}
    for palabra in lista_palabras:
        for letra in palabra:
            if letra in 'aeiou':
                letra = letra + 'p' + letra
            palabra_ger = palabra_ger + letra
        # print(palabra, palabra_ger)
        diccionario[palabra] = palabra_ger
        palabra_ger = ''
            
    return diccionario

#Prueba 
print(diccionario_ger(['banana', 'manzana', 'mandarina']))


        
                