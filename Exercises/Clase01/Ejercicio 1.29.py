'''Traductor (rústico) al lenguaje inclusivo
Queremos hacer un traductor que cambie las palabras masculinas de una frase por 
su versión neutra. Como primera aproximación, completá el siguiente código para 
reemplazar todas las letras 'o' que figuren en el último o anteúltimo caracter 
de cada palabra por una 'e'. Por ejemplo 'todos somos programadores' pasaría a 
ser 'todes somes programadores'. Guardá tu código en el archivo inclusive.py'''


frase = 'Todos, tu también'
palabras = frase.split() #se arma una lista con las palabras del string 'frase' delimitados por espacio
frase_inclusiva = [] # creo una lista vacia donde se sumaran las palabras inclusiva y no inclusivas


for palabra in palabras:
    if 'o' in palabra[-3:]: # condicional para ver si hay letra 'o' en los 3 ultimos caracteres de palabra (por si llega haber una ',')
        palabra = palabra[:-3]+palabra[-3:].replace('o','e') #concanteno todo el comieno de la palabra con las dos ultimos caracteres reemplazados por lenguaje inclusivo
        frase_inclusiva.append(palabra) #ahora agrego la palabra inclusiva a la nueva lista inclusiva
        
        
    else: #a las palabras sin genero no se las modifica y se las agrega a la lista inclusiva
        frase_inclusiva.append(palabra)

frase_t = ' '.join(frase_inclusiva) #uno todas las palabras de la lista inclusiva dejando un espacio entre ellas y se forma un string
print(frase_t)