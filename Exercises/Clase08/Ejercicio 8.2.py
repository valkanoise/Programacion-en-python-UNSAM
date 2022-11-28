from datetime import date


hoy = date.today()
prox_primavera = date(hoy.year + 1, 9,21) 

# Calculo la diferencia entre la prox. primavera y hoy, genera un delta con días y horas
dias_horas_hasta_primavera = prox_primavera - hoy

# Para tener solo los días se usa el atributo days
dias_hasta_primavera = dias_horas_hasta_primavera.days


print(f' Faltan {dias_hasta_primavera} días para la primavera')

