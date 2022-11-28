value = 42863.1

# imprime valor tal cual fue asignado a value
print(value)

# imprime el valor con 4 decimales
print(f'{value:0.4f}')

# imprime el valor con 2 decimales y alineado a la derecha, 
# dentro de un campo de 16 caracteres
print(f'{value:>16.2f}')

# imprime el valor con 2 decimales y alineado a la izquierda, 
# dentro de un campo de 16 caracteres
print(f'{value:<16.2f}')

# acá * funciona como un caracter de relleno. La coma indica usar separador de miles
print(f'{value:*>16,.2f}')

# el sombrerito indica que se quiere tener el texto centrado y rellenar con *
print(f'{value:*^16,.2f}')