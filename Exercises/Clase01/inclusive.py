'''Traductor (rústico) al lenguaje inclusivo
Queremos hacer un traductor que cambie las palabras masculinas de una frase por 
su versión neutra. Como primera aproximación, completá el siguiente código para 
reemplazar todas las letras 'o' que figuren en el último o anteúltimo caracter 
de cada palabra por una 'e'. Por ejemplo 'todos somos programadores' pasaría a 
ser 'todes somes programadores'. Guardá tu código en el archivo inclusive.py'''


frase = 'Todos, tu también'
palabras = frase.split() 
frase_inclusiva = [] 


for palabra in palabras:
    if 'o' in palabra[-3:]: 
        palabra = palabra[:-3]+palabra[-3:].replace('o','e') 
        frase_inclusiva.append(palabra) 
        
    else: 
        frase_inclusiva.append(palabra)


frase_t = ' '.join(frase_inclusiva)
print(frase_t)