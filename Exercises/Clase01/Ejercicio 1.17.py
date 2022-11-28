'''Ejercicio 1.17: Iteración sobre cadenas
Usá el comando for para iterar sobre los caracteres de una cadena.

>>> cadena = "Ejemplo con for"
>>> for c in cadena:
        print('caracter:', c)

# Mirá el output.
Modificá el código anterior de manera que dentro del ciclo el programa cuente cuántas 
letras "o" hay en la cadena.'''


cadena = "Ejemplo con for"
# inicializo una variable para contar
contador = 0  

for c in cadena:
    print("caracter:",c)
    if c == 'o':
        contador = contador + 1
        
print('Total de letras "o" en cadena:', contador)