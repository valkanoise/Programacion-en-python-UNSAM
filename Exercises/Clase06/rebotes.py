# rebotes.py
# Archivo de ejemplo
# Ejercicio

altura = 100
perdida_por_rebote = 3/5
nro_rebote = 1

while nro_rebote <= 10:
    altura = altura * perdida_por_rebote
    print(nro_rebote, round(altura, 4))     #uso función round(valor, digitos_decimales) para redondear el resultado
    nro_rebote = nro_rebote + 1
    
    
# otra opción

# for i in range (1,11):
#     altura = altura * perdida_por_rebote
#     print(nro_rebote, altura)
#     nro_rebote = nro_rebote + 1